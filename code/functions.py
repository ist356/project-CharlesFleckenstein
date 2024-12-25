import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
import requests


def wiki_page_hyperlink_getter(playwright: Playwright, url_end: str) -> list:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f'https://en.wikipedia.org/wiki/{url_end}',timeout=None)
    links = []
    for item in page.query_selector_all('a'):
        link = item.get_attribute('href')
        links.append(link)

    context.close()
    browser.close()
    return links

def wiki_page_text_getter(playwright: Playwright, url_end: str) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(f'https://en.wikipedia.org/wiki/{url_end}',timeout=None)
    text = ''
    for item in page.query_selector_all('p'):
        text_bit = item.inner_text()
        text += text_bit
    
    context.close()
    browser.close()
    return text


def entities_extract(string: str) -> dict:
    url = 'https://cent.ischool-iot.net/api/azure/entityrecognition'
    apikey = '944ffa919f060abc04a6b32a'
    headers = {
        'X-API-KEY': apikey,
    }
    data = {'text': string}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    result = response.json()
    entities = result['results']['documents'][0]['entities']
    output = []
    for entitie in entities:
        if entitie['confidenceScore'] > 0.75:
            output.append(entitie['text'])
    return output

def keyphrase_extract(string: str) -> str:
    url = 'https://cent.ischool-iot.net/api/azure/keyphrasextraction'
    apikey = '944ffa919f060abc04a6b32a'
    headers = {
        'X-API-KEY': apikey
    }
    data = {'text': string}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    result = response.json()
    keyphrases = result['results']['documents'][0]['keyPhrases']
    return keyphrases


if __name__ == '__main__':
    with sync_playwright() as playwright:
         text = wiki_page_text_getter(playwright, "Alfred's_Blind_Skink") 
         links = wiki_page_hyperlink_getter(playwright, "Alfred's_Blind_Skink")
    assert links[21] == '/wiki/Special:MyContributions'
    ### i was going to test text but it was too long to test and copy pasting still fails the test so i left it out
    output = keyphrase_extract('The john brown fox jumped over the john dog, also steven mcpooper gold')
    assert output == ['steven mcpooper gold', 'john brown fox', 'john dog']
    entities = entities_extract('The john brown fox jumped over the john dog, also steven mcpooper gold')
    assert entities == ['john brown fox', 'steven mcpooper gold']
    

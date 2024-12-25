import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    link_items = []
    page.goto("https://en.wikipedia.org/wiki/Special:AllPages?from=alfred&to=&namespace=0",timeout=None) 
    link_items = []
    target_page = "https://en.wikipedia.org/w/index.php?title=Special:AllPages&from=A%C5%A1irat+Northeastern+Neo-Aramaic"
    current_page = "https://en.wikipedia.org/wiki/Special:AllPages?from=alfred&to=&namespace=0"   
     #write a loop that goes through all pages, but stops when it reached the page listed below
    # "/w/index.php?title=Special:AllPages&amp;from=A%C5%A1irat+Northeastern+Neo-Aramaic" :

    # there were too many pages: i ran it up to the letter c adn it was 220 gb 
    
    for i in range(20):
        page.goto(current_page, timeout=None)
    
        for item in page.query_selector_all("li"):
            next = item.inner_text()
            if next == '':
                continue
            else:
                link_item = next.replace(' ','_')
                link_items.append(link_item)
        # with open('cache/link_items_A.csv', 'a') as f:
        #     for item in link_items:
        #         f.write("%s\n" % item)                 
        next_page_list = []
        for thing in page.query_selector_all("a "):
                title = thing.get_attribute('title')

                if title == 'Special:AllPages': 
                    next_page_list.append(thing.get_attribute('href'))
                else: 
                      continue
                
        if target_page in next_page_list:
            break
        if next_page_list:
            current_page = f'https://en.wikipedia.org/{next_page_list[1]}'

        next_page_list = []
        page.goto(current_page,timeout=None)
        
    df = pd.DataFrame(link_items, columns=['link_items'])
    df.to_csv('cache/Alfreds.csv', index=False)


#/w/index.php?title=Special:AllPages&amp;from=%5Cn
#/w/index.php?title=Special:AllPages&amp;from=A




    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)


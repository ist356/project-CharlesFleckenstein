import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd
import streamlit as st
import seaborn as sns
from functions import wiki_page_hyperlink_getter, wiki_page_text_getter, entities_extract, keyphrase_extract
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Wikipedia Viewer')
df_art = pd.read_csv('cache/fred_items_final.csv')
articles = df_art['link_items'].tolist()

options = st.selectbox('Options',['Compare Alfreds', 'Alfred Lookup'])
output = ''
if options == 'Alfred Lookup':
    text = st.text_input('Article Lookup','Search for Article Here')
    search_results = []
    run_button = st.button('Run')
    if text:
        for item in articles:
            if text in item:
                search_results.append(item)
        st.write(search_results)
    if run_button:
        print(search_results)
        if search_results[0] == text:
            with sync_playwright() as playwright:
                output = wiki_page_text_getter(playwright, search_results[0])
                st.write(f'Article Found: {output}')
                entities = entities_extract(output)
                keyphrases = keyphrase_extract(output)
                hyperlinks = wiki_page_hyperlink_getter(playwright, search_results[0])
                st.write(f'Entities: {entities}')
                st.write(f'Keyphrases: {keyphrases}')
                st.write(f'Hyperlinks: {hyperlinks}')
        else:
            st.write('too many articles give me one')
if options == 'Compare Alfreds':
    text = st.text_input('Article Lookup','Search for Article Here')
    search_results1 = []
    art_1 = ''
    art_2 = ''
    add_art1 = st.button('Add Article 1')
    add_art2 = st.button('Add Article 2')
    compare_button = st.button('Compare')
    if text:
        for item in articles:
            if text in item:
                search_results1.append(item)
        st.write(search_results1)
    if add_art1:
        art_1 = text
    if add_art2:
        art_2 = text
    if compare_button:
        with sync_playwright() as playwright:
            hyperlinks1 = wiki_page_hyperlink_getter(playwright, art_1)
            hyperlinks2 = wiki_page_hyperlink_getter(playwright, art_2)
            plot, series = plt.subplots()
        df1 = pd.DataFrame(hyperlinks1, columns=['hyperlinks'])
        df1['count'] = 1
        df2 = pd.DataFrame(hyperlinks2, columns=['hyperlinks'])
        df2['count'] = 1

        figure1, series1 = plt.subplots()
        figure2, series2 = plt.subplots()

        sns.barplot(data = df1, x = hyperlinks1,  y='count', estimator='sum', ax = series1 ).set_title('amount fo hyperlinks per article compare')
        sns.barplot(data = df2, x = hyperlinks2,  y='count', estimator='sum', ax = series1 ).set_title('amount fo hyperlinks per article compare')
        st.pyplot(figure1)
        st.pyplot(figure2)

    
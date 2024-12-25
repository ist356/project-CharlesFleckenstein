











    # letters = ['m','n','o']#,'p','q','r','s','t','u','v','w','x','y','z']
    #page.get_by_role("link", name="Next page (Änglahund)").first.click()
    # # for letter in letters:
    # #     page.goto(f"https://en.wikipedia.org/wiki/Special:AllPages/{letter}",timeout=None)
    # #     for item in page.query_selector_all("li"):
    # #         next = item.inner_text()
    # #         if next == '':
    # #             continue
    # #         else:
    # #             link_item = next.replace(' ','_')
    # #             link_items.append(link_item)
    # # df = pd.DataFrame(link_items, columns=['link_items'])
    # # df.to_csv('cache/link_items.csv', index=False)

    # ### I was looking thougn the existing items that I had pulled and noticed a lot was missing,
    # ###  and the was the page im scrapign from work is with a selector for page type
    # ### previously i had it set to jsut articles, but i think this category selector will fill in the gaps in this data

    # #set up lists
    # category_list = []
    # # below is the skip list which are items lso found unde rthe li tag but are not article links
    # skip_list = ['Donate', 'Create account', 'Log in','Donate',' Create account',' Log in','Upload file']

    # ### Get all categories
    # for letter in letters:
    #     page.goto(f"https://en.wikipedia.org/wiki/Special:AllPages?from={letter}&to=&namespace=14",timeout=None)
    #     for subject in page.query_selector_all("li"):
    #         category = subject.inner_text()
    #         if category == '':
    #             continue
    #         if category in skip_list:
    #             continue
    #         else:
    #             category = category.replace(' ','_')
    #             category_list.append(category)
    # cat_item_list =[]
    # ### Get all subcategories
    # for category in category_list:
    #     page.goto(f"https://en.wikipedia.org/wiki/{category}",timeout=None)
    #     for li in page.query_selector_all("li"):
    #         sub_cat = li.inner_text()
    #         if sub_cat == '':
    #            continue
    #         else:
    #             link_item_cat = sub_cat.replace(' ','_')
    #             cat_item_list.append(link_item_cat)     
    # df = pd.DataFrame(cat_item_list, columns=['link_items']) 
    # df.to_csv('cache/cat_items(j-l).csv', index=False)
import pandas as pd
import numpy as np




# df = pd.read_csv('cache/link_items.csv')
# df_filt = df[df['link_items']!= 'Privacy_policy']
# df_filt = df_filt[df_filt['link_items']!= 'Main_Page']
# df_filt = df_filt[df_filt['link_items']!= 'About_Wikipedia']
# df_filt = df_filt[df_filt['link_items']!= 'Disclaimers']
# df_filt = df_filt[df_filt['link_items']!= 'Contact_Wikipedia']
# df_filt = df_filt[df_filt['link_items']!= 'Code_of_Conduct']
# df_filt = df_filt[df_filt['link_items']!= 'Developers']
# df_filt = df_filt[df_filt['link_items']!= 'Statistics']
# df_filt = df_filt[df_filt['link_items']!= 'Cookie_statement']
# df_filt = df_filt[df_filt['link_items']!= 'Mobile_view']
# df_filt = df_filt[df_filt['link_items']!= 'Donate']
# df_filt = df_filt[df_filt['link_items']!= '_Create_account']
# df_filt = df_filt[df_filt['link_items']!= 'Create_account']
# df_filt = df_filt[df_filt['link_items']!= '_Log_in']
# df_filt = df_filt[df_filt['link_items']!= 'Upload_file']
# df_filt = df_filt[df_filt['link_items']!= 'Log_in']
# df_filt = df_filt[df_filt['link_items']!= 'Edit_preview_settings']
# df_filt.to_csv('cache/link_items_filtered.csv', index=False)

# df = pd.read_csv('cache/Alfreds.csv')
# alfreds = df['link_items'].tolist()
# not_fred_list = []
# fred_list = []
# for item in alfreds:
#     if item not in fred_list:
#         fred_list.append(item)
#     if item in fred_list:
#         not_fred_list.append(item)
# for item in fred_list:
#     if item in not_fred_list:
#         fred_list.remove(item)

# fred_df = pd.DataFrame(fred_list, columns=['link_items'])
# fred_df.to_csv('cache/fred_items_final.csv', index=False)
df = pd.read_csv('cache/fred_items_final.csv')
freds = df['link_items'].tolist()
number_list = [1,2,3,4,5]
for i in range(4):
    print(freds[i])
    freds.remove(freds[i])
freds_df = pd.DataFrame(freds, columns=['link_items'])
print(freds_df.head(10))
#or i in range(4):
    #print(freds[i])
    


    
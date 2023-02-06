from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import time

start = time.time()

df= pd.read_csv('Output_Data_Structure.csv')
df= df['URL'][:7]

for url in df:
    page= requests.get(url)
    soup= BeautifulSoup(page.content, 'html.parser')

    # Getting all the article headings
    headings= soup.find('h1')
    print(headings.get_text())

#     # Getting all the article text in <p> tags                  
#     paras= soup.find_all('p')
#     try:
#         for text in paras:
#             print(text.get_text(),'\n')
#             file = open('data1.text','a', encoding='utf-8')
#             file.write(text.get_text())
#     except Exception as e:
#         pass

# end = time.time()
# print(end-start)





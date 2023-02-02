from bs4 import BeautifulSoup
import pandas as pd
import requests
import regex

article_headings =[]
paras = []

url= "https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/"
page= requests.get(url)
soup= BeautifulSoup(page.content, 'html.parser')
#Getting all the article headings
article_headings= soup.find_all('div',class_='td-post-content')
print(article_headings)

# # Getting all the article text
# paras= soup.find_all('p',class_='wp-block-image')
# print(paras.get_text())

# heading_file= open('heading_file.txt','w')
# heading_file.write(article_headings)
# heading_file.close()
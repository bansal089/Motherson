from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import csv
from multiprocessing import pool 

# Information Extracter for a page 
from links import links

df= pd.DataFrame()
df.to_csv('data_frame.csv')

for url in links:
    page= requests.get(url)
    soup= BeautifulSoup(page.content, 'html.parser')

    company_name= soup.find('div', class_='company_and_premium')
    print(company_name.get_text().strip())

    job_profile_name= soup.find('span', class_='profile_on_detail_page')
    print(job_profile_name.get_text())

    time_of_posting= soup.find('div', {'class':'status status-small status-inactive'})
    print(time_of_posting.get_text())

    location_of_work= soup.find('a',{'class':'location_link view_detail_button'})
    print(location_of_work.get_text())

    no_of_applicants= soup.find('div', {'class':'applications_message'})
    print(no_of_applicants.get_text())

    skills_required=soup.find('div', {'class':'round_tabs_container'})
    skills= []
    for skill in skills_required:
        skills.append(skill.get_text().replace('\n',''))
    print(skills)
    
    no_of_openings= [_.get_text(strip=True) for _ in soup.find_all(class_= 'text-container')]
    print(no_of_openings[-1])

# Saving data into pandas dataframe
    df= df.append({'company_name':company_name.get_text().strip(),
   'job_profile_name':job_profile_name.get_text(),
    'time_of_posting':time_of_posting.get_text(), 
    'location_of_work':location_of_work.get_text(), 
    'no_of_applicants':no_of_applicants.get_text(),
    'skills_required':skills, 
    'no_of_openings':no_of_openings[-1]}, ignore_index= True)


df.to_csv('data_frame.csv')
# print(df)




    




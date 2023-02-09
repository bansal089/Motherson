import pandas as pd
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pprint import pprint
from tqdm import tqdm
import re
import time
from multiprocessing import Pool

page_selector = pd.date_range(start = '1/1/2009', end= '11/1/2021', freq= 'M')
dates= []

def occuring_months():
    for i in page_selector:
        combined_date= str(i)[:4]+str(i)[5:7]
        dates.append(combined_date)

data_list= []
date_index= []

def scraper(dates):
    url= "http://www.estesparkweather.net/archive_reports.php?date="+ dates
    page= requests.get(url)
    soup= BeautifulSoup(page.content, 'html.parser')
    tables= soup.find_all('table')

    parsed_data = [row.text.splitlines() for row in tables]
    parsed_data = parsed_data[:-9]
# pprint(parsed_data)
    
    for l in range(len(parsed_data)):
        parsed_data[l]= parsed_data[l][2:len(parsed_data[l]):3]
# # pprint(parsed_data)

    for i in range(len(parsed_data)):
        raw_data = ['.'.join(re.findall("\d+",str(parsed_data[i][j].split()[:5]))) for j in range(len(parsed_data[i]))]
    # print(raw_data)
        data_list.append(raw_data)
    # print(data_list)
        date_index.append(dates + raw_data[0])
    # pprint(date_index)

    formated_data= [data_list[i][1:] for i in range(len(data_list)) if len(data_list[i][1:]) == 19]
    # pprint(formated_data)
    col=['Average temperature (°F)', 'Average humidity (%)','Average dewpoint (°F)', 
        'Average barometer (in)','Average windspeed (mph)', 'Average gustspeed (mph)','Average direction (°deg)', 'Rainfall for month (in)',
        'Rainfall for year (in)', 'Maximum rain per minute','Maximum temperature (°F)', 'Minimum temperature (°F)','Maximum humidity (%)', 
        'Minimum humidity (%)', 'Maximum pressure','Minimum pressure', 'Maximum windspeed (mph)',
        'Maximum gust speed (mph)', 'Maximum heat index (°F)']
    
    f_index = [date_index[i] for i in range(len(date_index)) if len(date_index[i]) > 6]
    index_col = [datetime.strptime(str(f_index[i]), '%Y%m%d').strftime('%Y-%m-%d') for i in range(len(f_index))]
    # pprint(index_col[:10])
        
    final_data = pd.DataFrame(formated_data, columns = col, index = f_index)
    print(final_data.head())   
# final_data.to_csv("Weather_Data.csv")
    return final_data


def run():
    p= Pool()
    x= p.map(scraper, dates)
    p.terminate()
    # p.join()  
    
if __name__ == "__main__":
    start= time.time()
    occuring_months()
    run()
    end= time.time()
    print(end-start)

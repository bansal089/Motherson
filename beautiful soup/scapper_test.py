
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent= r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

# Step 3: HTML Tree trasversal

# Get the title of HTML page
title= soup.title
print(type(title.string))

# Get first element in the HTML page
print(soup.find('p'))

# Get classes of any element in the HTML page
print(soup.find('p')['class'])

# Find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# Get the text from tags/soup (from first paragraph)
print(soup.find('p').get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()

# Get all the links of a page
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)
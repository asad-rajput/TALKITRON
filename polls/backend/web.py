# import requests
# from bs4 import BeautifulSoup


# # Making a GET request
# r = requests.get("https://www.flipkart.com/laptops/")

# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')

# # Finding by id
# s = soup.find('div', id= 'main')

# # Getting the leftbar
# # leftbar = s.find('ul', class_='leftBarList')

# # All the li under the above ul
# # lines = leftbar.find_all('li')

# for line in lines:
# 	print(line.text)

# from selenium import webdriver
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd 

# driver = webdriver.chrome ("/usr/lib/chromium-browser/chromedriver")
# products=[]
# prices=[]
# ratings=[]
# driver.get ("https://www.flipkart.com/laptops/")
# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
# 	name=a.find('div', attrs={'class':'_3wU53n'})
# 	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# 	rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# 	products.append(name.text)
# 	prices.append(price.text)
# 	ratings.append(rating.text) 
# df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')


# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.daraz.com'
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')
# title = soup.find('h3').get_text()

# print(title)


import requests
from bs4 import BeautifulSoup

url = 'https://www.daraz.com.np/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title').get_text()

print(title)

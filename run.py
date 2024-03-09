import requests
from bs4 import BeautifulSoup
import pandas as pd
# I’ve used pandas and beautiful soup in the past to retrieve stock and formula 1 data

url = 'https://www.remey-swag.com/f1/index.html'
response = requests.get(url)
pageContent = response.text

soup = BeautifulSoup(pageContent, 'html.parser')
title = soup.title.string  # Extract the page title

data = {'Website': ['Remey Swag'], 'Title': [title]}
df = pd.DataFrame(data)

print("Fetched and parsed data from a webpage:")
print(df)

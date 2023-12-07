import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://damndelicious.net/recipe-index/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the article titles (modify the selector based on the HTML structure)
    article_titles = soup.find_all('h4', class_='title')

    for title in article_titles:
        title_text = title.text.lower()
        if 'chicken' in title_text:
            print("chicken recipe was found in:", title.text)
            
    
    # Loop through the titles and print them
    for title in article_titles:
        print(title.text)
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

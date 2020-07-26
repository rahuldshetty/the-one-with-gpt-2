# importing libraris
import requests
from bs4 import BeautifulSoup

# Constants
MAIN_URL = "https://fangj.github.io/friends/"
WRITE_FILE = "output.txt"

# File handler to store the results
out_file = open(WRITE_FILE, 'w')

# Get HTML contents from the main page
r = requests.get(MAIN_URL)
soup = BeautifulSoup(r.content, 'html.parser')

items = soup.find_all("a")

for i,item in enumerate(items):
    print("Extracting:",i,"/",len(items))
    new_url = MAIN_URL + item['href']
    # Extract contents from the navigated page
    r = requests.get(new_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # for each paragraph extract contents
    try:
        for para in soup.find_all('p'):
            text = (para.text)
            out_file.write(text + "\n")
    except:
        print("Error in webpage id:", i)

print("Completed")
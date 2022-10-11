from bs4 import BeautifulSoup
import requests
import pandas as pd

def moreexchange():
    page = requests.get("""http://www.cambiossuiza.com/""")
    soup = BeautifulSoup (page.text, 'html.parser')
    tables = soup.find_all('table')
    return tables[0]

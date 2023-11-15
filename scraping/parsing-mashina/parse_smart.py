from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://softech.kg/phones/Xiaomiphones'

def parsing_smartfone():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.find('div', class_='row')
    tel = container.find('div', class_='product-thumb')
    result = []
parsing_smartfone()
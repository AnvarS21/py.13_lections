from bs4 import BeautifulSoup
import requests
import csv
import lxml

url = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
container = soup.find('div', class_='list-view')
phones = container.find_all('div', class_='item product_listbox oh')
res = []
for phone in phones:
    name = phone.find('div', class_='listbox_title oh').find('a').text
    price = phone.find('div', class_='listbox_price text-center').text.strip()
    img = phone.find('div', class_='listbox_img pull-left').find('img').get('src')
    images = 'https://www.kivano.kg' + img
    dict_ = {'name': name, 'price': price, 'images': images}
    res.append(dict_)

    

def write_to_csv(data: list):
    with open('phones.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'name', 'price', 'images']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№', 
            'name': 'Name:', 
            'price': 'Price:', 
            'images': 'images'
        })
        for car in data:
            writer.writerow({
                '№': count, 
                'name': car['name'], 
                'price': car['price'], 
                'images': car['images']
            })
            count += 1

write_to_csv(res)
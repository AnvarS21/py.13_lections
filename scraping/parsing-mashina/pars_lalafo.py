from bs4 import BeautifulSoup
import requests
import csv
import lxml


url = 'https://lalafo.kg/'
def parsing_wil():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.find('div', class_='main-feed__container')
    product = container.find_all('article', class_='adTile-wrap')
    result = []
    for prod in product:
        price = prod.find('p', class_ = 'adTile-price').text.strip()
        img = prod.find('img')
        if img is not None:
            img = prod.find('img').get('data-src')
        desc = prod.find('div', class_ = 'adTile-title__wrap').text.strip()
        name = prod.find('div', class_ = 'adTile-label-wrap')
        if name is not None:
            name = prod.find('div', class_ = 'adTile-label-wrap').text.strip()
        ava = prod.find('img', class_='userAvatar-photo')
        if ava is not None:
            ava = ava.get('data-src')
        data = {'title': name, 'desc': desc, 'price': price, 'avatar': ava, 'img': img}
        result.append(data)

        
        
    write_to_csv(result)

def write_to_csv(data: list):

    with open('lalafo.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'name', 'desc', 'price','avatar', 'image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№', 
            'name': 'Name:', 
            'desc': 'Description:',
            'price': 'Price:', 
            'avatar': 'avatar',
            'image': 'Image Url:'
        })
        for car in data:
            writer.writerow({
                '№': count, 
                'name': car['title'], 
                'desc': car['desc'],
                'price': car['price'],
                'avatar': car['avatar'],
                'image': car['img']
            })
            count += 1

parsing_wil()
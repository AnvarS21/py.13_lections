from bs4 import BeautifulSoup
import requests
import csv
import re


url = 'https://www.mashina.kg/search/all/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
container = soup.find('div', class_='table-view-list')
cars = container.find_all('div', class_='list-item')

all_url_cars = []
photos_car = []
p = []



result = []
for i in cars:
    url_cars = i.find('a').get('href')
    url_cars = 'https://mashina.kg' + url_cars
    all_url_cars.append(url_cars)

for car in all_url_cars:
    response = requests.get(car).text
    soup = BeautifulSoup(response, 'lxml')
    fotos = soup.find('div', class_='fotorama').find_all('a')
    for f in fotos:
        photos = f.get('data-full')
        p.append(photos)
    photos_car.append(p)
    p = []
    desc = soup.find('div', class_='seller-comments').text.replace('\n', ' ')



    for el in photos_car:
    
        data = {'photos': el, 'desc': desc}
        result.append(data)
print(result)

def write_to_csv(data: list):
    with open('car.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'desc', 'photos']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№', 
            'desc': 'desc',
            'photos': 'photos'
        })
        for car in data:
            writer.writerow({
                '№': count, 
                'desc': car['desc'],
                'photos': car['photos']
            })
            count += 1

write_to_csv(result)
    
    




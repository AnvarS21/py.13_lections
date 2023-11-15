import requests
from bs4 import BeautifulSoup
import lxml
count = 1
jobs_python = []
# def pars_devkg():   
#     while True:
#         flajok = True 
#         url = f'https://devkg.com/ru/jobs?page={count}'
#         print(f'Страница: {count}')
#         count += 1
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'lxml')
#         container = soup.find('div', class_ = 'jobs-list')
#         jobs = container.find_all('article', class_='item')
#         for job in jobs:
#             stop = job.find('div', 'jobs-item-field price').text
#             if len(stop) == 18:
#                 print('МЫ ОСТАНОВИЛИСЬ')
#                 flajok = False
#                 break
#             adress = job.find('a', class_='link').get('href')
#             desc = job.find('div', class_='jobs-item-field position').text.replace(' ', '')
#             if 'python' in job.find('div', class_='jobs-item-field position').text.lower().split() or 'backend' in job.find('div', class_='jobs-item-field position').text.lower().split():
#                 jobs_python.append(desc + 'Ссылка ---> https://devkg.com' + adress)

#         if flajok == False:
#             break

def pars_job_codify():
    url = 'https://www.employment.kg/vacancies'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.find('div', class_="rezums vacans").find('ul')    
    print(container)
    # print(soup)


pars_job_codify()
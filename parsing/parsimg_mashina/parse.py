from bs4 import BeautifulSoup as bs
import requests
import csv

count = 0

def get_html(url: str) -> str:
    '''Получает html код определенного сайта'''
    response = requests.get(url)
    return response.text

def get_last_page(html: str) -> int:
    soup = bs(html, 'html.parser')
    pages = soup.find('div', class_='pages fl').find_all('a', class_='pages-item')
    last_page = pages[-1].get('data-ci-pagination-page')
    return int(last_page)

def get_data(html:str) -> list:
    '''Функция парсер, получает все данные с сайта'''
    soup = bs(html, 'lxml')
    catalog = soup.find('div', class_ = 'catalog-list')
    cars = catalog.find_all('div', class_ = 'catalog-list-item')
    result = []
    for car in cars:
        
            
        name = car.find('span', class_ = 'catalog-list-capition').text.strip()
        try:
            img = car.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            img = 'No picher'
        price = car.find('span', class_='catalog-list-item-price').text
        desc1 = car.find('span', class_='catalog-year').text.strip()
        desc2 = car.find('span', class_ ='catalog-item-mileage' ).text.strip()
        desc3 = car.find('span', class_ = 'catalog-item-descr').text.strip()
        description = f'{desc1} {desc2} {desc3}'

        data = {
            'name': name,
            'price': price,
            'description': description,
            'img': img
        }

        result.append(data)

    return result

def write_to_csv(data:dict) -> None:
    '''Функция для записи всех данных в CSV файл'''

    with open('bmw.csv', 'a') as file:
        fieldnames = ['#', 'Name', 'Price', 'Description', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        global count
      
       
        for car in data:
            count += 1
            writer.writerow ({
                '#': count,
                'Name': car['name'],
                'Price': car['price'],
                'Description': car['description'],
                'Image':car['img']
            })

def prepare_csv() -> None:
    '''Функция которая подготовит csv файл'''
    with open ('bmw.csv', 'w') as file:
        fieldnames = ['#', 'Name', 'Price', 'Description', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '#': '#',
            'Name': 'Name',
            'Price': 'Price',
            'Description': 'Description',
            'Image':'Image'
            })

def main():
    i = 1
    prepare_csv()
    while True:
        url = f'https://cars.kg/offers/{i}'
        html = get_html(url)
        last_page = get_last_page(html)
        data = get_data(html)
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу!')
        if i == 94:
            break
        i += 1
        

main()
# from bs4 import BeautifulSoup as bs
# import requests
# import lxml

# URL = 'https://www.kivano.kg/'


# def get_html(url):
#     response = requests.get(url)
#     return response.text


# def get_data(html,URL):
#     soup = bs(html, 'lxml')
#     blog_products = soup.find('div', class_ = 'product_vitrina')
#     products = blog_products.find_all('div',class_ ='product_box')
#     list_ = []
#     for product in products:
#         title = product.find('div', class_ = 'product_title').text
#         price = product.find('div', class_ = 'product_price').text.replace('\n', '')
#         img_div = product.find('div', class_ ='product_img')
#         img = img_div.find('img').get('src')

#         list_.append({'title':title, 'price':price, 'image': f"{URL}{img.replace('/', '', 1)}"})
#     return list_[-1]

# html = get_html(URL)
# print(get_data(html,URL))



from bs4 import BeautifulSoup
import requests
import csv 
source = requests.get('https://www.wikipedia.org/').text
my_page = BeautifulSoup(source, 'lxml')
blog_lang = my_page.find('div', class_ = 'central-featured-lang lang4')




print(blog_lang.text)











# from bs4 import BeautifulSoup as bs
# import requests
# import lxml



# url ='https://www.wikipedia.org/'

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html,url):
#     soup = bs('lxml')
#     name_ = soup.find('div',class_ = 'central-featured-lang lang4').text
#     name1_ = name_.find_all('div', class_ = 'small').text

# print(get_data)

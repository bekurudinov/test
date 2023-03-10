import peewee
from models import Category, Product
import random


def add_category(name):
    try:
        data = Category(name=name.lower().strip())
        data.save()
        print(f'Сохранили категорию {name.strip()}!')
    except (peewee.IntegrityError, peewee.InternalError):
        print('такая категория уже сушествует')

# add_category('   платья   ')
# add_category('джинсы')
# add_category('футболки')
# add_category('свитеры')
# add_category('обуви')


def add_product(name, price, category_name):
    try:
        category_id = Category.get(name=category_name.lower().strip())
    except peewee.DoesNotExist:
        category_id = None

    if category_id:
        data  = Product(title=name, price=price, category_id=category_id)
        data.save()
        print(f'сохранили товар {name}!')
    else:
        print(f'категории {category_name} не сушествует!')

# add_product('Zara', 300, 'платья')

# add_product('adidas ', 500, 'джинсы')

# add_product('Puma keps', 600, 'футболки')

# add_product('nike air jordan', 1000, 'свитеры')

# add_product('badlon', 200, 'обуви')


'''===========Добавление данных========='''
# add_category('cars')
# add_category('telefony')

# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     # print(ls)
#     for x in ls:
#         name =x.replace('\n', '')
#         price  =random.randint(5000, 200000)
#         add_product(name,price, 'cars')
'''====================================='''
with open('files/telefon.txt', 'r')as file:
    ls = file.readlines()
    for x in ls:
        name = x.replace('n', '')
        price = random.randint(200, 1000)
        add_product(name, price, 'telefony')
from models import Product, Category


# обновление данных
# query = Product.update(price=500).where(Product.title=='adidas')
# print(query)
# query.execute()
# query = Product.update(price = (Product.price + Product.price * 0.5))#увеличиваем всем товарыфм цены
# query.execute()

# query = Product.update(price=200000).where(Product.category_id==1 and Product.category_id==3)
# query.execute()



# удаление данных
# удаление через запрос
# query = Product.delete().where(Product.id == 5)
# query.execute()

# удаление через объект

# product = Product.get(id =3)
# print(product, product.title)
# product.delete_instance()


query = Product.delete().where(Product.id>=1)
print(query)
query.execute()
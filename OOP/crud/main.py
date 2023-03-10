from views import CreateMixin, ReadMixins, UpdateMixin, DeleteMixin


class Product(CreateMixin, ReadMixins, UpdateMixin, DeleteMixin):
    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4)
        return 'Saved!'

    
smartphones = Product()
print(smartphones.post(title ='Redmi Note 10', descreption = 'The best phone for own price', qty = 5, price = 250))

print(smartphones.post(title ='Redmi Note 5', descreption = 'The best phone for own price', qty = 10, price = 1000))

print(smartphones.post(title ='Iphone Xs', descreption = 'The best phone for own price', qty = 50, price = 10000))

print(smartphones.post(title ='Iphone 14 pro max', descreption = 'The best price', qty = 20, price = 100000))

print(smartphones.post(title ='Nokia', descreption = 'The best ', qty = 15, price = 500))
print()
print(smartphones.list())
print()
print(smartphones.detail(5))
print(smartphones.detail(15))
print()
print(smartphones.patch(5, title='Poco Phone 20', price = 500))
print(smartphones.patch(15, title='Poco Phone 20'))
print()
print(smartphones.list())
print(smartphones.save())
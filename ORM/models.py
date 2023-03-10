import peewee
from main import db
from datetime import datetime

class Category(peewee.Model):
    category_id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=50, unique = True)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'categories'
        order_by = ('created_at',)
class Product(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    title = peewee.CharField(max_length=50)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=100)
    category_id = peewee.ForeignKeyField(Category, to_field='category_id', on_delete='cascade', related_name='products')
    created_at =peewee.DateTimeField(default=datetime.now())


    class Meta:
        database = db
        db_table = 'products'
        order_by = ('created_at',)

    

db.connect()
# Category.create_table()
# Product.create_table()


'''================migrate изменяет поля '''


# from playhouse.migrate import migrate, PostgresqlMigrator
# migrator = PostgresqlMigrator(db)
# migrate(
#     migrator.alter_column_type('products', 'title', peewee.TextField())
# )
# ORM (object-relational mapping)-  технология прогармирование  благодаря который разработчики могут использвоать язык програмированние для взоимодействие с реалицонной базой данных (PostgreSQL, MySQL, OracleDB).OSError
# Вместо того чтобы писать сырые запросы на оперделленых SQL,  вы будете писать код ООП на языке программирование . Это очень сильно ускоряет разработку приложение и бд, особенно на начальных.

from peewee import PostgresqlDatabase
db = PostgresqlDatabase(
    database='orm_db',
    user='user',
    password='1',
    host ='localhost',
    port =5432
)

# db.connect() 
import psycopg
import config

# коннект к удаленной бд по конфигу
connection = psycopg.connect(
    host = config.HOST,
    dbname = config.DATABASE,
    user = config.USER,
    password = config.PASSWORD,
    port = config.PORT
)

# создание таблиц в бд по запросам
def create_table(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()



# запросы на создание таблиц
query_partners_import = '''
    create table partners_import (
    partner_type nchar(3) not null,
    partner_name nchar(100) PRIMARY KEY not null,
    partner_dir nchar(100) not null,
    partner_mail nchar(100) not null,
    partner_phone nchar(13) not null,
    partner_addr nchar(300) not null,
    partner_inn nchar(10) not null,
    partner_rate nchar(2) not null
    )
    '''

query_partner_products_import = '''
    create table partner_products_import (
    product_name_fk nchar(300) not null,
    FOREIGN KEY (product_name_fk) REFERENCES products_import(product_name) ON UPDATE CASCADE,
    
    partner_name_fk nchar(100) not null,
    FOREIGN KEY (partner_name_fk) REFERENCES partners_import(partner_name) ON UPDATE CASCADE,
    
    product_count int not null,
    sale_date date not null
    )
    '''

query_material_type_import = '''
    create table material_type_import (
    material_type nchar(50) PRIMARY KEY not null,
    material_broke_percent nchar(5) not null
    )
    '''

query_products_import = '''
    create table products_import (
    product_type_fk nchar(50) not null,
    FOREIGN KEY (product_type_fk) REFERENCES product_type_import(product_type) ON UPDATE CASCADE,
    product_name nchar(300) PRIMARY KEY not null,
    product_article bigint not null,
    product_min_cost real not null
    )
    '''

query_product_type_import = '''
    create table product_type_import (
    product_type nchar(50) PRIMARY KEY not null,
    product_coefficient_type real not null
    )
    '''


# вызовы функции для создания таблиц
create_table(connection, query_partners_import)
create_table(connection, query_product_type_import)
create_table(connection, query_products_import)
create_table(connection, query_material_type_import )
create_table(connection, query_partner_products_import)
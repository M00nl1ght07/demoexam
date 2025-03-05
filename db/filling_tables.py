import psycopg
import pandas as pd
import openpyxl
import config


def import_partners_import(connection):
    query = '''
    INSERT INTO partners_import
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    data_frame = pd.read_excel('excel/Partners_import.xlsx', engine='openpyxl')
    cursor = connection.cursor()
    for excel_row in data_frame.itertuples():
        p_type = excel_row._1
        name = excel_row._2
        director = excel_row.Директор
        mail = excel_row._4
        phone = excel_row._5
        addr = excel_row._6
        inn = excel_row.ИНН
        rate = excel_row.Рейтинг

        values = (p_type, name, director, mail, phone, addr, inn, rate)

        cursor.execute(query, values)

    # Сохранение изменений а БД
    connection.commit()
    cursor.close()


def import_product_type_import(connection):
    # Создание запроса на добавление
    query = '''
    INSERT INTO product_type_import
    VALUES (%s, %s)
    '''
    # Создание датафрейма
    data_frame = pd.read_excel('excel/Product_type_import.xlsx', engine='openpyxl')
    # Создание курсора, для запуска скрипта
    cursor = connection.cursor()
    # Итерируем датафрейм, превращая его строки в кортежи
    for excel_row in data_frame.itertuples():
        print(excel_row)
        p_type = excel_row._1
        coef = excel_row._2

        # Создание кортежа с переменными
        values = (p_type, coef)
        # Исполняем запрос и передаем в %s соответствующие переменные из values
        cursor.execute(query, values)

    # Сохранение изменений а БД
    connection.commit()
    cursor.close()


def import_material_type_import(connection):
    # Создание запроса на добавление
    query = '''
    INSERT INTO material_type_import
    VALUES (%s, %s)
    '''
    # Создание датафрейма
    data_frame = pd.read_excel('excel/Material_type_import.xlsx',
                               engine='openpyxl')
    # Создание курсора, для запуска скрипта
    cursor = connection.cursor()
    # Итерируем датафрейм, превращая его строки в кортежи
    for excel_row in data_frame.itertuples():
        print(excel_row)
        m_type = excel_row._1
        percent = f"{round(excel_row._2 * 100, 2)}%"

        # Создание кортежа с переменными
        values = (m_type, percent)
        # Исполняем запрос и передаем в %s соответствующие переменные из values
        cursor.execute(query, values)

    # Сохранение изменений а БД
    connection.commit()
    cursor.close()


def import_products_import(connection):
    # Создание запроса на добавление
    query = '''
    INSERT INTO products_import
    VALUES (%s, %s, %s, %s)
    '''
    # Создание датафрейма
    data_frame = pd.read_excel('excel/Products_import.xlsx', engine='openpyxl')
    # Создание курсора, для запуска скрипта
    cursor = connection.cursor()
    # Итерируем датафрейм, превращая его строки в кортежи
    for excel_row in data_frame.itertuples():
        print(excel_row)
        p_type = excel_row._1
        name = excel_row._2
        article = excel_row.Артикул
        cost = excel_row._4

        # Создание кортежа с переменными
        values = (p_type, name, article, cost)
        # Исполняем запрос и передаем в %s соответствующие переменные из values
        cursor.execute(query, values)

    # Сохранение изменений а БД
    connection.commit()
    cursor.close()


def import_partner_products_import(connection):
    # Создание запроса на добавление
    query = '''
    INSERT INTO partner_products_import
    VALUES (%s, %s, %s, %s)
    '''
    # Создание датафрейма
    data_frame = pd.read_excel('excel/Partner_products_import.xlsx',
                               engine='openpyxl')
    # Создание курсора, для запуска скрипта
    cursor = connection.cursor()
    # Итерируем датафрейм, превращая его строки в кортежи
    for excel_row in data_frame.itertuples():
        print(excel_row)
        name_prod = excel_row.Продукция
        name_part = excel_row._2

        count_p = excel_row._3
        date = excel_row._4

        # Создание кортежа с переменными
        values = (name_prod, name_part, count_p, date)
        # Исполняем запрос и передаем в %s соответствующие переменные из values
        cursor.execute(query, values)

    # Сохранение изменений а БД
    connection.commit()
    cursor.close()


connection_uri = psycopg.connect(
        user=config.USER,
        host=config.HOST,
        password=config.PASSWORD,
        dbname=config.DATABASE
)

import_partners_import(connection_uri)
import_product_type_import(connection_uri)
import_material_type_import(connection_uri)
import_products_import(connection_uri)
import_partner_products_import(connection_uri)

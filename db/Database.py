import psycopg
from . import config  # Используем точку для импорта из текущего пакета

class Database():
    def __init__(self):
        # переменная для хранения строки подключения к БД
        self.connection_uri = self.connect_to_db()
    # функция подкллючения к БД по данным из config.py
    def connect_to_db(self):
        try:
            print('Подключение к БД....')
            connection = psycopg.connect(
                user=config.USER,
                host=config.HOST,
                password=config.PASSWORD,
                dbname=config.DATABASE
            )
            print('БД Подключена')
            # возвращение в переменную self.connection_uri значения переменной connection
            return connection
        
        # обработка ошибок
        except Exception as error:  
            print(f':: {error}')
            return None

    # функция получения всей информации о Партнерах, для создания карточек
    def take_all_partners_info(self):
        try:
            query = '''
            SELECT *
            FROM partners_import;
            '''
            # создание курсора для взаимодействия с БД
            cursor = self.connection_uri.cursor()
            # исполнение запроса
            cursor.execute(query)

            # создание массива для хранения результатов
            partners_data = []
            # перебор ответа из Базы данных
            for return_row in cursor.fetchall():
                # добавление данных в словарь
                partners_data.append(
                    {
                        'type': return_row[0].strip(),
                        'name': return_row[1].strip(),
                        'dir': return_row[2].strip(),
                        'mail': return_row[3].strip(),
                        'phone': return_row[4].strip(),
                        'addr': return_row[5].strip(),
                        'inn': return_row[6].strip(),
                        'rate': return_row[7].strip()
                    }
                )
            # возврат данных
            return partners_data
        except Exception as error:
            print(error)
            # при ошибке возвращается пустой список
            return []
    # функция получения числа продаж для конкретного партнера
    def take_count_of_sales(self, partner_name: str):
        try:
            query = f'''
            SELECT SUM(product_count)
            FROM partner_products_import
            WHERE partner_name_fk = '{partner_name}';
            '''
            # создание курсора для взаимодействия с БД
            cursor = self.connection_uri.cursor()
            # исполнение запроса
            cursor.execute(query)
            # запись значения в переменную
            count = cursor.fetchone()
            # закрытие курсора
            cursor.close()
            # проверка наличия ответа на запрос
            if count:
                return count[0]
            return None
        except Exception as error:
            print(error)
            return None
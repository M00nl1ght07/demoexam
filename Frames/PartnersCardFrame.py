from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QScrollArea, 
    QLabel,  
    QPushButton, 
    QHBoxLayout,  
    QFrame  

)
from PySide6.QtGui import QPixmap
from db import Database

class PartnerCardsClass(QFrame):
    def __init__(self, main_class_controller): 
        super().__init__()
        self.controller = main_class_controller
        self.db: Database.Database = main_class_controller.db

        self.main_frame_layout = QVBoxLayout(self)
        self.setup_ui()
    
    # установка интерфейса
    def setup_ui(self):
        # создание текстового поля
        title_label = QLabel("Партнеры")
        # назначение объектного имени для стилизации объекта
        title_label.setObjectName("Title")
        # добавление поля на фрейм
        self.main_frame_layout.addWidget(title_label)

        # добавление фотографии на экран
        self.add_picture()

        # создание области прокрутки
        scroll_area = QScrollArea()
        # объекты внутри области прокрутки будут подстраивать свой размер под размер области
        scroll_area.setWidgetResizable(True)
        # установка контейнера с карточками в область прокрутки scroll_area
        scroll_area.setWidget(self.create_partners_cards())

        # добавление области прокрутки в разметку фрейма
        self.main_frame_layout.addWidget(scroll_area)

    # функция добавления фотографии
    def add_picture(self):
        # создание области, которая будет хранить фото
        picture_place = QLabel()
        # создание инструмента для считывания фото из файловой системы
        picture_read = QPixmap('/Icons/icon.png')

        # объекты внутри QLabel будут размером как сам QLabel
        picture_place.setScaledContents(True)
        # установка размеров для QLabel
        picture_place.setFixedSize(52, 52)
        # добавление фото в QLabel
        picture_place.setPixmap(picture_read)

        # добавление фото на экран
        self.main_frame_layout.addWidget(picture_place)
    # функция расчета скидки партнера
    def calculate_discount(self, partner_name: str):
        # получение суммы продаж
        count = self.db.take_count_of_sales(partner_name)
        # проверка по зданию
        if count == None:
            return 0
        elif count > 300_000:
            return 15
        elif count > 50_000:
            return 10
        elif count > 10000:
            return 5
        return 0
    # функция карточек партнеров
    def create_partners_cards(self):
        # создание контейнера для карточек
        cards_container = QWidget()
        # назначение разметки для контейнера, чтобы карточки были вертикально расположены
        cards_container_layout = QVBoxLayout(cards_container)

        # Генерация карточек
        for partner_information in self.db.take_all_partners_info():
            # создание карточки
            card = QWidget()
            # назначение объектного имени для дизайна
            card.setObjectName(f"Card")

            # создание разметки для карточки, чтобы текст размещался вертикально
            card_layout = QVBoxLayout()
            card.setLayout(card_layout)

            # создание горизонтальной разметки
            card_top_level_hbox = QHBoxLayout()
            # создание текстового поля с Типом и Именем партнера
            partner_type_label = QLabel(f'{partner_information["type"]} | {partner_information["name"]}')
            partner_type_label.setStyleSheet('QLabel {font-size: 18px}')

            partner_discount_label = QLabel(f'{self.calculate_discount(partner_information["name"])}%')
            # назначение стиля для поля
            partner_discount_label.setStyleSheet('QLabel {qproperty-alignment: AlignRight; font-size: 18px}')

            # добавление полей в горизонтальную разметку
            card_top_level_hbox.addWidget(partner_type_label)
            card_top_level_hbox.addWidget(partner_discount_label)

            # добавление горизонтальной разметки в карточку
            card_layout.addLayout(card_top_level_hbox)

            # создание текстовых полей
            dir_label = QLabel(f"{partner_information['dir']}")
            # назначение объектного имени для Дизайна
            dir_label.setObjectName("Card_label")

            phone_label = QLabel(f"+7 {partner_information['phone']}")
            phone_label.setObjectName("Card_label")

            rate_label = QLabel(f"Рейтинг: {partner_information['rate']}")
            rate_label.setObjectName("Card_label")

            card_layout.addWidget(dir_label)
            card_layout.addWidget(phone_label)
            card_layout.addWidget(rate_label)

            # добавление карточки в разметку
            cards_container_layout.addWidget(card)

        # возвращение контейнера в то место, где вызывают функцию
        return cards_container
from PySide6.QtWidgets import (
    QWidget,  
    QStackedWidget,  
    QVBoxLayout,  
    QApplication 
)
import sys
from Frames import PartnersCardFrame
from db import Database

class MainApplicationClass(QWidget):
    # Конструктор класса MainApplication
    def __init__(self):
        # Вызов Родительского класса
        super().__init__()

        # установка заголовка приложения
        self.setWindowTitle("Мастер Пол")
        # установка стартовых размеров приложения
        self.resize(1024, 768)

        # вызов класса Database()
        self.db = Database.Database()

        # создание контейнера для фреймов
        self.frames_container = QStackedWidget()

        # вызов класса первого фрейма
        partner_cards_frame = PartnersCardFrame.PartnerCardsClass(self)

        # добавление класса фрейма в контейнер фреймов
        self.frames_container.addWidget(partner_cards_frame)

        # создание разметки для класса MainApplicationClass, которая будет размещать фреймы из self.frame_container
        layout = QVBoxLayout(self)

        # добавление контейнера с фреймами в разметку
        layout.addWidget(self.frames_container) 
        
# стили приложения
styles_sheet = '''
QPushButton {
background: #67BA80;
color: #000000;
}

QLineEdit {
font-size: 15px;
}


#Title {
font-size: 20px;
qproperty-alignment: AlignCenter;
}

#Hint_label {
font-size: 18px;
padding: 10px, 0px, 0px, 0px;
font-weight: bold;
}

#Main_label {
font-size: 15px;
}

#Card_label {
font-size: 15px;
}

#Card {
border: 2px solid black;
}

#Top_lvl_label {
font-size: 30px;
}

'''

# регистрация приложения в системе
application = QApplication(sys.argv)
# подключение стилей приложения
application.setStyleSheet(styles_sheet)
# установка шрифта
application.setFont('Segoe UI')
# вызов класса MainApplicationClass
main_class_object = MainApplicationClass()
# визуализация класса
main_class_object.show()
# запуск приложения в системе
application.exec()

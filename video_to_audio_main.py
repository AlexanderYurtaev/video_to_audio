from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from funcs import video_to_audio


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Video to Audio Converter')
        self.setGeometry(900, 500, 900, 500)

        # глaвный label
        self.label_main = QtWidgets.QLabel(self)
        self.label_main.setText('Video to Audio Converter')
        self.label_main.setGeometry(280, 10, 340, 40)
        self.label_main.setFont(QFont('Arial', 30))

        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(0, 69, 900, 261)

        # конфигурим tab1
        self.tab_1 = QtWidgets.QWidget()

        self.label_hint_tab_1 = QtWidgets.QLabel(self.tab_1)
        self.label_hint_tab_1.setText('Введите путь до файла или адрес видео в ютубе:')
        self.label_hint_tab_1.setGeometry(50, 30, 470, 15)

        self.input_filed_tab_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.input_filed_tab_1.setGeometry(50, 50, 540, 50)
        self.input_filed_tab_1.setPlaceholderText(
            '/Users/aleksandr/Downloads/Архив с ютуба/DevOps Quality Metrics that Matter_ Forrester Research on 75 '
            'Common Metrics.mp4')

        self.button_begin_tab_1 = QtWidgets.QPushButton(self.tab_1)
        self.button_begin_tab_1.setGeometry(290, 180, 261, 41)
        self.button_begin_tab_1.setText('Начать')
        self.button_begin_tab_1.clicked.connect(self.begin_convert_video_to_mp3)

        self.tab_widget.addTab(self.tab_1, 'Видео в mp3')

        # конфигурим tab 2
        self.tab_2 = QtWidgets.QWidget()

        self.label_hint_tab_2 = QtWidgets.QLabel(self.tab_2)
        self.label_hint_tab_2.setText('Введите путь до файла:')
        self.label_hint_tab_2.setGeometry(50, 30, 470, 15)

        self.input_filed_tab_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.input_filed_tab_2.setGeometry(50, 50, 540, 50)
        self.input_filed_tab_2.setPlaceholderText(
            '/Users/aleksandr/Downloads/Архив с ютуба/DevOps Quality Metrics that Matter_ Forrester Research on 75 '
            'Common Metrics.mp4')

        self.button_begin_tab_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_begin_tab_2.setGeometry(290, 180, 261, 41)
        self.button_begin_tab_2.setText('Начать')

        self.tab_widget.addTab(self.tab_2, 'Обрезать mp3')

        # label результат
        self.text_result = ''
        self.label_result = QtWidgets.QLabel(self)
        # self.label_result.setText('Что-то пошло не так !')
        self.label_result.setText(self.text_result)
        self.label_result.setGeometry(280, 370, 311, 41)
        self.label_result.setFont(QFont('Arial', 20))
        self.label_result.setAlignment(Qt.AlignCenter)
        # self.label_result.setStyleSheet("QLabel {background-color: red;}")

        # label путь куда сохранен файл
        # self.text_saved_path = 'Фоайл сохранен по адресу:\n/Users/aleksandr/sdfsd/sdfsdfsdf/sdfsdfsdf/sdfsdfDownloads/Архив с ютуба/DevOps Quality Metrics that Matter_ Forrester Research on 75 Common Metrics.mp4'
        self.text_saved_path = ''
        self.label_result_details = QtWidgets.QLabel(self)
        self.label_result_details.setText(self.text_saved_path)
        self.label_result_details.setGeometry(60, 400, 731, 91)
        # self.label_result_details.adjustSize()
        self.label_result_details.setWordWrap(True)

    # def take_adrress_from_input_filed(self, input_field) -> str:
    #     path = self.input_filed_tab_1.toPlainText()
    #     print('path')
    #     return path


    def begin_convert_video_to_mp3(self):
        video_location = self.input_filed_tab_1.toPlainText()
        print(video_location)
        video_to_audio(video_location)

    def begin_cut_file(self):
        pass


def start_application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_application()

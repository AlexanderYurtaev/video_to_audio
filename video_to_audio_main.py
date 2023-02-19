from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from funcs import video_to_audio, download_from_youtube


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

        # label результат
        self.label_result = QtWidgets.QLabel(self)
        self.label_result.setText('')
        self.label_result.setGeometry(280, 360, 311, 41)
        self.label_result.setFont(QFont('Arial', 20, QFont.Bold))
        self.label_result.setAlignment(Qt.AlignCenter)

        # label путь куда сохранен файл
        self.label_result_details = QtWidgets.QLabel(self)
        self.label_result_details.setText('')
        self.label_result_details.setGeometry(0, 400, 900, 100)
        self.label_result_details.setStyleSheet('background-color: rgb(233, 176, 99);padding :15px')
        self.label_result_details.setWordWrap(True)


        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(0, 69, 900, 261)
        self.tab_widget.currentChanged.connect(self.print_active_tab_index)

        # конфигурим tab1
        self.tab_1 = QtWidgets.QWidget()

        self.label_hint_tab_1 = QtWidgets.QLabel(self.tab_1)
        self.label_hint_tab_1.setText('Введите путь до файла или адрес видео в ютубе:')
        self.label_hint_tab_1.setGeometry(50, 30, 470, 15)

        self.input_filed_tab_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.input_filed_tab_1.setGeometry(50, 50, 790, 50)
        self.input_filed_tab_1.setPlaceholderText(
            '/Users/aleksandr/Downloads/Архив с ютуба/DevOps Quality Metrics that Matter_ Forrester Research on 75 '
            'Common Metrics.mp4')

        self.button_begin_tab_1 = QtWidgets.QPushButton(self.tab_1)
        self.button_begin_tab_1.setGeometry(290, 180, 261, 41)
        self.button_begin_tab_1.setText('Начать')
        self.button_begin_tab_1.clicked.connect(self.begin_convert_video_to_mp3)

        self.label_cut_file = QtWidgets.QLabel(self.tab_1)
        self.label_hint_tab_1.setText('Редактировать начало и конец:')
        self.label_hint_tab_1.setGeometry(50, 110, 210, 15)

        self.input_start_tab_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.input_start_tab_1.setGeometry(50, 130, 70, 23)
        self.input_start_tab_1.setPlaceholderText('00:00:00')

        self.input_end_tab_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.input_end_tab_1.setGeometry(130, 130, 70, 23)
        self.input_end_tab_1.setPlaceholderText('02:30:20')

        self.tab_widget.addTab(self.tab_1, 'Видео в mp3')

        # конфигурим tab 2
        self.tab_2 = QtWidgets.QWidget()

        self.label_hint_tab_2 = QtWidgets.QLabel(self.tab_2)
        self.label_hint_tab_2.setText('Введите путь до файла:')
        self.label_hint_tab_2.setGeometry(50, 30, 470, 15)

        self.input_filed_tab_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.input_filed_tab_2.setGeometry(50, 50, 790, 50)
        self.input_filed_tab_2.setPlaceholderText(
            '/Users/aleksandr/Downloads/Архив с ютуба/DevOps Quality Metrics that Matter_ Forrester Research on 75 '
            'Common Metrics.mp4')

        self.button_begin_tab_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_begin_tab_2.setGeometry(290, 180, 261, 41)
        self.button_begin_tab_2.setText('Начать')
        self.button_begin_tab_2.clicked.connect(self.begin_cut_mp3)

        self.tab_widget.addTab(self.tab_2, 'Обрезать mp3')

        # конфигурим tab 3
        self.tab_3 = QtWidgets.QWidget()

        self.label_hint_tab_3 = QtWidgets.QLabel(self.tab_3)
        self.label_hint_tab_3.setText('Введите адрес видео в youtube:')
        self.label_hint_tab_3.setGeometry(50, 30, 470, 15)

        self.input_filed_tab_3 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.input_filed_tab_3.setGeometry(50, 50, 790, 50)
        self.input_filed_tab_3.setPlaceholderText('https://www.youtube.com/watch?v=lUZUsRLAoN4')

        self.button_begin_tab_3 = QtWidgets.QPushButton(self.tab_3)
        self.button_begin_tab_3.setGeometry(290, 180, 261, 41)
        self.button_begin_tab_3.setText('Начать')
        self.button_begin_tab_3.clicked.connect(self.begin_dowload_video)

        self.tab_widget.addTab(self.tab_3, 'Скачать видео')


    def begin_convert_video_to_mp3(self):
        # обнуление контента лейблов чет не работает. разобраться
        # self.label_result.clear()
        # self.label_result_details.clear()
        start_time = self.input_start_tab_1.toPlainText()

        try:
            video_location = self.input_filed_tab_1.toPlainText()
            saved_file_path = video_to_audio(video_location)
            self.label_result.setText('УСПЕШНО')
            self.label_result.setStyleSheet('color: green')
            self.label_result_details.setText(f'Файл сохранен:\n{saved_file_path}')
        except ValueError as ex:
            self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
            self.label_result.setStyleSheet('color: red')
            self.label_result_details.setText(
                f'You should enter correct address of the file before push the button Begin !')

    def begin_cut_mp3(self):
        try:
            file_location = self.input_filed_tab_2.toPlainText()
            saved_file_path = download_from_youtube(file_location)
            self.label_result.setText('УСПЕШНО')
            self.label_result.setStyleSheet('color: green')
            self.label_result_details.setText(f'Файл сохранен в разрешении 720p:\n{saved_file_path}')
        except Exception as ex:
            self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
            self.label_result.setStyleSheet('color: red')
            self.label_result_details.setText(
                f'You should enter correct address of the video before push the button Begin !')

    def begin_dowload_video(self):
        try:
            video_location = self.input_filed_tab_3.toPlainText()
            saved_file_path = download_from_youtube(video_location)
            self.label_result.setText('УСПЕШНО')
            self.label_result.setStyleSheet('color: green')
            self.label_result_details.setText(f'Файл сохранен в:\n{saved_file_path}')
        except Exception as ex:
            self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
            self.label_result.setStyleSheet('color: red')
            self.label_result_details.setText(
                f'You should enter correct address of the video before push the button Begin !')


    def begin_cut_file(self):
        pass

    def print_active_tab_index(self):
        current_tab_index = self.tab_widget.currentIndex()
        print(current_tab_index)
        self.label_result.clear()
        self.label_result_details.clear()


def start_application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_application()

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from funcs import video_to_audio, download_video_from_youtube, cut_audio_file


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

        self.checkbox_crop_tab_1 = QtWidgets.QCheckBox(self.tab_1)
        self.checkbox_crop_tab_1.setText('Редактировать время начала и конца')
        self.checkbox_crop_tab_1.setGeometry(50, 110, 260, 15)
        self.checkbox_crop_tab_1.stateChanged.connect(self.do_check_crop_tab2)

        self.input_start_tab_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.input_start_tab_1.setGeometry(70, 130, 70, 23)
        self.input_start_tab_1.setPlaceholderText('00:00:00')
        self.input_start_tab_1.hide()

        self.input_end_tab_1 = QtWidgets.QPlainTextEdit(self.tab_1)
        self.input_end_tab_1.setGeometry(150, 130, 70, 23)
        self.input_end_tab_1.setPlaceholderText('02:30:20')
        self.input_end_tab_1.hide()

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
            'Common Metrics.mp3')

        self.button_begin_tab_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_begin_tab_2.setGeometry(290, 180, 261, 41)
        self.button_begin_tab_2.setText('Начать')
        self.button_begin_tab_2.clicked.connect(self.begin_cut_mp3)

        # чекбокс и поля для обрезания файла
        self.checkbox_crop_tab_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkbox_crop_tab_2.setText('Редактировать время начала и конца')
        self.checkbox_crop_tab_2.setGeometry(50, 110, 260, 15)
        self.checkbox_crop_tab_2.stateChanged.connect(self.do_check_crop_tab2)

        self.input_start_tab_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.input_start_tab_2.setGeometry(70, 130, 70, 23)
        self.input_start_tab_2.setPlaceholderText('00:00:00')
        self.input_start_tab_2.hide()

        self.input_end_tab_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.input_end_tab_2.setGeometry(150, 130, 70, 23)
        self.input_end_tab_2.setPlaceholderText('02:30:20')
        self.input_end_tab_2.hide()

        # чекбокс для вырезания из файла
        self.checkbox_cut_tab_2 = QtWidgets.QCheckBox(self.tab_2)
        # hide until fixed bug https://github.com/Zulko/moviepy/pull/1757
        self.checkbox_cut_tab_2.hide()
        self.checkbox_cut_tab_2.setText('Вырезать участок')
        self.checkbox_cut_tab_2.setGeometry(350, 110, 260, 15)
        self.checkbox_cut_tab_2.stateChanged.connect(self.do_check_cut_tab2)

        self.input_start_cut_tab_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.input_start_cut_tab_2.setGeometry(370, 130, 70, 23)
        self.input_start_cut_tab_2.setPlaceholderText('00:31:20')
        self.input_start_cut_tab_2.hide()

        self.input_end_cut_tab_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.input_end_cut_tab_2.setGeometry(450, 130, 70, 23)
        self.input_end_cut_tab_2.setPlaceholderText('01:30:11')
        self.input_end_cut_tab_2.hide()

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
        end_time = self.input_end_tab_1.toPlainText()

        try:
            video_location = self.input_filed_tab_1.toPlainText()
            if start_time != '' and end_time == '':
                saved_file_path = video_to_audio(video_location, cut_start=start_time)
            elif start_time == '' and end_time != '':
                saved_file_path = video_to_audio(video_location, cut_end=end_time)
            # TO DO
            # elif start_time < end_time or start_time == end_time:
            #     raise Exception
            else:
                saved_file_path = video_to_audio(video_location, start_time, end_time)

            self.label_result.setText('УСПЕШНО')
            self.label_result.setStyleSheet('color: green')
            self.label_result_details.setText(f'Файл сохранен:\n{saved_file_path}')
        except ValueError as ex:
            self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
            self.label_result.setStyleSheet('color: red')
            self.label_result_details.setText(
                f'You should enter correct address of the file before push the button Begin !')

    def begin_cut_mp3(self):
        if self.checkbox_cut_tab_2.isChecked() and self.checkbox_crop_tab_2.isChecked():
            self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
            self.label_result.setStyleSheet('color: red')
            self.label_result_details.setText(
                f'Выберите только один вариант модификации аудио файла !')
            return

        if self.checkbox_crop_tab_2.isChecked():
            print('here0')
            start_time = self.input_start_tab_2.toPlainText()
            end_time = self.input_end_tab_2.toPlainText()
            mode = 'crop'
            if start_time == '' and end_time == '':
                self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
                self.label_result.setStyleSheet('color: red')
                self.label_result_details.setText(f'Enter start time or/and end time.')
        elif self.checkbox_cut_tab_2.isChecked():
            start_time = self.input_start_cut_tab_2.toPlainText()
            end_time = self.input_end_cut_tab_2.toPlainText()
            mode = 'cut'
            if start_time == '' or end_time == '':
                self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
                self.label_result.setStyleSheet('color: red')
                self.label_result_details.setText(
                    f'В режиме "Вырезать участок" должно быть указано и время начала и время конца.')
                return print('here')

        audio_location = self.input_filed_tab_2.toPlainText()

        try:
            saved_file_path = cut_audio_file(audio_location, start_time, end_time, mode)
            self.label_result.setText('УСПЕШНО')
            self.label_result.setStyleSheet('color: green')
            self.label_result_details.setText(f'Файл сохранен:\n{saved_file_path}')
        except Exception as ex:
            self.label_result.setText('ЧТО-ТО ПОШЛО НЕ ТАК !')
            self.label_result.setStyleSheet('color: red')
            self.label_result_details.setText(
                f'You should enter correct address of the video before push the button Begin !')
            print(ex)

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

    def print_active_tab_index(self):
        self.label_result.clear()
        self.label_result_details.clear()

    # function which check if check box cut start/end is checked
    def do_check_crop_tab2(self):
        match self.tab_widget.currentIndex():
            case 0:
                if self.checkbox_crop_tab_1.isChecked():
                    self.input_start_tab_1.show()
                    self.input_end_tab_1.show()
                else:
                    self.input_start_tab_1.hide()
                    self.input_end_tab_1.hide()
            case 1:
                # if self.checkbox_cut_tab_2.isChecked():
                # self.checkbox_cut_tab_2.setCheckState(0)
                if self.checkbox_crop_tab_2.isChecked():
                    self.input_start_tab_2.show()
                    self.input_end_tab_2.show()
                else:
                    self.input_start_tab_2.hide()
                    self.input_end_tab_2.hide()

    def do_check_cut_tab2(self):
        # if self.checkbox_crop_tab_2.isChecked():
        #     self.checkbox_crop_tab_2.setCheckState(0)
        if self.checkbox_cut_tab_2.isChecked():
            self.input_start_cut_tab_2.show()
            self.input_end_cut_tab_2.show()
        else:
            self.input_start_cut_tab_2.hide()
            self.input_end_cut_tab_2.hide()


def start_application():
    import funcs
    import utils
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_application()

import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog

from five_numbers import Ui_five_number
from show_numbers import Ui_numbers_2


class Game(QMainWindow):
    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.ui = Ui_five_number()
        self.ui.setupUi(self)

        self.ui.answer.clicked.connect(self.test)
        self.ui.start.clicked.connect(self.test_start)

    def test(self):
        text = self.ui.writing_numbers.toPlainText()
        if text == "":
            text = "y"
        self.ui.information.setPlainText(text)

    def test_start(self):
        dialog = Dialog(self)  # Создаем экземпляр диалогового окна
        dialog.ui.numbers.setPlainText("Hello")  # Устанавливаем текст
        dialog.exec()  # Показываем диалоговое окно


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_numbers_2()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)  # Таймер сработает только один раз
        self.timer.timeout.connect(self.close)  # Закрыть окно по истечении времени
        self.timer.start(3000)  # Установить таймер на 3000 миллисекунд (3 секунды)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Game()
    window.show()

    sys.exit(app.exec())

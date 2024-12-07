import random
import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QWidget

from game import Ui_game
from show_numbers import Ui_numbers_2
from menu import Ui_menu


class Game(QMainWindow):
    def __init__(self, parent=None):
        super(Game, self).__init__(parent)

        self.counter = None
        self.dialog = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.ui = Ui_game()
        self.ui.setupUi(self)

        self.set_numbers = []

        self.number_of_numbers = 0

        self.ui.answer.clicked.connect(self.checking_the_response)
        self.ui.start.clicked.connect(self.show_numbers)
        self.ui.Exit.clicked.connect(self.close_game)

    def checking_the_response(self):
        text = self.ui.writing_numbers.toPlainText().strip()  # Убираем лишние пробелы
        if text:  # Проверяем, что строка не пустая
            try:
                # Преобразуем строку в список целых чисел
                user_numbers = list(map(int, text.split()))
            except ValueError:
                self.ui.information.setPlainText("Вы ввели некорректные значения")
                return

            numbers_string = ', '.join(map(str, self.set_numbers))
            counter_true = 0

            # Преобразуем self.set_numbers в множество для быстрого поиска
            if self.set_numbers:
                for number in user_numbers:
                    if number in self.set_numbers:
                        counter_true += 1

                if len(user_numbers) > len(self.set_numbers):
                    self.ui.information.setPlainText(
                        f"{numbers_string}. Вы запомнили {counter_true} из {len(self.set_numbers)} чисел, но добавили лишние значения."
                    )
                else:
                    self.ui.information.setPlainText(
                        f"{numbers_string}. Вы запомнили {counter_true} из {len(self.set_numbers)} чисел."
                    )
            else:
                self.ui.information.setPlainText("Чтобы начать, тренировку нажмите кнопку Начать")

        else:
            self.ui.information.setPlainText("Вы ввели некорректные значения")

    def show_numbers(self):
        self.generate_numbers()
        numbers_string = ', '.join(map(str, self.set_numbers))
        self.dialog = Dialog(self)
        self.dialog.ui.numbers.setPlainText(str(numbers_string))  # Устанавливаем текст

        self.counter = 1  # Счетчик времени

        self.timer.start(1000)
        self.dialog.finished.connect(self.show)
        self.dialog.exec()  # Показываем диалоговое окно

    def update_timer(self):
        self.dialog.ui.time.setPlainText(f"{self.counter}")
        self.counter += 1

    def generate_numbers(self):
        self.set_numbers = [random.randint(0, 99) for _ in range(self.number_of_numbers)]

    def close_game(self):
        self.hide()
        if self.parent():  # Проверяем, есть ли родитель (Menu)
            self.parent().show()  # Показываем главное меню


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_numbers_2()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)  # Закрыть окно по истечении времени
        self.timer.start(10000)  # Установить таймер на 10000 миллисекунд (10 секунд)


class Menu(QMainWindow):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.game = None
        self.ui = Ui_menu()
        self.ui.setupUi(self)

        self.ui.five_numbers.clicked.connect(self.click_five)
        self.ui.ten_numbers.clicked.connect(self.click_ten)
        self.ui.fifteen_numbers.clicked.connect(self.click_fifteen)
        self.ui.exit.clicked.connect(self.close_menu)

    def click_five(self):
        self.hide()  # Скрыть главное окно
        self.game = Game(self)  # Создаем экземпляр игры
        self.game.number_of_numbers = 5  # Устанавливаем количество чисел

        # Открываем второе окно
        self.game.show()  # Показываем новое основное окно

    def click_ten(self):
        self.hide()  # Скрыть главное окно
        self.game = Game(self)  # Создаем экземпляр игры
        self.game.number_of_numbers = 10  # Устанавливаем количество чисел

        # Открываем второе окно
        self.game.show()  # Показываем новое основное окно

    def click_fifteen(self):
        self.hide()  # Скрыть главное окно
        self.game = Game(self)  # Создаем экземпляр игры
        self.game.number_of_numbers = 15  # Устанавливаем количество чисел

        # Открываем второе окно
        self.game.show()  # Показываем новое основное окно

    def close_menu(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Menu()
    window.show()

    sys.exit(app.exec())

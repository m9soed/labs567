import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtWidgets import QWizard, QLineEdit, QWizardPage, QCheckBox, QComboBox

class BlackTextWizard(QWizard):
    def __init__(self):
        super().__init__()

        self.addPage(LoginPage())
        self.addPage(PersonalInfoPage())
        self.addPage(InterestPage())

        self.setWindowTitle("Регистрация пользователя")

    def accept(self):
        print("Регистрация завершена.")
        # Получаем данные из мастера
        login = self.page(0).login_edit.text()
        password = self.page(0).password_edit.text()
        name = self.page(1).name_edit.text()
        interests = self.page(2).interests_combo.currentText()
        subscription = self.page(2).subscribe_checkbox.isChecked()

        # Выводим данные на главное окно программы
        result_label = QLabel(f"Логин: {login}\nПароль: {password}\nФИО: {name}\nИнтересы: {interests}\nПодписка: {subscription}")
        result_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_window.central_widget.layout().addWidget(result_label)
        super().accept()  # Вызываем оригинальный метод accept()

class LoginPage(QWizardPage):
    def __init__(self):
        super().__init__()

        self.setTitle("Логин и пароль")

        layout = QVBoxLayout()

        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Логин")
        layout.addWidget(self.login_edit)

        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Пароль")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_edit)

        self.setLayout(layout)

        # Устанавливаем стиль для всех элементов на странице
        self.setStyleSheet("""
            color: black;
        """)

    def validatePage(self):
        if not self.login_edit.text() or not self.password_edit.text():
            return False
        return True

class PersonalInfoPage(QWizardPage):
    def __init__(self):
        super().__init__()

        self.setTitle("ФИО")

        layout = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("ФИО")
        layout.addWidget(self.name_edit)

        self.setLayout(layout)

        # Устанавливаем стиль для всех элементов на странице
        self.setStyleSheet("""
            color: black;
        """)

    def validatePage(self):
        if not self.name_edit.text():
            return False
        return True

class InterestPage(QWizardPage):
    def __init__(self):
        super().__init__()

        self.setTitle("Темы, интересные пользователю")

        layout = QVBoxLayout()

        self.interests_combo = QComboBox()
        self.interests_combo.addItems(["Политика", "Наука", "Технологии", "Искусство"])
        layout.addWidget(self.interests_combo)

        self.subscribe_checkbox = QCheckBox("Согласен на рассылку")
        layout.addWidget(self.subscribe_checkbox)

        self.setLayout(layout)

        # Устанавливаем стиль для всех элементов на странице
        self.setStyleSheet("""
            color: black;
        """)

    def validatePage(self):
        return True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главное окно программы")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.start_registration_button = QPushButton("Начать регистрацию")
        self.start_registration_button.clicked.connect(self.start_registration)
        layout.addWidget(self.start_registration_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    @Slot()
    def start_registration(self):
        wizard = BlackTextWizard()
        wizard.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

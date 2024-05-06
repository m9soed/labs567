from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QLabel

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowTitle("Соглашение")
        self.checkbox = QCheckBox("Соглашаюсь")
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.resize(300, 300)
        self.label = QLabel("Нажмите кнопку, чтобы открыть диалог")
        self.button = QPushButton("Нажми меня")
        self.button.clicked.connect(self.show_dialog)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_dialog(self):
        dialog = Dialog(self)
        if dialog.exec():
            if dialog.checkbox.isChecked():
                QMessageBox.information(self, "Состояние чекбокса", "Выбран")
            else:
                QMessageBox.information(self, "Состояние чекбокса", "Не выбран")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
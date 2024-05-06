import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QLineEdit, QPushButton, QGridLayout

class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мое Приложение")
        self.setGeometry(100, 100, 600, 400)

        self.tab_widget = QTabWidget()

        self.setup_tab1()
        self.setup_tab2()

        self.setCentralWidget(self.tab_widget)

    def setup_tab1(self):
        self.tab1 = QWidget()
        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.weight_input = QLineEdit(self)
        self.quantity_input = QLineEdit(self)
        self.add_button = QPushButton("Добавить", self)
        self.add_button.clicked.connect(self.add_product)

        layout.addWidget(QLabel("Название продукта:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Вес продукта:"))
        layout.addWidget(self.weight_input)
        layout.addWidget(QLabel("Количество продукта:"))
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.add_button)

        self.tab1.setLayout(layout)
        self.tab_widget.addTab(self.tab1, "Добавить продукт")

    def setup_tab2(self):
        self.tab2 = QWidget()
        layout = QGridLayout()

        self.products = []

        layout.addWidget(QLabel("Название"), 0, 0)
        layout.addWidget(QLabel("Вес"), 0, 1)
        layout.addWidget(QLabel("Количество"), 0, 2)

        self.tab2.setLayout(layout)
        self.tab_widget.addTab(self.tab2, "Список продуктов")

    def add_product(self):
        name = self.name_input.text()
        weight = self.weight_input.text()
        quantity = self.quantity_input.text()

        self.products.append((name, weight, quantity))

        self.update_products_grid()

    def update_products_grid(self):
        layout = self.tab2.layout()

        for i, product in enumerate(self.products):
            name_label = QLabel(product[0])
            weight_label = QLabel(product[1])
            quantity_label = QLabel(product[2])

            layout.addWidget(name_label, i + 1, 0)
            layout.addWidget(weight_label, i + 1, 1)
            layout.addWidget(quantity_label, i + 1, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApplication()
    my_app.show()
    sys.exit(app.exec())

from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QDialog, QDialogButtonBox

import sys


class Note:
    def __init__(self, text="", date=None):
        self.text = text
        self.date = date if date is not None else QDate.currentDate()

    def __str__(self):
        return f"{self.date.toString('dd.MM.yyyy')} - {self.text}"


class NoteDialog(QDialog):
    def __init__(self, parent=None, note=None):
        super().__init__(parent)

        self.note = note

        self.setWindowTitle("Add note")

        self.text_edit = QLineEdit()
        self.date_edit = QLineEdit()
        self.date_edit.setInputMask("99.99.9999")
        self.date_edit.setFixedWidth(80)

        if self.note:
            self.text_edit.setText(self.note.text)
            self.date_edit.setText(self.note.date.toString("dd.MM.yyyy"))

        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Text"))
        form_layout.addWidget(self.text_edit)
        form_layout.addWidget(QLabel("Date"))
        form_layout.addWidget(self.date_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def accept(self):
        text = self.text_edit.text().strip()
        date_text = self.date_edit.text().strip()
        if text and date_text:
            try:
                date = QDate.fromString(date_text, "dd.MM.yyyy")
            except ValueError:
                self.date_edit.setFocus()
                return
            self.note = Note(text, date)
            super().accept()
        else:
            if not text:
                self.text_edit.setFocus()
            else:
                self.date_edit.setFocus()


class NotesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.notes = []

        self.create_widgets()
        self.create_layout()

        self.setWindowTitle("Notes")
        self.setMinimumSize(600, 400)

    def create_widgets(self):
        self.notes_list_widget = QListWidget()

        self.new_note_button = QPushButton("New")
        self.new_note_button.clicked.connect(self.show_new_note_dialog)

        self.edit_note_button = QPushButton("Edit")
        self.edit_note_button.clicked.connect(self.edit_selected_note)

        self.delete_note_button = QPushButton("Delete")
        self.delete_note_button.clicked.connect(self.delete_selected_note)

    def create_layout(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_note_button)
        button_layout.addWidget(self.edit_note_button)
        button_layout.addWidget(self.delete_note_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.notes_list_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_new_note_dialog(self):
        dialog = NoteDialog(self)
        if dialog.exec() == QDialog.Accepted:
            note = dialog.note
            item = QListWidgetItem(str(note))
            item.setData(Qt.UserRole, note)
            self.notes_list_widget.addItem(item)
            self.notes.append(note)

    def edit_selected_note(self):
        selected_items = self.notes_list_widget.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            note = selected_item.data(Qt.UserRole)
            dialog = NoteDialog(self, note)
            if dialog.exec() == QDialog.Accepted:
                new_note = dialog.note
                index = self.notes.index(note)
                self.notes[index] = new_note
                selected_item.setData(Qt.UserRole, new_note)
                selected_item.setText(str(new_note))

    def delete_selected_note(self):
        selected_items = self.notes_list_widget.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            note = selected_item.data(Qt.UserRole)
            self.notes.remove(note)
            self.notes_list_widget.takeItem(self.notes_list_widget.row(selected_item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesWindow()
    window.show()
    sys.exit(app.exec())

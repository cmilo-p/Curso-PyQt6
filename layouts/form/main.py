import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDateEdit, QLineEdit, QComboBox, QFormLayout, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QDate


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 200, 300)
        self.setWindowTitle("FormLayout")
        self.crear_formulario()
        self.show()

    def crear_formulario(self):
        titulo = QLabel("Solicitud de ingreso")
        titulo.setFont(QFont("Arial", 18))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Nombre")
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Apellido")

        self.genero_selection = QComboBox()
        self.genero_selection.addItems(["Masculio", "Femenino"])

        self.fecha_nacimiento_edit = QDateEdit()
        self.fecha_nacimiento_edit.setDisplayFormat("yyyy-MM-dd")
        self.fecha_nacimiento_edit.setMaximumDate(
            QDate.currentDate()
        )
        self.fecha_nacimiento_edit.setCalendarPopup(True)
        self.fecha_nacimiento_edit.setDate(QDate.currentDate())

        self.telefono = QLineEdit()
        self.telefono.setPlaceholderText("605-6485564")

        submit_button = QPushButton("SUBMIT")
        submit_button.clicked.connect(self.mostrar_info)

        primer_h_box = QHBoxLayout()
        primer_h_box.addWidget(self.nombre_edit)
        primer_h_box.addWidget(self.apellido_edit)

        main_form = QFormLayout()
        main_form.addRow(titulo)
        main_form.addRow("Nombre: ", primer_h_box)
        main_form.addRow("Genero: ", self.genero_selection)
        main_form.addRow("Fecha: ", self.fecha_nacimiento_edit)
        main_form.addRow("Telefono: ", self.telefono)
        main_form.addRow(submit_button)

        self.setLayout(main_form)

    def mostrar_info(self):
        QMessageBox.information(self, "Information",
                                f"Nombre: {self.nombre_edit.text()} {self.apellido_edit.text()}\n \
                                Genero: {self.genero_selection.currentText()}\n \
                                Fecha: {self.fecha_nacimiento_edit.text()}\n \
                                telefono: {self.telefono.text()}",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok
                                )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

import sys
import os
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QStackedLayout, QFormLayout, QHBoxLayout, QVBoxLayout, QComboBox, QDateEdit, QMessageBox
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QPixmap, QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle("QStackedLayout")
        self.generate_window()
        self.show()

    def generate_window(self):
        botton_1 = QPushButton("Ventana 1")
        botton_1.clicked.connect(self.change_window)
        botton_2 = QPushButton("Ventana 2")
        botton_2.clicked.connect(self.change_window)
        botton_3 = QPushButton("Ventana 3")
        botton_3.clicked.connect(self.change_window)

        self.buttons_group = QHBoxLayout()
        self.buttons_group.addWidget(botton_1)
        self.buttons_group.addWidget(botton_2)
        self.buttons_group.addWidget(botton_3)

        # Página 1
        tittle = QLabel("Mapa")
        tittle.setFont(QFont("Arial", 18))
        tittle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        image_map = QLabel()
        # Convertir imagen a Mapa de Bits para ser pasado al Qlabel
        pixmap = QPixmap("images/map.png")
        image_map.setPixmap(pixmap)
        # Obtener el tamaño de la ventana
        window_size = self.size()
        image_map.setMaximumSize(window_size)
        image_map.setScaledContents(True)

        page1_layout = QVBoxLayout()
        page1_layout.addWidget(tittle)
        page1_layout.addWidget(image_map)

        container_1 = QWidget()
        container_1.setLayout(page1_layout)

        # Página 2
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

        form_2 = QFormLayout()
        form_2.addRow(titulo)
        form_2.addRow("Nombre: ", primer_h_box)
        form_2.addRow("Genero: ", self.genero_selection)
        form_2.addRow("Fecha: ", self.fecha_nacimiento_edit)
        form_2.addRow("Telefono: ", self.telefono)
        form_2.addRow(submit_button)

        container_2 = QWidget()
        container_2.setLayout(form_2)

        # Página 3
        title3 = QLabel("Observaciones")
        title3.setFont(QFont("Arial", 18))
        title3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.observation = QTextEdit()
        form_3 = QFormLayout()
        form_3.addRow(title3)
        form_3.addRow("Observations", self.observation)

        container_3 = QWidget()
        container_3.setLayout(form_3)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_1)
        self.stacked_layout.addWidget(container_2)
        self.stacked_layout.addWidget(container_3)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.buttons_group)
        main_layout.addLayout(self.stacked_layout)
        self.setLayout(main_layout)

    def change_window(self):
        button = self.sender()

        if button.text().lower() == 'ventana 1':
            self.stacked_layout.setCurrentIndex(0)
        elif button.text().lower() == 'ventana 2':
            self.stacked_layout.setCurrentIndex(1)
        elif button.text().lower() == 'ventana 3':
            self.stacked_layout.setCurrentIndex(2)

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

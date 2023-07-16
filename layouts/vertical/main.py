import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumHeight(200)
        self.setFixedWidth(200)
        self.setWindowTitle('Layout Vertical')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        boton1 = QPushButton('Boton #1')
        boton2 = QPushButton('Boton #2')
        boton3 = QPushButton('Boton #3')
        boton4 = QPushButton('Boton #4')

        boton1.clicked.connect(self.imprimir_nombre_boton)
        boton2.clicked.connect(self.imprimir_nombre_boton)
        boton3.clicked.connect(self.imprimir_nombre_boton)
        boton4.clicked.connect(self.imprimir_nombre_boton)

        layout = QVBoxLayout()
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        layout.addWidget(boton4)

        self.setLayout(layout)

    def imprimir_nombre_boton(self):
        boton = self.sender()
        QMessageBox.information(self, 'Boton press', f'Se le dio click al boton {boton.text()}',
                                QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

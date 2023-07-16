import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QGridLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Çalculadora')
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):

        self.pantalla = QTextEdit()
        # Habilitar o Deshabilitar un campo/Widget
        self.pantalla.setDisabled(True)

        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")

        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")

        boton_ce = QPushButton("CE")
        boton_borrar = QPushButton("<-")
        boton_resultado = QPushButton("=")

        self.main_grid = QGridLayout()
        # addWidget(posicion_inicial_(row/Y), posicion_inicial_(column/X), rowSpan(opcional), colSpan(opcional))
        self.main_grid.addWidget(self.pantalla, 0, 0, 2, 4)
        self.main_grid.addWidget(boton_ce, 2, 0, 1, 2)
        self.main_grid.addWidget(boton_borrar, 2, 2)
        self.main_grid.addWidget(boton_suma, 2, 3)

        self.main_grid.addWidget(boton_7, 3, 0)
        self.main_grid.addWidget(boton_8, 3, 1)
        self.main_grid.addWidget(boton_9, 3, 2)
        self.main_grid.addWidget(boton_division, 3, 3)

        self.main_grid.addWidget(boton_4, 4, 0)
        self.main_grid.addWidget(boton_5, 4, 1)
        self.main_grid.addWidget(boton_6, 4, 2)
        self.main_grid.addWidget(boton_multiplicacion, 4, 3)

        self.main_grid.addWidget(boton_1, 5, 0)
        self.main_grid.addWidget(boton_2, 5, 1)
        self.main_grid.addWidget(boton_3, 5, 2)
        self.main_grid.addWidget(boton_resta, 5, 3)

        self.main_grid.addWidget(boton_0, 6, 0)
        self.main_grid.addWidget(boton_00, 6, 1)
        self.main_grid.addWidget(boton_punto, 6, 2)
        self.main_grid.addWidget(boton_resultado, 6, 3)

        self.setLayout(self.main_grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

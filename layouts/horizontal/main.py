import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        # Limitar Ancho  minimo de la ventana , tamaño en pixeles
        self.setMinimumWidth(600)
        # Limitar el ancho fijo de la ventana, tamaño en pixeles
        self.setFixedHeight(80)
        self.setWindowTitle('Layout Horizontal')
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        correo_label = QLabel('Correo Electronico:')
        correo_input = QLineEdit()
        enviar_button = QPushButton("Enviar")

        # Crear layout y agregar sus componentes
        layout = QHBoxLayout()
        layout.addWidget(correo_label)
        layout.addWidget(correo_input)
        layout.addWidget(enviar_button)

        # Asignar layout a la ventana actual
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QWidget


class VentanaVacia(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        # Definir las dimensiones de la ventana cuando esta vacía
        # la función 'setGeometry()' recibirá cuatro parámetros de posición (X, Y, ANCHO, LARGO)
        self.setGeometry(100, 100, 250, 250)

        # Definir el título de la ventana
        self.setWindowTitle("Mi primera Ventana")

        # Ejecutar la función 'show()' para poder visualizar la ventana
        self.show()


# Inicializar la aplicación
if __name__ == '__main__':

    # Inicializar la aplicación con 'QApplication', el cual ejecuta el mainlloopEvent de la aplicación, es decir,
    # es la que se encarga administrar las interacciones del usuario con la ventana
    app = QApplication(sys.argv)

    # Generar instancia de VentanaVacia (clase con los métodos que mostraran la interfaz al usuario)
    ventana = VentanaVacia()

    # Ejecutar la aplicación dentro de 'sys.exit()' para asegurar que corte todos los recursos usados en la aplicación
    # al momento de cerrar la ventana de esta misma
    sys.exit(app.exec())

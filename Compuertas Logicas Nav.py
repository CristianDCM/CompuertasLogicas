from PyQt5.QtWidgets import QApplication, QMainWindow  # Ventana principal
from PyQt5.QtCore import QUrl # Para abrir una URL
from PyQt5.QtWebEngineWidgets import QWebEngineView # Para mostrar una pagina web
import sys 
#pip install PyQt5 PyQtWebEngine
class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__() # Constructor de la clase padre
        self.browser = QWebEngineView() # Crea un objeto de tipo QWebEngineView
        self.browser.setUrl(QUrl('http://163.10.22.82/OAS/compuertas_logicas/Simulacion/editor_simple.html'))
        self.setCentralWidget(self.browser) # Agrega el objeto browser al centro de la ventana
        self.setGeometry(100, 100, 800, 450) # (x, y, ancho, alto)
        self.show() # Muestra la ventana

app = QApplication(sys.argv) # Crea un objeto de tipo QApplication
QApplication.setApplicationName('Simulador de Compuertas Logicas')
window = MainWindow() # Crea un objeto de tipo MainWindow
app.exec_() # Ejecuta la aplicacion
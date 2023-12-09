import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
#pip install PyQt5 PyQtWebEngine

URL = 'http://163.10.22.82/OAS/compuertas_logicas/Simulacion/editor_simple.html' 
WINDOW_SIZE = (100, 100, 800, 450)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(URL))
        self.setWindowIcon(QIcon('img/logic.ico'))
        self.setWindowTitle("Simulador de compuertas lógicas")
        self.setCentralWidget(self.browser)
        self.setGeometry(*WINDOW_SIZE)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

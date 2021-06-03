import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.browser = QWebEngineView()
      self.browser.setUrl(QUrl('http://google.com'))
      self.setCentralWidget(self.browser)
      self.showMaximized()
      
      # navbar
      navbar = QToolBar()
      self.addToolBar(navbar)

      backButton = QAction('Back', self)
      backButton.triggered.connect(self.browser.back)
      navbar.addAction(backButton)

      forwardButton = QAction('Forward', self)
      forwardButton.triggered.connect(self.browser.forward)
      navbar.addAction(forwardButton)

app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow()
app.exec_()
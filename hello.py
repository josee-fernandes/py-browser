import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.browser = QWebEngineView()
      self.browser.setUrl(QUrl('https://google.com'))
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

      refreshButton = QAction('Refresh', self)
      refreshButton.triggered.connect(self.browser.reload)
      navbar.addAction(refreshButton)

      homeButton = QAction('Home', self)
      homeButton.triggered.connect(self.navigateHome)
      navbar.addAction(homeButton)
   
   def navigateHome(self):
      self.browser.setUrl(QUrl('https://google.com'))

app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow()
app.exec_()
import sys
from PyQt4 import QtCore, QtGui, QtWebKit

class EvernoteWindow(QtGui.QMainWindow):

    def __init__(self,url="https://evernote.com/"):
        """
            Initialize a Window with the Evernote log in screen
        """

        QtGui.QMainWindow.__init__(self)
        self.resize(500,500)
        self.centralwidget = QtGui.QWidget(self)

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.frame = QtGui.QFrame(self.centralwidget)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.html = QtWebKit.QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)
        self.html.load(QtCore.QUrl(url))
        self.html.show()


        
    def closeEvent(self,event):
        """ When the window is closed, it gets the last URL. 
        """
        self.url = self.html.url().toString()
        event.accept() # Closes the window
        

def get_token(url):
    """ Opens a webbrowser window to log in into Evernote. 
        Returns the URL to which the log in procedure redirects.
    """
    app = QtGui.QApplication(sys.argv)
    main = EvernoteWindow( url )
    main.show()
    app.exec_()
    return main.url



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Browser()
    main.show()
    sys.exit(app.exec_())
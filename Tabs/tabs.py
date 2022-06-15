# we will create here tabs using PyQt5

# It creates tabs on window and each tab will executes specific widget.

# Step 1: Import all important librabries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

       # Give title to the application window
       # Nota Bene: If you want to make any changes to application window, never forget to use the 'self' 
        self.setWindowTitle("Tabs in PyQt5")
        
        # Resize the application window according to the size you want to see it
        self.resize(500, 500)

        # Create tabs widget
        tabs = QTabWidget()

        # Make the tabs moveable
        tabs.setMovable(True)

        # Add tabs
        tabs.addTab(QLabel("THIS IS TAB 1\nWelcome to tab1"), 'TAB one')
        tabs.addTab(QLabel("THIS IS TAB 2\nWelcome to tab2"), 'TAB two')
        tabs.addTab(QLabel("THIS IS TAB 3\nWelcome to tab3"), 'TAB three')

        # Add layout
        layout = QVBoxLayout()

        # Add tabs to the layout
        layout.addWidget(tabs)

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()


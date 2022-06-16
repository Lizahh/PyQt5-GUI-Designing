# Creating a stacked layout: The QStackedLayout class provides a stack of widgets where only one widget is visible at a time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Step 1: Import all important librabries
class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
       # Give title to the application window
       # Nota Bene: If you want to make any changes to application window, never forget to use the 'self' 
        self.setWindowTitle("Stacked layout in PyQt5")
        
        # Resize the application window according to the size you want to see it
        self.resize(500, 500)

        # Creating stacked layout
        layout = QStackedLayout()

       # Adding widgets to the stacked layout: in it only top widget is visible at first and you can show only one at a time
        layout.addWidget(QLabel("widget on position 1 on stack"))
        layout.addWidget(QLabel("widget on position 2 on stack"))
        layout.addWidget(QLabel("widget on position 3 on stack"))
        layout.addWidget(QLabel("widget on position 4 on stack"))

        

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)

        
# Run the application window
app = QApplication([])
window = MainWindow()
window.show()
app.exec()


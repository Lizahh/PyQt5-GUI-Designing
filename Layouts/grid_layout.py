# Here we will create a grid layout of widgets 

# QGridLayout takes the space made available to it (by its parent layout or by the parentWidget()), divides it up into rows and columns, and puts each widget it manages into the correct cell.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Step 1: Import all important librabries
class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
       # Give title to the application window
       # Nota Bene: If you want to make any changes to application window, never forget to use the 'self' 
        self.setWindowTitle("Grid layout in PyQt5")
        
        # Resize the application window according to the size you want to see it
        self.resize(500, 500)

        # Creating grid layout
        layout = QGridLayout()

       # Adding widgets to the grid layout: we will add coordinates of the new widgets: (1,0) means 1st row and 0th column etc.
        layout.addWidget(QLabel("Widget in 0th row 0th col"), 0,0)
        layout.addWidget(QLabel("Widget in 0th row 1st col"), 0,1)
        layout.addWidget(QLabel("Widget in 0th row 2nd col"), 0,2)
        layout.addWidget(QLabel("Widget in 1st row 0th col"), 1,0)
        layout.addWidget(QLabel("Widget in 1st row 1st col"), 1,1)
        layout.addWidget(QLabel("Widget in 1st row 2nd col"), 1,2)
        layout.addWidget(QLabel("Widget in 2nd row 0th col"), 2,0)
        layout.addWidget(QLabel("Widget in 2nd row 1st col"), 2,1)
        layout.addWidget(QLabel("Widget in 2nd row 2nd col"), 2,2)

        

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


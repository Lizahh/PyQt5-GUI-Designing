# Here we will create a vertical layout of widgets 

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Step 1: Import all important librabries
class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
       # Give title to the application window
       # Nota Bene: If you want to make any changes to application window, never forget to use the 'self' 
        self.setWindowTitle("Vertical layout in PyQt5")
        
        # Resize the application window according to the size you want to see it
        self.resize(500, 500)

        # Creating vertical layout
        layout = QVBoxLayout()

       # Adding widgets to the vertical layout
        layout.addWidget(QLabel("Stuff 1"))
        layout.addWidget(QLabel("Stuff 2"))
        layout.addWidget(QLabel("Stuff 3"))
        layout.addWidget(QLabel("Stuff 4"))
        

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


# we will create here Lists widgets using PyQt5

# QListWidget class is an item-based interface to add or remove items from a list. Each item in the list is a QListWidgetItem object.

# Step 1: Import all important librabries
from ast import Lambda
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Step 2: Make class for the application window
class MyWindow(QMainWindow):
   
    # Making constructor
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)

        # Give title to the application window
        # Nota Bene: If you want to make any changes to application window, never forget to use the 'self' 
        self.setWindowTitle("Lists Widgets in PyQt5")

        # Resize the application window according to the size you want to see it
        self.resize(500,500)

        # Create lists widget
        mylist = QListWidget()

        # Add items to the list
        mylist.addItems(['Easy', 'Medium', 'Hard'])

        # Add label to show which one we selected
        self.label = QLabel("You selected Nothing")

        # Now add the functionality to list widget
        mylist.currentItemChanged.connect(self.show_selected)
        
        # Add layout
        layout = QVBoxLayout()

        # Add combo boxes and label to the layout
        layout.addWidget(mylist)
        layout.addWidget(self.label)

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)

  
    # functions definitions of list
    def show_selected(self, mylist):
        self.label.setText(mylist.text())
        
# Executing the application window
app = QApplication([])
window = MyWindow()
window.show()
app.exec()


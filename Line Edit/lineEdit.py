# we will create here line edits using PyQt5

# line edit is just like an input field. You type some input and it takes in.

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
        self.setWindowTitle("Line Edit in PyQt5")

        # Resize the application window according to the size you want to see it
        self.resize(500,500)

        # Create line edit
        input_field = QLineEdit()

        # Add label to show which one we selected
        self.label = QLabel("You selected Nothing")

        # Now add the functionality to line edit: it will work when you will press enter after giving input
        input_field.returnPressed.connect(lambda: self.show_selected(input_field))
        
        # Add layout
        layout = QVBoxLayout()

        # Add line edit and label to the layout
        layout.addWidget(input_field)
        layout.addWidget(self.label)

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)

  
    # functions definitions of line edit
    def show_selected(self, input_field):
        self.label.setText(input_field.text())

        
# Executing the application window
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

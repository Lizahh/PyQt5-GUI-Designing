# We will create here combo boxes using PyQt5

# Combo boxe is a type of dialogue box containing a combination of controls, such as sliders, text boxes, and drop-down lists.

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
        self.setWindowTitle("Combo Boxes in PyQt5")

        # Resize the application window according to the size you want to see it
        self.resize(500,500)

        # Create combo boxes
        combo = QComboBox()

        # Add items to the combo boxes
        combo.addItems(['Easy', 'Medium', 'Hard'])

        # Add label to show which one we selected
        self.label = QLabel("You selected Nothing")

        # Now add the functionality to these radio buttons
        combo.activated.connect(lambda: self.show_selected(combo))
        
        # Add layout
        layout = QVBoxLayout()

        # Add combo boxes and label to the layout
        layout.addWidget(combo)
        layout.addWidget(self.label)

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)

  
    # functions definitions of combo boxes
    def show_selected(self, combo):
        self.label.setText(combo.currentText())
        
# Executing the application window
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

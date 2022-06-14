
# we will create here radio buttons using PyQt5

# Checkboxes are the ones that can accept only one choice at the same time

# Step 1: Import all important librabries
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
        self.setWindowTitle("CheckBoxes in PyQt5")

        # Resize the application window according to the size you want to see it
        self.resize(500,500)

        # Create radio buttons
        male_button = QRadioButton("Male")
        female_button = QRadioButton("Female")

        # Add label to show which one we selected
        self.label = QLabel("You selected Nothing")

        # Now add the functionality to these radio buttons
        male_button.toggled.connect(lambda: self.selected_radio_button(male_button))
        female_button.toggled.connect(lambda: self.selected_radio_button(female_button))


        # Add layout
        layout = QVBoxLayout()

        # Add radio buttons and label to the layout
        layout.addWidget(male_button)
        layout.addWidget(female_button)
        layout.addWidget(self.label)

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)

  
    # functions definitions of radio buttons
    def selected_radio_button(self, rb): # rb here means radio button
        print(self.label.setText(rb.text()))

# Executing the application window
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

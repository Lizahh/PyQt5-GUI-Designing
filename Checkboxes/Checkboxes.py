# We will create here checkboxes using PyQt5

# Checkboxes are the ones that can accept multiple choices at the same time

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

        # Create checkboxes
        self.label = QLabel("You didn't check anything")
        checkbox1 = QCheckBox("C++")
        checkbox2 = QCheckBox("Java")
        checkbox3 = QCheckBox("Python")
        checkbox4 = QCheckBox("C#")

        # Now add the functionality to these checkboxes
        # for button we do 'btn.clicked.connect()' but for checkboxes, we will use checkbox.toggled.connect()
        checkbox1.toggled.connect(lambda: self.checkbox_function(checkbox1))
        checkbox2.toggled.connect(lambda: self.checkbox_function(checkbox2))
        checkbox3.toggled.connect(lambda: self.checkbox_function(checkbox3))
        checkbox4.toggled.connect(lambda: self.checkbox_function(checkbox4))

        # Make a list to keep track on all the toggled checkboxes
        self.toggled_checkboxes = []

        # Add layout
        layout = QVBoxLayout()

        # Add checkboxes and label to the layout
        layout.addWidget(checkbox1)
        layout.addWidget(checkbox2)
        layout.addWidget(checkbox3)
        layout.addWidget(checkbox4)
        layout.addWidget(self.label)

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)

    # function definitions for checkboxes

    def checkbox_function(self, cb):   # cb here means checkbox1 -> which shows we will give the output of checkbox to this function and it will give something by using that output
        # print(cb.text())  # It means show the text of clicked checkbox on the command window. we didnt use self, so it will not be shown on application window

        # we can also do the following to the output of our checkboxes. It will return booleans (True or False) to the command window
        # print(cb.isChecked())
        
        # But,we will create proper functionality instead of just displaying the selected text on the command window

        if(cb.isChecked()):
            # if the checkbox will be toggled then the text of that checkbox will be added to this list
            self.toggled_checkboxes.append(cb.text())
        
        # if the checkbox is not toggled, then this part will run
        else:

            # if the checkbox is not toggled, then take that checkbox text out from the list

            # we will use the filter function for it
            self.toggled_checkboxes = list(filter(lambda stuff: (stuff!=cb.text()), self.toggled_checkboxes))

            # Lets break down above line into following parts to understand:
            # 1 - self.toggled_checkboxes list will be completely updated each time if the checbox is unchecked or you untoggled it
            # 2 - list() function will create list: as you can create list either by using [] method or list() method. Both are OK
            # 3 - Now we will filter out stuff from the self.toggled_checkboxes list. How it will be done? It will take stuff (stuff is here checkbox)
            # then, it will filter that stuff value in the self.toggled_checkboxes list, and will remove it from there.
        
        
        # Now we will add functionality to change the label
        task_string = ""
        for task in self.toggled_checkboxes:
            task_string += (task+"\n")

        self.label.setText(task_string)
  


# Executing the application window
app = QApplication([])
window = MyWindow()
window.show()
app.exec()

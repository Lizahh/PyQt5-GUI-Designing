# we will create here dialog box using PyQt5

# Whenever some button will be pressed, a new dialogue box (window) will open. As new window is opened, so we need to write a complete class for new window (dialoge).

# Step 1: Import all important librabries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# This is the class for dialog box
class MyDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(MyDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Dialog Box")
        self.resize(200, 200)

        self.label = QLabel("Hey! You are in dialog box window")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        # very important
        self.setLayout(self.layout)


class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

       # Give title to the application window
       # Nota Bene: If you want to make any changes to application window, never forget to use the 'self' 
        self.setWindowTitle("Main Window")

        # Resize the application window according to the size you want to see it
        self.resize(500, 500)

        # Create a button that will jump you to the new dialog box
        btn = QPushButton("Press me to open a new dialog bo")

        # Now add the functionality to that pressed button
        btn.pressed.connect(self.dialog_handler)

        # Add layout
        layout = QVBoxLayout()

        # Add button to the layout
        layout.addWidget(btn)

        # Make a universal widget and add layout to that
        widget = QWidget()
        widget.setLayout(layout)

        # Make this universal widget as central on the application window (dont forget to use self as we are gonna make change on the application widnow)
        self.setCentralWidget(widget)

    def dialog_handler(self):
        dialog = MyDialog()
        dialog.label.setText("Hey! Welcome to new Dialog box")
        dialog.exec()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()

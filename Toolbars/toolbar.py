
# Creating a toolbar in PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Step 1: Import all important librabries
class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
       # Give title to the application window
       # Nota Bene: If you want to make any changes to application window, never forget to use the 'self' 
        self.setWindowTitle("Toolbar in PyQt5")
        
        # Resize the application window according to the size you want to see it
        self.resize(500, 500)

        # Creating toolbar
        toolbar = QToolBar("My Toolbar")

        
        # Create layout
        layout = QVBoxLayout()

        # We will create different widgets of the toolbar

        # Here, we can simply write the following statement to add widget of paint in our toolbar:
        # Never forget to add self here
        # action_btn1 = QAction("Paint", self)

        # Or we can also add the logo on place of the name of the widget
        action_btn1 = QAction(QIcon("paint-logo.png"), "Paint", self)
        action_btn2 = QAction(QIcon("word.png"), "MS Word", self)
        action_btn3 = QAction(QIcon("vlc.png"), "VLC media player", self)
        action_btn4 = QAction(QIcon("chrome.png"), "Chrome", self)
        action_btn5 = QAction(QIcon("task.png"), "task manager", self)
        action_btn6 = QAction(QIcon("folder.png"), "Folders", self)

        # Make sure when you click on the widget, it keep on clicked for all the time you are using that
        action_btn1.setCheckable(True)
        action_btn2.setCheckable(True)
        action_btn3.setCheckable(True)
        action_btn4.setCheckable(True)
        action_btn5.setCheckable(True)
        action_btn6.setCheckable(True)

        # Add these widgets to the toolbar
        toolbar.addAction(action_btn1)
        # We can add a separator to add multiple tools
        toolbar.addSeparator()
        toolbar.addAction(action_btn2)
        # We can add a separator to add multiple tools
        toolbar.addSeparator()
        toolbar.addAction(action_btn3)
        # We can add a separator to add multiple tools
        toolbar.addSeparator()
        toolbar.addAction(action_btn4)
        # We can add a separator to add multiple tools
        toolbar.addSeparator()
        toolbar.addAction(action_btn5)
        # We can add a separator to add multiple tools
        toolbar.addSeparator()
        toolbar.addAction(action_btn6)

        # Add this toolbar to the parent toolbar
        self.addToolBar(toolbar)
    
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


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Buttons Window")
        self.resize(500,500)

        # now lets create buttons
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")

        # we can use the following two lines as labels but they will show output on command window. 
        #label1 = QLabel("Click on button 1")
        #label2 = QLabel("Click on button 2")

        # we want output on application window after we clicked on buttons. to do so , we need to make label part of the class which is our application window class. we will do it by using self keyword
        self.label1 = QLabel("Click on button 1:")
        self.label2 = QLabel("Click on button 2")

        # change the font of these labels: pick font of the label in variable and change it
        font1 = self.label1.font()
        font1.setPointSize(40)

        # now apply this changing of point size of font on label
        self.label1.setFont(font1)

        # change the font of these labels: pick font of the label in variable and change it
        font2 = self.label2.font()
        font2.setPointSize(60)

        # now apply this changing of point size of font on label
        self.label2.setFont(font2)


        # align these labels to center
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)

        # add actions to the button: the function will be called by clicking on button. must call that function with keyword 'self' as those functions are part of class
        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)

        # if you do not want to call to functions on clicking the buttons you can use the lambda functions
        # btn1.clicked.connect(lambda x: self.label.setText("Button 1 is clicked"))
        # btn2.clicked.connect(lambda x: self.label.setText("Button 2 is clicked"))
        
        # add the vertical layout
        layout = QVBoxLayout()

        # Add stuff to the layout using addwidget method
        # if we want to use labels without self, then add them in layout with the following line:
        #layout.addWidget(label1)
        # layout.addWidget(label2)

        # if you want to show label on the application window, then add them in layout with self keyword
        layout.addWidget(self.label1)
        layout.addWidget(btn1)
        layout.addWidget(self.label2)
        layout.addWidget(btn2)

        # Create a universal widget and add everything to that i.e. layouts, buttons etc.
        widget = QWidget()

        # First of all, add layout to this universal widget mtlb is widget ko aik layout di pehly
        widget.setLayout(layout)

        # make this widget central on the window: as we are making changes on application window, so use self

        self.setCentralWidget(widget)

        # must give self as parameter in both these functions
    def btn1_clicked(self):
        # this print output will be displayed on the command window, not on the application window
        #print("Button 1 is clicked")
        # to display output on the application window, use the following commands
        self.label1.setText("You clicked on button 1")
    def btn2_clicked(self):
        # this print output will be displayed on the command window, not on the application window
        #print("Button 2 is clicked")

        # to display output on the application window, use the following commands
        self.label2.setText("You clicked on button 2")

# Now lets make application and run it
app = QApplication([])
window = MyWindow()
window.show()
app.exec()





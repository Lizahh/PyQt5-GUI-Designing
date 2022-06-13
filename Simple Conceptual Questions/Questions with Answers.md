### 1. What is PyQt5?

Answer: 
  It is front end library that helped us to build with Python with other languages. The most important thing to remember about PyQt5 is 'It is class based API', which means everything in it is done by making and using classes.

### 2 - Which classes are imported from the main class of PyQt5 to use the labels, windows etc.?
Answer: 
  * from PyQt5.QtWidgets import QLabel
  * from PyQt5.QtWidgets import QMainWindow
  * from PyQt5.QtWidgets import QApplication

### 3 - Do we need to import all these three files each time to make a widget?
Answer:
  No, we can simply write from PyQt5.QtWidgets import *.

### 4 - Why to import from PyQt5.QtCore import * ?
Answer:
It is important to import it as it is used to align stuff and widgets.

### 5 -	What is the purpose of layout?
Answer: 
     Layout is important as we are working on multiple buttons. Layout is just a way to arrange our things in our application. For example, lets talk about vertical layout. So, if we add 5 things in vertical layout, then everything will be in vertical way like a stack on the application. To handle the layout, we need to import:
* from PyQt5.QtGui import *

### 6 - Which command is used to create buttons in PyQt5?
Answer: 
  Btn = QPushButton(“Button1”)


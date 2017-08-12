import sys
from PyQt5 import QtWidgets

# Whole application definition
app = QtWidgets.QApplication(sys.argv)
# Sys.argv :- allows us to pass command line arguments to the app.

window = QtWidgets.QDialog()
window.setGeometry(50, 50, 500, 300)
# Set Geometry :- X,Y, Width, Height
window.setWindowTitle("My Window")
# Window Title

window.show()
# Shows the window on user's screen

sys.exit(app.exec_())


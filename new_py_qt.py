import sys

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
from PySide6.QtSvg import *
# MAIN WINDOW
# ////
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize (200, 200)
        # QFrame / BG
        
        self.bg = QFrame ()
        self.bg.setStyleSheet ("background-color: #333")
        self.bg_layout = QVBoxLayout(self.bg)
        # ADD SVG WIDGET
        file = "emoticon-emotion-expression-laugh-svgrepo-com.svg"
        self.get_size = QSvgRenderer(file)
        self.svg_widget = QSvgWidget(file) 
        self.svg_widget.setFixedSize(self.get_size.defaultSize())

         # ADD SVG TO LAYOUT
        self.bg_layout.addWidget(self.svg_widget, Qt.AlignCenter, Qt.AlignCenter)
                                                  
        # SET CENTRAL WIDGET
        self.setCentralWidget (self.bg)
        self.show()
#if __name__ =="__main__":
# Q APPLICATION
app = QApplication(sys.argv)
window = Mainwindow()
sys.exit(app.exec())
    
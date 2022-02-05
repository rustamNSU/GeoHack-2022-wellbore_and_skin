import sys
from PySide6.QtWidgets import (QWidget,QMainWindow,QMessageBox,QHBoxLayout,QVBoxLayout,QFileDialog, QLabel, QLineEdit, QGridLayout, QApplication,QPushButton)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np


from matplotlib.figure import Figure


# Matplotlib window
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax1 = fig.add_subplot(2, 2, 1)
        self.ax2 = fig.add_subplot(2, 2, 2)
        self.ax3 = fig.add_subplot(2, 2, 3)
        self.ax4 = fig.add_subplot(2, 2, 4)
        
        super(MplCanvas, self).__init__(fig)
        
class DataCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        baf = Figure(figsize=(width, height), dpi=dpi)
        self.grid = baf.add_subplot(111)
        super(DataCanvas, self).__init__(baf)        
        

       



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.Value = 0
        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.initUI()
        self.get_plot_one()
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        self.show()
        
    def get_plot_one(self):
        figure_widget = QWidget()
        figure_layout = QVBoxLayout()
        
        sc = MplCanvas(self, width=20, height=20, dpi=100)
        toolbar = NavigationToolbar(sc, self)
        
        figure_layout.addWidget(toolbar)
        figure_layout.addWidget(sc)

        figure_widget.setLayout(figure_layout)
        self.main_layout.addWidget(figure_widget)
        

    def initUI(self):
        
        data_widget = QWidget()
        self.main_layout.addWidget(data_widget)
        
        
        title = QLabel('K')
        author = QLabel('SKIN')
        review = QLabel('Cd')
        otvet = QLabel('Path')
        
        
        self.runButton = QPushButton("RUN")
        self.openButton = QPushButton("OPEN")
        
        
        self.warning = QLabel('-')
        self.titleEdit = QLabel('-')
        self.authorEdit = QLabel('-')
        self.reviewEdit = QLabel('-')
        self.otvetEdit = QLabel('-')
        
        self.runButton.clicked.connect(self.run_change)    
        self.openButton.clicked.connect(self._on_open_data)

        grid = QGridLayout()
        data_widget.setLayout(grid)
        grid.setSpacing(10)
        
        #grid.addWidget(self.warning, 2, 0)

        grid.addWidget(self.runButton, 1, 0)
        
        grid.addWidget(self.openButton ,1, 1 )
        
        grid.addWidget(title, 3, 0)
        grid.addWidget(self.titleEdit, 3, 1)

        grid.addWidget(author, 4, 0)
        grid.addWidget(self.authorEdit, 4, 1)

        grid.addWidget(review, 5, 0)
        grid.addWidget(self.reviewEdit, 5, 1)
        
        grid.addWidget(otvet, 6, 0)
        grid.addWidget(self.otvetEdit, 6, 1)
        
        
     #   dr = DataCanvas(self, width=20, height=20, dpi=100)
        
       # toolbar = NavigationToolbar(dr, self)
        
    def _on_open_data(self):
        
        file_name = QFileDialog.getOpenFileName(self)
        self.input_path = file_name[0]
        self.otvetEdit.setText(self.input_path)
        self.Value = 1
    def run_change(self):
        if self.Value == 0:
            error = QMessageBox.question(self,
                        "Ошибка", "Файл не обнаружен",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if error == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
            self.Value = 1

        
            
 

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    
    
    sys.exit(app.exec_())
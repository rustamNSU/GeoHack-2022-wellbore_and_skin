import sys
from PySide6.QtWidgets import (QWidget,  QTextEdit, QComboBox,QMainWindow,QMessageBox,QHBoxLayout,QVBoxLayout,QFileDialog, QLabel, QLineEdit, QGridLayout, QApplication,QPushButton)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from PySide6.QtGui import QIcon


from matplotlib.figure import Figure
from data_from_books import read_csv, compute_model_data
from plot_field_data import plot_field_pressure

# Matplotlib window
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        
        
        self.ax = self.fig.add_subplot()
        
        super(MplCanvas, self).__init__(self.fig)
    
    def plot_test_plot(self, field_data, k, skin, cs):
        self.ax.clear()
        compute_model_data(field_data, self.ax, k=k, Skin=skin, Cs=cs)
        
        

        #self.ax.cla()
    
        
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
        self.init_mpl_canvas()
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('GeoHack-2022, анализ ГДИС')

        self.setWindowIcon(QIcon('nsu.png'))
        
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        self.setStyleSheet("background-color: #ffcc99;")
        
        self.show()
        
        
        
        
        
    def init_mpl_canvas(self):
        figure_widget = QWidget()
        figure_layout = QVBoxLayout()
        
        self.mpl_canvas = MplCanvas(self, width=20, height=20, dpi=100)
        toolbar = NavigationToolbar(self.mpl_canvas, self)
        
        figure_layout.addWidget(toolbar)
        figure_layout.addWidget(self.mpl_canvas)

        figure_widget.setLayout(figure_layout)
        self.main_layout.addWidget(figure_widget)
        

    def initUI(self):
        
        data_widget = QWidget()
        self.main_layout.addWidget(data_widget)
        
        
        k_label = QLabel('проницаемость, md')
        skin_label = QLabel('Skin')
        cs_label = QLabel('Cs, m3/Pa')
        
        
        self.runButton = QPushButton("RUN")
        self.openButton = QPushButton("OPEN")
        
        
        #self.warning = QLabel('-')
        self.k_text = QLineEdit()
        self.skin_text =QLineEdit()
        self.cs_text = QLineEdit()
        
      
        
        self.runButton.clicked.connect(self.run_change)
        self.updateValue = 0   
        self.openButton.clicked.connect(self._on_open_data)
        
    



        
        
        
        

        grid = QGridLayout()
        data_widget.setLayout(grid)
        grid.setSpacing(10)
        
        #grid.addWidget(self.warning, 2, 0)

        grid.addWidget(self.runButton, 1, 0)
        
        grid.addWidget(self.openButton ,1, 1 )
        
        grid.addWidget(k_label, 2, 0)
        grid.addWidget(self.k_text, 2, 1)

        grid.addWidget(skin_label, 3, 0)
        grid.addWidget(self.skin_text, 3, 1)

        grid.addWidget(cs_label, 4, 0)
        grid.addWidget(self.cs_text, 4, 1)
        
      #  grid.addWidget(otvet, 6, 0)
        #grid.addWidget(self.otvetEdit, 6, 1)
        
        #grid.addWidget(self.combo_box, 3, 0)
        
        
   
       
       
    def _on_open_data(self):
        file_name = QFileDialog.getOpenFileName(self)
        self.input_path = file_name[0]
        #self.otvetEdit.setText(self.input_path)
        self.Value = 1
        
    def read_data(self):
        self.field_data = read_csv(self.input_path)
        self.k_text.setText('1.07e-14')
        self.skin_text.setText('7.7')
        self.cs_text.setText('2.3e-7')

        
    def run_change(self):
        if self.Value == 0:
            error = QMessageBox.question(self,
                        "Ошибка", "Файл не обнаружен!",
                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if error == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            
            if self.updateValue == 0:
                self.read_data()
                self.updateValue = 1
            k = float(self.k_text.text())
            skin = float(self.skin_text.text())
            cs = float(self.cs_text.text())
            self.mpl_canvas.plot_test_plot(self.field_data, k , skin, cs)
            #self.mpl_canvas.clf()
            
            self.mpl_canvas.draw()
            
        
            
 

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    
    
    sys.exit(app.exec_())
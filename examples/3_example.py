import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout
from PyQt5.Qt import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.centralgrid = QGridLayout(self)                                 # +++ self
        self.centralgrid.setContentsMargins(1, 1, 1, 1)

        self.left_widget()
        self.centralgrid.addWidget(self.leftWidget, 0, 0)   #, 38, 1)
        self.centralgrid.setColumnStretch(0, 2)                              # !!!  2
        
        self.right_widget()
        self.centralgrid.addWidget(self.rightWidget, 0, 1)  #, 38, 1)
        self.centralgrid.setColumnStretch(1, 9)                              # !!!  9

        self.main_frame_settings()

    # метод для создания левого виджета, а также для создания и размещения кнопок на нём
    def left_widget(self):
        self.leftWidget = QWidget()                                               # leftWidget
        self.leftWidget.setStyleSheet("background-color: rgb(120, 120, 120)") 
        self.leftGrid = QGridLayout(self.leftWidget)

        self.btn_weather = QPushButton("Weather")
        self.btn_birth = QPushButton("Birthdays")

        ''' или так
        spacer = QSpacerItem(25, 25, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.leftGrid.addItem(spacer, 0, 0)
        # кнопки устанавливается не в указанные координаты (14, 0) и (15, 0) !!!
        self.leftGrid.addWidget(self.btn_weather, 14, 0, 1, 1)
        self.leftGrid.addWidget(self.btn_birth, 15, 0, 1, 1)
        self.leftGrid.addItem(spacer, 38, 0)  
        '''
        self.leftGrid.addWidget(self.btn_weather, 14, 1, 1, 1)
        self.leftGrid.addWidget(self.btn_birth,   15, 1, 1, 1)
        
        self.leftGrid.setColumnStretch(0, 1)                        # !!!
        self.leftGrid.setColumnStretch(2, 1)                        # !!!
        self.leftGrid.setRowStretch(0, 1)                           # !!!
        self.leftGrid.setRowStretch(38, 1)                          # !!!
        
        # функция работает !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.leftGrid.setSpacing(25)

    # метод для создания правого виджета,
    def right_widget(self):
        self.rightWidget = QWidget()
        self.rightWidget.setStyleSheet("background-color: rgb(0, 160, 160)")

        self.btn5 = QPushButton("QQ")
        self.btn6 = QPushButton("123")
        
        self.rightGrid = QGridLayout(self.rightWidget)
        # кнопки устанавливается не в указанные координаты (0, 0) и (4, 0) !!!
        self.rightGrid.addWidget(self.btn5, 1, 1, 1, 1)
        self.rightGrid.addWidget(self.btn6, 4, 1, 1, 1)

#        self.rightGrid.setColumnStretch(0, 1)                        # !!!
#        self.rightGrid.setColumnStretch(2, 1)                        # !!!
        self.rightGrid.setRowStretch(0, 1)                            # !!!
        self.rightGrid.setRowStretch(38, 1)                           # !!!
        
        # функция работает !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.rightGrid.setSpacing(75)

    def main_frame_settings(self):
        self.setWindowTitle("Lapa")
        self.resize(640, 480)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import (QWidget, QFileDialog, QLabel, QLineEdit, QGridLayout, QApplication,QPushButton, QVBoxLayout )


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button_open = QPushButton('Выбрать картинку')
        self.button_open.clicked.connect(self._on_open_image)

        #self.label_image = QLabel()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.button_open)

        self.setLayout(main_layout)

    def _on_open_image(self):
        file_name = QFileDialog.getOpenFileName(self, "Выбор картинки", None, "Image (*.png *.jpg)")[0]
        if not file_name:
            return


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()
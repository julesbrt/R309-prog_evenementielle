import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QGridLayout, QWidget, QLabel, QComboBox, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__list = QComboBox()
        self.__list.addItems(["°C -> K", "K -> °C"])
        self.__lab = QLabel("Température")
        self.__entrC = QLineEdit("")
        self.__affC = QLabel("°C")
        self.__convert = QPushButton("Convertir")
        self.__info = QPushButton("?")
        self.__conv = QLabel("Conversion")
        self.__entrK = QLineEdit("")
        self.__affK = QLabel("K")

        button_widget = QWidget()
        grid_button = QGridLayout()
        button_widget.setLayout(grid_button)

        #Vu sur GNU radio, qui utilise également Qt
        grid.addWidget(self.__lab, 0, 0, 1, 1)
        grid.addWidget(self.__entrC, 0, 1, 1, 1)
        grid.addWidget(self.__affC, 0, 2, 1, 2)
        grid.addWidget(self.__list, 1, 2, 1, 1)
        grid.addWidget(self.__convert, 1, 0, 1, 1)
        grid.addWidget(self.__info, 4, 1, 1, 1)
        grid.addWidget(self.__conv, 3, 0, 1, 1)
        grid.addWidget(self.__entrK, 3, 1, 1, 1)
        grid.addWidget(self.__affK, 3, 2, 1, 2)

        # Ajouter les composants au grid ayout
        self.__convert.clicked.connect(self._actionConvert)
        self.__info.clicked.connect(self._actionInfo)
        self.setWindowTitle("Conversion de température")

    def _actionConvert(self):
        try:    
            if self.__list.currentText() == "°C -> K":
                self.__entrK.setText(str(float(self.__entrC.text()) - 273.15))
            else:
                self.__entrC.setText(str(float(self.__entrK.text()) + 273.15))
        except ValueError:
            msg = QMessageBox()
            message = "Veuillez entrer une valeur numérique"
            msg.setIcon(QMessageBox.Information)
            msg.setText(message)
            msg.exec()


    def _actionInfo(self):
        msg = QMessageBox()
        message = "Cette application permet de convertir des températures en °C et en K"
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np



class Window(QMainWindow):
        def __init__(self):
            super().__init__()





            title = "Image Inspector"
            top = 400
            left = 400
            width = 1065
            height = 701

            self.setWindowTitle(title)
            self.setGeometry(top, left, width, height)

            self.MyUI()
            self.LoadDataFromFile()





        def MyUI(self):
            canvas = Canvas(self, width = 8, height = 4)
            canvas.move(0,0)
            button = QPushButton("Click Me", self)
            button.move(100, 450)

            button2 = QPushButton("Click Me 2", self)
            button2.move(200, 450)



class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()


    def plot(self):
        x = np.array([0, .1, .2, .3, .4, .5, .6])
        y = np.array([0, .1, .2, .3, .4, .5, .6])
        concentrations = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                            [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                            [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                            [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                            [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                            [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                            [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

        data = LoadDataFromFile(self)

        fig, ax = plt.subplots()
        im = ax.imshow(data)

        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.ax.set_ylabel("test", rotation=-90, va="bottom")

        ax.set_xticks(np.arange(len(x)))
        ax.set_yticks(np.arange(len(y)))

        ax.set_xticklabels(x)
        ax.set_yticklabels(y)

        ax.set_title("concentrations in brain tissue")
        fig.tight_layout()
        plt.show()
       # x = np.array([50, 30, 40])
       # labels = ["Apples", "Bananas", "Melons"]
       # ax = self.figure.add_subplot(111)
       # ax.pie(x, labels=labels)

# This is where the data is loaded in from the binary file
# For reference this file is loaded in as floats and being
# Such this file will be read in 32 bits at a time as these
# Are 4 byte floats

def LoadDataFromFile(self):
    filepath = "D:/com/byu/resource/data/Brain2/brain_2.bin"
    f = open(filepath, 'rb')
    data = np.fromfile(f, '<f4')
    sizeX = data(1)
    sizeY = data(2)
    sizeZ = data(3)
    sizeImg = sizeX*sizeY*sizeZ
    img = np.reshape(data(4, 4+sizeImg-1), [sizeZ, sizeX, sizeY])
    imgX = np.reshape(data(4+sizeImg, 3+sizeImg+sizeX), [1, sizeX])
    imgY = np.reshape(data(4+sizeImg+sizeX, 3+sizeImg+sizeX+sizeY), [1, sizeY])
    imgZ = np.reshape(data(4+sizeImg+sizeX+sizeY, 3+sizeImg+sizeX+sizeY+sizeZ), [sizeZ, 1])
    return data

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()

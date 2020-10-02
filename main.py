from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

top = 400
left = 400
width = 500
height = 500
f = open('text.txt', 'w')

class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        title = "Лабораторная 1"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setFixedSize(width,height)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.lastPoint = QPoint()
        self.countFig = 0

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("Файл")
        loadAction = QAction("Загрузить", self)
        fileMenu.addAction(loadAction)
        loadAction.triggered.connect(self.loadFile)
        saveAction = QAction("Сохранить",self)
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        exitAction = QAction("Выход", self)
        fileMenu.addAction(exitAction)
        exitAction.triggered.connect(qApp.quit)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.firstPoint = event.pos()
            self.countFig += 1
            f.write("Фигура " + str(self.countFig) + " : " + str(self.lastPoint.x()) + "  " + str(self.lastPoint.y()) + "\n")

    def mouseReleaseEvent(self, event):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.white, 4, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawEllipse(self.lastPoint, 10, 10)
        self.update()

    def paintEvent(self, event):
        canvasPainter  = QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect() )

    def loadFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.image = QImage(filename[0]).scaled(width, height, Qt.IgnoreAspectRatio)

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

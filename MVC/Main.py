import sys

from Model import ModelToDB
from View import ToDoList
from Controller import Controller
from PySide6 import QtGui,QtCore,QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    model = ModelToDB()
    view = ToDoList(model)
    controller = Controller(model, view)
    controller.run()
    sys.exit(app.exec())
import sys

from Model import ModelToDB
from View import ToDoList
from Presenter import Presenter
from PySide6 import QtGui,QtCore,QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    model = ModelToDB()
    view = ToDoList()
    presenter = Presenter(model, view)
    presenter.run()
    sys.exit(app.exec())
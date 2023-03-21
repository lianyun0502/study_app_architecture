import sys

from PySide6 import QtGui, QtCore, QtWidgets

TASK_LIST = [
    'Process email inbox',
    'Write blog Post',
    'Prepare Video scripts',
    'Tax accounting',
    'Prepare presentation',
    'Go to gym',
]

TITLE = 'To Do List'
DELETE_BIN_FILE = 'Delete'

class ToDoList(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle(TITLE)
        self.resize(500, 300)
        self.setupUI()

    def setupUI(self):
        self.frame = QtWidgets.QFrame()
        self.setCentralWidget(self.frame)
        ly = QtWidgets.QVBoxLayout()
        self.frame.setLayout(ly)


        self.task_list = QtWidgets.QListWidget(self.frame)

        self.task_list.addItems(TASK_LIST)
        self.task_list.clicked.connect(self.selectTask)

        self.frame.layout().addWidget(self.task_list)

        self.my_entry = QtWidgets.QLineEdit(self.frame)
        self.my_entry.returnPressed.connect(self.addTask)
        self.frame.layout().addWidget(self.my_entry)

        self.delete_task_btn = QtWidgets.QPushButton(parent=self.frame, text='DELETE_BIN_TXT')
        self.delete_task_btn.setEnabled(False)
        self.delete_task_btn.clicked.connect(self.deleteTask)
        self.frame.layout().addWidget(self.delete_task_btn)


    def selectTask(self):
        self.delete_task_btn.setEnabled(True)

    def addTask(self):
        task = self.my_entry.text()
        self.task_list.addItem(task)
        self.task_list.scrollToBottom()
        self.my_entry.clear()

    def deleteTask(self):
        index = self.task_list.currentIndex().row()
        self.task_list.takeItem(index)
        self.delete_task_btn.setEnabled(False)

    def focusOut(self):pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = ToDoList()
    win.show()
    sys.exit(app.exec())



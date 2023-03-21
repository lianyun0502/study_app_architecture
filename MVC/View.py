from PySide6 import QtWidgets, QtGui, QtCore
from Model import ModelToDB

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
    def __init__(self, model:ModelToDB):
        self.model = model
        super().__init__(parent=None)
        self.setWindowTitle(TITLE)
        self.resize(500, 300)
        self.setupUI()

    def setupUI(self):
        self.frame = QtWidgets.QFrame()
        self.frame.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.setCentralWidget(self.frame)
        ly = QtWidgets.QVBoxLayout()
        self.frame.setLayout(ly)


        self.task_list = QtWidgets.QListWidget(self.frame)

        # self.task_list.addItems(TASK_LIST)
        self.task_list.clicked.connect(self.selectTask)

        self.frame.layout().addWidget(self.task_list)

        self.my_entry = QtWidgets.QLineEdit(self.frame)

        # self.my_entry.returnPressed.connect(self.addTask)
        self.frame.layout().addWidget(self.my_entry)

        self.delete_task_btn = QtWidgets.QPushButton(parent=self.frame, text='DELETE_BIN_TXT')
        self.delete_task_btn.setEnabled(False)
        # self.delete_task_btn.clicked.connect(self.deleteTask)
        self.frame.layout().addWidget(self.delete_task_btn)

    def getEntryText(self)->str:
        return self.my_entry.text()

    def clearEntry(self)->None:
        self.my_entry.clear()

    def selectTask(self):
        self.delete_task_btn.setEnabled(True)

    def updateTaskList(self)->None:
        self.task_list.clear()
        self.task_list.addItems(self.model.getTasks())
        self.task_list.scrollToBottom()

    @property
    def selected_task(self)->int:
        return self.task_list.currentItem().text()

    def bind_addTask(self, func):
        self.my_entry.returnPressed.connect(func)


    def bind_deleteTask(self, func):
        self.delete_task_btn.clicked.connect(func)
        self.delete_task_btn.setEnabled(False)

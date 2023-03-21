from typing import Protocol, Callable
from View import ToDoList
from Model import ModelToDB

class View(Protocol):
    selected_task:str
    def clearEntry(self)->None:...

    def getEntryText(self)->str:...

    def updateTaskList(self)->None:...

    def bind_addTask(self, func:Callable[[...],None]):...

    def bind_deleteTask(self, func:Callable[[...],None]):...

    def show(self)->None:...

class Controller:
    def __init__(self, model:ModelToDB, view:View):
        self.model = model
        self.view = view
        self.view.bind_addTask(self.addTask)
        self.view.bind_deleteTask(self.deleteTask)

    def addTask(self, event=None):
        task = self.view.getEntryText()
        self.view.clearEntry()
        self.model.addTask(task=task)
        self.view.updateTaskList()

    def deleteTask(self, event=None):
        self.model.deleteTask(self.view.selected_task)
        self.view.updateTaskList()


    def run(self) -> None:
        self.view.updateTaskList()
        self.view.show()

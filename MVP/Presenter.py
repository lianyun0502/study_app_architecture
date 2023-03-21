from __future__ import annotations
from typing import Protocol, Callable, Sequence
from View import ToDoList
from Model import ModelToDB


class View(Protocol):
    selected_task:str
    delete_task_btn=None
    def clearEntry(self)->None:...

    def getEntryText(self)->str:...

    def updateTaskList(self, tasks:Sequence)->None:...

    def setupUI(self,presenter:Presenter)->None:
        ...

    # def bind_addTask(self, func:Callable[[...],None]):...
    #
    # def bind_deleteTask(self, func:Callable[[...],None]):...

    def show(self)->None:...

class Presenter:
    def __init__(self, model:ModelToDB, view:View):
        self.model = model
        self.view = view
        # self.view.bind_addTask(self.addTask)
        # self.view.bind_deleteTask(self.deleteTask)

    def handle_addTask(self, event=None):
        task = self.view.getEntryText()
        self.view.clearEntry()
        self.model.addTask(task=task)
        self.updateTaskList()

    def handle_deleteTask(self, event=None):
        self.model.deleteTask(self.view.selected_task)
        self.updateTaskList()
        self.view.delete_task_btn.setEnabled(False)

    def updateTaskList(self)->None:
        tasks = self.model.getTasks()
        self.view.updateTaskList(tasks)

    def run(self) -> None:
        self.view.setupUI(self)
        self.updateTaskList()
        self.view.show()

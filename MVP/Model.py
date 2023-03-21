import sqlite3

class ModelToDB:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('task.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('create table if not exists tasks (title tasks)')

    def addTask(self, task:str)->None:
        self.cursor.execute("insert into tasks values (?)", (task,))
        self.connection.commit()

    def deleteTask(self, task:str)->None:
        self.cursor.execute('delete from tasks where title = ?', (task,))
        self.connection.commit()

    def getTasks(self)->list[str]:
        tasks:list[str] = []
        for row in self.cursor.execute('select title from tasks'):
            tasks.append(str(row[0]))
        return tasks


# manager.py
from file_handler import FileHandler
from models import Task

class TaskManager:
    def __init__(self):
        self.tasks = FileHandler.load()

    def add(self, title, priority):
        self.tasks.append(Task(title, priority))
        FileHandler.save(self.tasks)

    def delete(self, index):
        self.tasks.pop(index)
        FileHandler.save(self.tasks)

    def toggle(self, index):
        task = self.tasks[index]
        task.status = "Completed" if task.status == "Pending" else "Pending"
        FileHandler.save(self.tasks)

    def stats(self):
        total = len(self.tasks)
        done = sum(t.status == "Completed" for t in self.tasks)
        return total, done
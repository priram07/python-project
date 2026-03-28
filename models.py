
# models.py
class Task:
    def __init__(self, title, priority, status="Pending"):
        self.title = title
        self.priority = priority
        self.status = status

    def to_dict(self):
        return self.__dict__
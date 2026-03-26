
# file_handler.py
import json
import os
from models import Task

class FileHandler:
    FILE = "tasks.json"

    @staticmethod
    def save(tasks):
        with open(FileHandler.FILE, "w") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=4)

    @staticmethod
    def load():
        if not os.path.exists(FileHandler.FILE):
            return []
        with open(FileHandler.FILE, "r") as f:
            data = json.load(f)
            return [Task(**t) for t in data]
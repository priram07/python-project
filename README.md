# Task Manager

A **desktop application in Python** to manage personal or work tasks using **Tkinter**.  
It allows you to add tasks, set their priority, mark them as completed, and see reports with a **visual chart** using `matplotlib`.

---

## Features

- **Add Tasks**: Create tasks with a title and priority level (High, Medium, Low).  
- **Toggle Status**: Mark tasks as **Pending** or **Completed** by selecting them.  
- **Delete Tasks**: Remove tasks you no longer need.  
- **Text Report**: Shows the total tasks, completed tasks, pending tasks, and completion rate.  
- **Pie Chart**: Visual representation of task completion using `matplotlib`.  
- **Persistent Storage**: Tasks are saved in a local JSON file (`tasks.json`) so they remain after closing the app.

---

## Installation

1. Clone or download the project folder.  

2. (Optional) Create a **virtual environment** for the project:

```bash
python -m venv .venv


Dependencies
Python 3.x (Tkinter included)
External library: matplotlib (for pie chart)

Notes
The tasks.json file is automatically created and updated as you add, toggle, or delete tasks.
You can easily extend the project to include features like search, filtering, or due dates.


# ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from manager import TaskManager

# ---------------- UI COLORS ----------------
BG = "#f0f2f5"
PRIMARY = "#2c3e50"
ACCENT = "#3498db"
SUCCESS = "#27ae60"
DANGER = "#e74c3c"

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("600x650")
        self.configure(bg=BG)

        self.manager = TaskManager()
        self.setup_ui()
        self.show_list()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=30)
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

        header = tk.Frame(self, bg=PRIMARY, height=70)
        header.pack(fill="x")
        tk.Label(header, text="TASK MANAGER", bg=PRIMARY, fg="white",
                 font=("Arial", 16, "bold")).pack(pady=20)

        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)

    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    def show_list(self):
        self.clear()
        top = tk.Frame(self.container, bg=BG)
        top.pack(fill="x")

        tk.Button(top, text="➕ Add Task", bg=ACCENT, fg="white",
                  command=self.show_add).pack(side="left")
        tk.Button(top, text="📊 Report", command=self.show_report).pack(side="right")

        self.tree = ttk.Treeview(self.container, columns=("t","p","s"), show="headings")
        self.tree.heading("t", text="Task")
        self.tree.heading("p", text="Priority")
        self.tree.heading("s", text="Status")
        self.tree.pack(fill="both", expand=True, pady=10)
        self.refresh()

        bottom = tk.Frame(self.container, bg=BG)
        bottom.pack(fill="x")
        tk.Button(bottom, text="Toggle Status", bg=SUCCESS, fg="white",
                  command=self.toggle_task).pack(side="left", padx=5)
        tk.Button(bottom, text="Delete", bg=DANGER, fg="white",
                  command=self.delete_task).pack(side="left", padx=5)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for t in self.manager.tasks:
            self.tree.insert("", "end", values=(t.title, t.priority, t.status))

    def show_add(self):
        self.clear()
        frame = tk.Frame(self.container, bg="white", padx=20, pady=20)
        frame.place(relx=0.5, rely=0.4, anchor="center", width=400)
        tk.Label(frame, text="New Task", font=("Arial", 14, "bold")).pack()

        entry = tk.Entry(frame)
        entry.pack(fill="x", pady=10)

        priority = ttk.Combobox(frame, values=["High", "Medium", "Low"])
        priority.set("Medium")
        priority.pack(fill="x")

        def save():
            if entry.get():
                self.manager.add(entry.get(), priority.get())
                self.show_list()
            else:
                messagebox.showwarning("Error", "Task cannot be empty")

        tk.Button(frame, text="Save", bg=SUCCESS, fg="white",
                  command=save).pack(fill="x", pady=10)
        tk.Button(frame, text="Back", command=self.show_list).pack()

    def get_selected_index(self):
        sel = self.tree.selection()
        return self.tree.index(sel[0]) if sel else None

    def toggle_task(self):
        i = self.get_selected_index()
        if i is not None:
            self.manager.toggle(i)
            self.refresh()

    def delete_task(self):
        i = self.get_selected_index()
        if i is not None and messagebox.askyesno("Confirm", "Delete task?"):
            self.manager.delete(i)
            self.refresh()

    def show_report(self):
        total, done = self.manager.stats()
        pending = total - done
        msg = f"""
Total: {total}
Completed: {done}
Pending: {pending}
Completion Rate: {(done/total*100) if total else 0:.1f}%
"""
        messagebox.showinfo("Report", msg)
        if total > 0:
            labels = ["Completed", "Pending"]
            sizes = [done, pending]
            colors = ["#27ae60","#e74c3c"]
            plt.figure(figsize=(4,4))
            plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
            plt.title("Task Completion")
            plt.show()
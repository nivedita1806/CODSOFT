import tkinter as tk
from tkinter import messagebox, Scrollbar
import json
import os

FILENAME = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Main App Class
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x520")
        self.root.configure(bg="#fff8dc")

        self.tasks = load_tasks()

        # Title Label
        tk.Label(root, text="📝 To-Do List", font=("Segoe UI", 20, "bold"), bg="#fff8dc", fg="#333").pack(pady=15)

        # Task Entry Section
        entry_frame = tk.Frame(root, bg="#fff8dc")
        entry_frame.pack(pady=5)

        self.task_entry = tk.Entry(entry_frame, font=("Segoe UI", 12), width=30)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.priority_var = tk.StringVar()
        self.priority_var.set("Medium")
        priority_menu = tk.OptionMenu(entry_frame, self.priority_var, "Low", "Medium", "High")
        priority_menu.config(font=("Segoe UI", 10), bg="#cce3de")
        priority_menu.pack(side=tk.LEFT)

        tk.Button(entry_frame, text="Add Task", font=("Segoe UI", 10, "bold"), bg="#00b4d8", fg="white", command=self.add_task).pack(side=tk.LEFT, padx=10)

        # Task List Frame
        list_frame = tk.Frame(root)
        list_frame.pack()

        self.scrollbar = Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, width=60, height=12, font=("Segoe UI", 12),
                                  yscrollcommand=self.scrollbar.set, selectbackground="#ffd6a5")
        self.listbox.pack()
        self.scrollbar.config(command=self.listbox.yview)

        # Action Buttons
        btn_frame = tk.Frame(root, bg="#fff8dc")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="✔ Mark as Done", width=15, bg="#90be6d", fg="white", command=self.mark_done).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="🗑 Delete Task", width=15, bg="#ef233c", fg="white", command=self.delete_task).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="❌ Exit", width=15, bg="#6c757d", fg="white", command=self.exit_app).pack(side=tk.LEFT, padx=10)

        # Status Label
        self.status = tk.Label(root, text="All tasks auto-save to file.", font=("Segoe UI", 9), bg="#fff8dc", fg="#777")
        self.status.pack(pady=5)

        self.load_to_listbox()

        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)

    # Load tasks into listbox
    def load_to_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["done"] else "⬜"
            icon = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}.get(task["priority"], "⚪")
            line = f"{status} {icon} {task['task']}"
            self.listbox.insert(tk.END, line)

    # Add task
    def add_task(self):
        task_text = self.task_entry.get().strip()
        priority = self.priority_var.get()
        if task_text:
            self.tasks.append({"task": task_text, "done": False, "priority": priority})
            self.task_entry.delete(0, tk.END)
            self.load_to_listbox()
        else:
            messagebox.showwarning("Input Needed", "Please enter a task.")

    # Mark as done
    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["done"] = True
            self.load_to_listbox()
        except IndexError:
            messagebox.showinfo("No Task Selected", "Please select a task to mark as done.")

    # Delete task
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")
            if confirm:
                self.tasks.pop(index)
                self.load_to_listbox()
        except IndexError:
            messagebox.showwarning("No Selection", "Select a task to delete.")

    # Exit and Save
    def exit_app(self):
        save_tasks(self.tasks)
        self.root.destroy()

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

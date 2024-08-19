class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed" if self.is_completed else "Not completed"
        return f"Description: {self.description}, Due date: {self.due_date}, Status: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Incorrect task index.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def show_tasks(self):
        print("Task list:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

# Example
manager = TaskManager()
manager.add_task("Do hometask", "2023-10-15")
manager.add_task("Buy food", "2023-10-10")
manager.add_task("Go to the gym", "2023-10-11")

print("All tasks:")
manager.show_tasks()

# Mark one task as completed
manager.mark_task_completed(1)

print("\nOngoing tasks:")
for task in manager.get_pending_tasks():
    print(task)

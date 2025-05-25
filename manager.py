import json
import os
import datetime
import matplotlib.pyplot as plt
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def delete_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def edit_task(self, name: str, **kwargs):
        for task in self.tasks:
            if task.name == name:
                for key, value in kwargs.items():
                    setattr(task, key, value)

    def mark_finished(self, name: str):
        for task in self.tasks:
            if task.name == name:
                task.status = "Finished"
                task.finished_date = datetime.date.today().isoformat()

    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)



    def load_from_file(self, filename="tasks.json"):
        if not os.path.exists(filename):
            return
        try:
            with open(filename, "r") as f:
                content = f.read()
                if not content.strip():
                    return  # pusty plik – nic nie robimy
                data = json.loads(content)
                self.tasks = [Task.from_dict(d) for d in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Błąd wczytywania pliku: {e}")



    def list_tasks_summary(self):
        for task in self.tasks:
            print(f"{task.name} | {task.priority} | {task.status} | {task.due_date} | {task.category}")

    def show_task_details(self, name: str):
        for task in self.tasks:
            if task.name == name:
                print("Szczegóły zadania:")
                for key, value in task.to_dict().items():
                    print(f"{key}: {value}")
                return
        print("Nie znaleziono zadania.")

    def get_statistics(self):
        total = len(self.tasks)
        if total == 0:
            return 0, 0, "Brak zadań"
        finished_on_time = sum(1 for task in self.tasks
                               if task.status == "Finished" and task.finished_date and task.finished_date <= task.due_date)
        avg_duration = sum((datetime.date.fromisoformat(task.finished_date) - datetime.date.fromisoformat(task.created_date)).days
                           for task in self.tasks if task.status == "Finished" and task.finished_date) or 0
        avg_duration /= max(1, sum(1 for t in self.tasks if t.status == "Finished" and t.finished_date))
        categories = {}
        for task in self.tasks:
            categories[task.category] = categories.get(task.category, 0) + 1
        most_common_category = max(categories, key=categories.get)
        return finished_on_time / total * 100, avg_duration, most_common_category

    def show_charts(self):
        status_counts = {"ToDo": 0, "InProgress": 0, "Finished": 0}
        for task in self.tasks:
            status_counts[task.status] += 1
        plt.figure()
        plt.bar(status_counts.keys(), status_counts.values())
        plt.title("Liczba zadań wg statusu")
        plt.tight_layout()
        plt.show()

        category_counts = {}
        for task in self.tasks:
            category_counts[task.category] = category_counts.get(task.category, 0) + 1
        plt.figure()
        plt.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%')
        plt.title("Zadania wg kategorii")
        plt.tight_layout()
        plt.show()

        priority_counts = {}
        for task in self.tasks:
            priority_counts[task.priority] = priority_counts.get(task.priority, 0) + 1
        plt.figure()
        plt.bar(priority_counts.keys(), priority_counts.values(), color="orange")
        plt.title("Zadania wg priorytetu")
        plt.tight_layout()
        plt.show()

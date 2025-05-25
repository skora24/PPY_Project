import datetime

class Task:
    def __init__(self, name, priority, status, due_date, category, description, created_date=None, finished_date=None):
        self.name = name
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.category = category
        self.description = description
        self.created_date = created_date or datetime.date.today().isoformat()
        self.finished_date = finished_date

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(**data)

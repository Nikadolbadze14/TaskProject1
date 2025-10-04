class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tasks = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def assign_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            task.assigned_to = self

    def unassign_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            task.assigned_to = None


class Task:
    def __init__(self, title, priority, status):
        self.title = title
        self.priority = priority
        self.status = status
        self.assigned_to = None

    def __str__(self):
        assigned = self.assigned_to.first_name if self.assigned_to else "unassigned"
        return f"Task: {self.title}, priority: {self.priority}, status: {self.status}, assigned to: {assigned}"

    def mark_status(self, new_status):
        self.status = new_status

    class Project:
        def __init__(self, name, description):
            self.name = name
            self.description = description
            self.users = []
            self.tasks = []

        def __str__(self):
            return f"project: {self.name}, description: {self.description}"

        def add_user(self, user):
            if user not in self.users:
                self.users.append(user)

        def add_task(self, task):
            if task not in self.tasks:
                self.tasks.append(task)


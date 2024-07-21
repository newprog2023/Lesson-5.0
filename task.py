class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Неверный индекс задачи")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")

    def show_current_tasks(self):
        current_tasks = self.get_current_tasks()
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            for task in current_tasks:
                print(task)

# Пример использования
task_manager = TaskManager()

# Добавление задач
task_manager.add_task("Купить продукты", "2023-10-10")
task_manager.add_task("Сдать проект", "2023-10-12")
task_manager.add_task("Позвонить врачу", "2023-10-11")

# Отметка задачи как выполненной
task_manager.mark_task_completed(2)

# Вывод текущих (не выполненных) задач
print("\nТекущие задачи:")
task_manager.show_current_tasks()

# Вывод всех задач
print("Все задачи:")
task_manager.show_tasks()

# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).

# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети
# имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
global numbers
class Task():
    def __init__(self, name, number, dedline, status):
        self.name = name
        self.number = number
        self.dedline = dedline
        self.status = status

    # Реализуй функцию для добавления задач, отметки выполненных задач
    # и вывода списка текущих (не выполненных) задач.
    def add_task(self):
        self.name = input ('Веедите новую задачу текстом')
        self.dedline = input ('Веедите дату окончания выполнения задачи в любом формате')
        status = "активно"
        self.number = self.number =+ 1
        print(f'Введена новая задача № {self.number}.{self.name}. Срок исполнения до {self.dedline}')

    def task_list(self):
        for i in range(numbers):
            print (Task.number, Task.name, )


task1 = Task("Оплатить ЖКХ", 76, 54,"блондин")

while True:
    task1.add_task()
#task1.task_list()


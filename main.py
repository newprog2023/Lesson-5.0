class Account():
    def __init__(self, client_id, count):
        self.client_id = client_id
        self.count = count

    def deposit(self):
        dep = int(input ('сколько внесём рублей ?'))
        print(f'{self.client_id} пополняет счёт на {dep} руб.')
        self.count += dep

    def snimaem(self):
        dep = int(input ('сколько снимем рублей ?'))
        if dep > self.count:
            print(f"На счете всего {self.count} нельзя снять больше")
        else:
            print(f'{self.client_id} снимает со счёта {dep} руб.')
            self.count -= dep

    def info(self):
        print(f'имя клиента - {self.client_id}')
        print(f"на счету -    {self.count}")

war1 = Account("Илья", 76)
war2 = Account("Добрыня", 60)

while True:
    name = int(input('Ваше имя Илья (1) или Добрыня (2) ?'))
    if name != 1 and name != 2:
        print('недопустимый ввод. Попробуйте ответить еще раз, введите 1 или 2')
        continue
    do = int(input('Желаете пополнить счет (1) или снять деньги (2) ?'))
    if do != 1 and do != 2:
        print('недопустимый ввод. Попробуйте ответить еще раз, введите 1 или 2')
        continue
#    money = int(input('Введите сумму в рублях ?'))
    if name == 1:
        war1.info()
        if do == 1:
            war1.deposit()
        elif do == 2:
            war1.snimaem()
        war1.info()
    elif name == 2:
        war2.info()
        if do == 1:
            war2.deposit()
        elif do == 2:
            war2.snimaem()
        war2.info()
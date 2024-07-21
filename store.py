class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def __str__(self):
        """Возвращает строковое представление магазина."""
        return f"Магазин '{self.name}', адрес: {self.address}, ассортимент: {self.items}"


# Пример использования
store = Store("Фрукты и Овощи", "ул. Примерная, д. 10")
store1 = Store("Универсам", "Москва, ул. Яна Купалы, д. 2")

# Добавление товаров
store.add_item("apples", 0.5)
store.add_item("bananas", 0.75)
store1.add_item("bananas", 0.75)

# Вывод информации о магазине
print(store)
print(store1)

# Получение цены товара
price = store.get_price("apples")
print(f"Цена на яблоки: {price}")
price = store1.get_price("apples")
print(f"Цена на яблоки: {price}")

# Обновление цены товара
store.update_price("bananas", 0.80)

# Удаление товара
store.remove_item("apples")

# Вывод обновленной информации о магазине
print(store)
print(store1)

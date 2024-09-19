class Product:

    def __init__(self, name: str, price: float, description: str, dimensions: str):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}, price: {self.price}'


class Customer:

    def __init__(self, name: str, surname: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Purchase:
    def __init__(self, user: Customer):
        self.products: dict[Product, int] = {}  # Словник товарів і їх кількості
        self.user = user

    def add_item(self, item: Product, cnt: int) -> None:
        """Додає товар у кошик або оновлює його кількість."""
        self.products[item] = cnt  # Перезаписуємо кількість товару

    def __str__(self) -> str:
        """Повертає інформацію про замовлення у форматі рядка."""
        product_list = "\n".join([f'{product.name}: {cnt} pcs.' for product, cnt in self.products.items()])
        return f'User: {self.user}\nItems:\n{product_list}'

    def get_total(self) -> float:
        """Обчислює загальну вартість замовлення."""
        total = sum(item.price * cnt for item, cnt in self.products.items())
        return total


lemon = Product('lemon', 5, "yellow", "small", )
apple = Product('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = Customer("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, Customer) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40

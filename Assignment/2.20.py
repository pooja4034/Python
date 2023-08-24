class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_id, item_name, quantity):
        item = {
            'item_id': item_id,
            'item_name': item_name,
            'quantity': quantity
        }
        self.items.append(item)

    def remove_item(self, item_id):
        for item in self.items:
            if item['item_id'] == item_id:
                self.items.remove(item)
                break

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            price_per_item = self.get_price_by_item_id(item['item_id'])
            total_price += price_per_item * item['quantity']
        return total_price

    def get_price_by_item_id(self, item_id):
        prices = {
            'A001': 10,
            'A002': 20,
            'B001': 15,
            'B002': 25
        }
        return prices.get(item_id, 0)  
cart = ShoppingCart()
cart.add_item('A001', 'Item 1', 2)
cart.add_item('B001', 'Item 2', 1)
cart.remove_item('A001')
total_price = cart.calculate_total_price()
print(f"Total price: Rs. {total_price}")
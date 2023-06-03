from kivy.uix.image import Image

class GroceryList:
    items = []

    @classmethod
    def add_item(cls, item_name, quantity):
        cls.items.append((item_name, quantity))

    @classmethod
    def delete_item(cls, index):
        if index < len(cls.items):
            del cls.items[index]

    @classmethod
    def get_list(cls):
        return [f'Item: {item}, Quantity: {quantity}' for item, quantity in cls.items]

    @classmethod
    def get_image(cls):
        img = Image(source='src/data/img/cartopia.png', size_hint=(1, None), height=400)
        return img

    @classmethod
    def delete_item(cls, index):
        if index < len(cls.items):
            del cls.items[index]

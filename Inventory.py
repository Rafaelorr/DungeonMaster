#Inventory.py
from ItemDatabase import item_database, Consumable, Weapon, Armor, randomItems

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name):
    # Search for item in each category of item_database
        for category in item_database.values():
            for item_list in category.values():
                for item in item_list:
                    if item.name == item_name:
                        if item_name in self.items:
                            self.items[item_name]['quantity'] += 1
                        else:
                            self.items[item_name] = {'item': item, 'quantity': 1}
                        print(f"{item_name} added to your inventory.")
                        return
        # Search in randomItems
        for item in randomItems:
            if item.name == item_name:
                if item_name in self.items:
                    self.items[item_name]['quantity'] += 1
                else:
                    self.items[item_name] = {'item': item, 'quantity': 1}
                print(f"{item_name} added to your inventory.")
                return
        print(f"No {item_name} found in the database.")

    def remove_item(self, item_name):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > 1:
                self.items[item_name]['quantity'] -= 1
            else:
                del self.items[item_name]
            return True
        return False

    def use_item(self, item_name, character):
        if item_name in self.items:
            item = self.items[item_name]['item']
            if isinstance(item, Consumable):
                message = item.use(character)
                self.remove_item(item_name)
                return message
            else:
                return f"{item_name} cannot be used."
        return f"No {item_name} in inventory."

    def equip_item(self, item_name, character):
        if item_name in self.items and isinstance(self.items[item_name]['item'], (Weapon, Armor)):
            item = self.items[item_name]['item']
            if character.charClass in item.suitable_classes:
                character.equipItem(item)
                return f"{item_name} equipped."
            else:
                return f"{item_name} is not suitable for your class."
        return f"No {item_name} in inventory."

    def __str__(self):
        inventory_str = "Inventory:\n"
        for item_name, item_info in self.items.items():
            inventory_str += f"{item_name} x{item_info['quantity']}\n"
        return inventory_str


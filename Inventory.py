from ItemDatabase import item_database, Consumable, Weapon, Armor, randomItems

class Inventory:
    def __init__(self):
        # Dictionary to store items with their quantity
        # Format: { item_name: {'item': ItemObject, 'quantity': int} }
        self.items = {}

    def add_item(self, item_name):
        """
        Adds an item to the inventory by searching in the item database and random items list.
        """
        # Helper function to add item to inventory
        def add(item):
            if item_name in self.items:
                self.items[item_name]['quantity'] += 1
            else:
                self.items[item_name] = {'item': item, 'quantity': 1}
            print(f"{item_name} added to your inventory.")

        # Search through item database
        for category in item_database.values():
            for item_list in category.values():
                for item in item_list:
                    if item.name == item_name:
                        add(item)
                        return

        # Search through random items list
        for item in randomItems:
            if item.name == item_name:
                add(item)
                return

        # If not found in any source
        print(f"No {item_name} found in the database.")

    def remove_item(self, item_name):
        """
        Removes one quantity of the specified item from inventory.
        Removes the item completely if quantity drops to 0.
        Returns True if item was removed, False if item was not found.
        """
        if item_name in self.items:
            if self.items[item_name]['quantity'] > 1:
                self.items[item_name]['quantity'] -= 1
            else:
                del self.items[item_name]
            return True
        return False

    def use_item(self, item_name, character):
        """
        Uses a consumable item on the character if it's in the inventory.
        """
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
        """
        Equips a weapon or armor to the character if class is suitable.
        """
        if item_name in self.items:
            item = self.items[item_name]['item']
            if isinstance(item, (Weapon, Armor)):
                if character.charClass in item.suitable_classes:
                    character.equipItem(item)
                    return f"{item_name} equipped."
                else:
                    return f"{item_name} is not suitable for your class."
        return f"No {item_name} in inventory."

    def __str__(self):
        """
        Returns a readable string representation of the inventory.
        """
        if not self.items:
            return "Inventory is empty."
        inventory_str = "Inventory:\n"
        for item_name, item_info in self.items.items():
            inventory_str += f"{item_name} x{item_info['quantity']}\n"
        return inventory_str

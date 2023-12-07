class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name]['quantity'] += 1
        else:
            self.items[item.name] = {'item': item, 'quantity': 1}

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

# Example usage in the game loop
player_inventory = Inventory()

# Example of adding an item to the inventory
player_inventory.add_item(item_database["Rogue"]["weapons"][0])  # Adds a Dagger

# Assuming 'player_character' is the instance of the Character class
# Example of using an item
print(player_inventory.use_item("Health Potion", player_character))

# Example of equipping an item
print(player_inventory.equip_item("Dagger", player_character))

# Displaying the inventory
print(player_inventory)

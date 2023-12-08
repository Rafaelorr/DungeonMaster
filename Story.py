# story.py

class StoryNode:
    def __init__(self, description, options=None, combat=None):
        self.description = description
        self.options = options if options else []
        self.combat = combat

    def display(self):
        print(self.description)
        if self.combat:
            self.handleCombat()
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option['text']}")

    def handleCombat(self):
        # Simple combat logic can be implemented here
        print("A wild enemy appears!")

    def selectOption(self, choice):
        if 1 <= choice <= len(self.options):
            return self.options[choice - 1]['node']
        else:
            print("Invalid choice.")
            return None

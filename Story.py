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

# Sample story structure with combat
def loadStory():
    finalBattle = StoryNode("You face the dragon. The final battle begins!", combat=True)
    dragonLair = StoryNode("You reach the dragon's lair.", [{"text": "Fight the dragon", "node": finalBattle}])
    mysticForest = StoryNode("You are in the Mystic Forest.", [{"text": "Go to the lair", "node": dragonLair}])
    startingVillage = StoryNode("Your journey begins in a small village.", [{"text": "Enter the forest", "node": mysticForest}])

    return startingVillage

class StoryNode:
    def __init__(self, description):
        self.description = description
        self.choices = {}

    def add_choice(self, description, node):
        self.choices[description] = node

    def is_terminal(self):
        return len(self.choices) == 0

    def __str__(self):
        return self.description

def approachDragon():
    def fightDragon():
        return StoryNode("An epic battle ensues. After a fierce struggle, you emerge victorious, the dragon defeated.")

    def negotiateWithDragon():
        return StoryNode("You engage in a tense negotiation. Surprisingly, the dragon agrees to a truce, offering you a portion of its treasure.")

    node = StoryNode("You find the dragon asleep, surrounded by mountains of treasure.")
    node.add_choice("Fight the dragon", fightDragon())
    node.add_choice("Attempt to negotiate with the dragon", negotiateWithDragon())
    return node

def exploreLair():
    def searchTreasure():
        return StoryNode("Among the treasure, you find a legendary weapon that will aid you in future battles.")

    def findSecretExit():
        return StoryNode("You discover a secret exit that leads to a hidden part of the dungeon.")

    node = StoryNode("The lair is filled with riches beyond imagination and several hidden pathways.")
    node.add_choice("Search through the treasure", searchTreasure())
    node.add_choice("Look for a secret exit", findSecretExit())
    return node

def enterDragonsLair():
    def leftPath():
        return approachDragon()

    def rightPath():
        return exploreLair()

    node = StoryNode("You stand at the entrance of the Dragon's Lair, the air thick with danger and opportunity.")
    node.add_choice("Approach the sleeping dragon", leftPath())
    node.add_choice("Explore the rest of the lair", rightPath())
    return node

# Starting Point in Dragon's Lair
dragonsLairStart = enterDragonsLair()

# Example Usage
current_node = dragonsLairStart
while not current_node.is_terminal():
    print(current_node)
    for choice in current_node.choices:
        print(f"- {choice}")
    decision = input("What do you choose to do? ")
    if decision in current_node.choices:
        current_node = current_node.choices[decision]
    else:
        print("Invalid choice. Please choose again.")
print(current_node)

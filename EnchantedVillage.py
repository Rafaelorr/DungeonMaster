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

def investigateCurse():
    def liftTheCurse():
        return StoryNode("After a challenging ritual, you successfully lift the curse, restoring peace to the village.")

    def seekHelp():
        return StoryNode("You decide to seek help from a nearby wizard, known for his knowledge of ancient curses.")

    node = StoryNode("The village is under a mysterious curse, with its inhabitants trapped in an unending slumber.")
    node.add_choice("Attempt to lift the curse", liftTheCurse())
    node.add_choice("Seek help from the wizard", seekHelp())
    return node

def exploreMysteriousForest():
    def findHiddenTreasure():
        return StoryNode("Deep in the forest, you discover hidden treasure, left by an ancient civilization.")

    def encounterForestSpirit():
        return StoryNode("You meet a benevolent forest spirit who offers to aid you in your quest.")

    node = StoryNode("A dense, mysterious forest surrounds the village, rumored to hold secrets and dangers.")
    node.add_choice("Search for hidden treasures", findHiddenTreasure())
    node.add_choice("Explore deeper into the forest", encounterForestSpirit())
    return node

def enterEnchantedVillage():
    def visitVillageCenter():
        return investigateCurse()

    def exploreSurroundingForest():
        return exploreMysteriousForest()

    node = StoryNode("You arrive at the Enchanted Village, shrouded in an eerie silence.")
    node.add_choice("Investigate the village center", visitVillageCenter())
    node.add_choice("Explore the surrounding forest", exploreSurroundingForest())
    return node

# Starting Point in Enchanted Village
enchantedVillageStart = enterEnchantedVillage()

# Example Usage
current_node = enchantedVillageStart
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

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

def exploreRuinedTemple():
    def investigateAltar():
        return StoryNode("You find an ancient artifact at the altar, radiating with mystical energy.")

    def searchChambers():
        return StoryNode("In the chambers, you discover hidden scrolls detailing lost magic spells.")

    node = StoryNode("The temple, though in ruins, holds secrets waiting to be uncovered.")
    node.add_choice("Investigate the altar", investigateAltar())
    node.add_choice("Search the surrounding chambers", searchChambers())
    return node

def encounterGuardianSpirit():
    def battle():
        return StoryNode("After a tough battle, the spirit yields, granting you passage to a hidden treasure.")

    def parley():
        return StoryNode("The spirit, impressed by your respect, shares ancient knowledge and guides you safely through the ruins.")

    node = StoryNode("A guardian spirit bars your way, emanating a powerful aura.")
    node.add_choice("Engage the spirit in battle", battle())
    node.add_choice("Attempt to parley with the spirit", parley())
    return node

def exploreAncientRuins():
    def leftPath():
        return exploreRuinedTemple()

    def rightPath():
        return encounterGuardianSpirit()

    node = StoryNode("You enter the Ancient Ruins. The air is thick with the weight of history.")
    node.add_choice("Go left towards a dilapidated temple", leftPath())
    node.add_choice("Go right where a faint light glows", rightPath())
    return node

# Starting Point in Ancient Ruins
ancientRuinsStart = exploreAncientRuins()

# Example Usage
current_node = ancientRuinsStart
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

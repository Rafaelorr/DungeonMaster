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

def exploreDeepCavern():
    def confrontCreature():
        return StoryNode("You confront the creature, realizing it's a lost spirit. After helping it find peace, a hidden passage reveals itself.")

    def sneakAround():
        return StoryNode("You sneak around the creature. As you pass, you accidentally stumble upon a secret chamber filled with ancient artifacts.")

    node = StoryNode("Deeper in the cavern, you hear a mysterious creature. Its sorrowful howls echo through the corridors.")
    node.add_choice("Confront the creature", confrontCreature())
    node.add_choice("Try to sneak around", sneakAround())
    return node

def findAncientRelic():
    def takeRelic():
        return StoryNode("You take the relic, and the cavern starts to shake. You must escape before it collapses!")

    def leaveRelic():
        return StoryNode("You decide to leave the relic. As you walk away, the cavern's walls shift, revealing a hidden exit.")

    node = StoryNode("You find an ancient relic emitting a strange energy. It seems powerful but potentially dangerous.")
    node.add_choice("Take the relic", takeRelic())
    node.add_choice("Leave the relic and continue exploring", leaveRelic())
    return node

def chooseCavernPath():
    def leftCavern():
        return exploreDeepCavern()

    def rightCavern():
        return findAncientRelic()

    node = StoryNode("You stand at a fork in the cavern. The left path leads into darkness, while the right path glows faintly.")
    node.add_choice("Explore the left path", leftCavern())
    node.add_choice("Explore the right path", rightCavern())
    return node


# Starting Point in Caverns of Echoes
cavernsOfEchoesStart = chooseCavernPath()

# Example Usage
current_node = cavernsOfEchoesStart
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

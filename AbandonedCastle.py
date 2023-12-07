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

def exploreHauntedHall():
    def investigatePortrait():
        return StoryNode("The portrait reveals a hidden switch, opening a secret passage leading to the castle's treasury.")

    def proceedCautiously():
        return StoryNode("You proceed cautiously, avoiding traps and finding a map showing a secret exit from the castle.")

    node = StoryNode("In the haunted hall, a ghostly portrait catches your eye. There is an eerie presence.")
    node.add_choice("Investigate the portrait", investigatePortrait())
    node.add_choice("Proceed cautiously through the hall", proceedCautiously())
    return node

def encounterGuardian():
    def fightGuardian():
        return StoryNode("After a tough battle, you defeat the guardian, gaining access to the ancient archives of the castle.")

    def bargainWithGuardian():
        return StoryNode("You bargain with the guardian, offering a trinket in exchange for safe passage to the castle's library.")

    node = StoryNode("A spectral guardian blocks your path, demanding you prove your worth or offer a tribute.")
    node.add_choice("Fight the guardian", fightGuardian())
    node.add_choice("Bargain with the guardian", bargainWithGuardian())
    return node

def chooseCastlePath():
    def leftWing():
        return exploreHauntedHall()

    def rightWing():
        return encounterGuardian()

    node = StoryNode("You're at the entrance of the abandoned castle. The left wing seems haunted, while the right wing is guarded.")
    node.add_choice("Explore the left wing", leftWing())
    node.add_choice("Head towards the right wing", rightWing())
    return node

# Starting Point in Abandoned Castle
abandonedCastleStart = chooseCastlePath()

# Example Usage
current_node = abandonedCastleStart
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

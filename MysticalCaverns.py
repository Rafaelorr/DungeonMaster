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

def solveMysticPuzzle():
    def success():
        return StoryNode("You solve the puzzle, revealing a hidden chamber with ancient artifacts.")

    def failure():
        return StoryNode("The puzzle remains unsolved, but you find a scroll with historical secrets about the cavern.")

    node = StoryNode("You encounter a complex mystical puzzle, with arcane symbols and shifting stones.")
    node.add_choice("Attempt to solve the puzzle", success())
    node.add_choice("Examine the puzzle but proceed without solving", failure())
    return node

def encounterCaveSpirits():
    def converse():
        return StoryNode("The spirits share knowledge of a powerful spell hidden deep within the cavern.")

    def avoid():
        return StoryNode("You avoid the spirits and find a hidden passage leading to a secluded part of the cavern.")

    node = StoryNode("Ethereal spirits float around a crystal formation, humming an ancient melody.")
    node.add_choice("Converse with the spirits", converse())
    node.add_choice("Avoid the spirits and explore nearby areas", avoid())
    return node

def exploreMysticalCaverns():
    def leftPath():
        return solveMysticPuzzle()

    def rightPath():
        return encounterCaveSpirits()

    node = StoryNode("You enter the Mystical Caverns, where two paths unfold before you.")
    node.add_choice("Take the left path towards a glowing light", leftPath())
    node.add_choice("Take the right path, where whispers echo", rightPath())
    return node

# Starting Point in Mystical Caverns
mysticalCavernsStart = exploreMysticalCaverns()

# Example Usage
current_node = mysticalCavernsStart
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

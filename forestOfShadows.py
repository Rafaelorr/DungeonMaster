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


def encounterFaerieCircle():
    def investigateCircle():
        def touchArtifact():
            return StoryNode("Touching the artifact teleports you to a mysterious part of the forest. You feel disoriented but curious.")

        def takeTreasure():
            return StoryNode("You take the treasure and leave the artifact untouched. As you leave, you hear a faint whisper in the wind.")

        node = StoryNode("You find a hidden treasure and a glowing artifact in the circle. The artifact seems to be calling to you.")
        node.add_choice("Touch the artifact", touchArtifact())
        node.add_choice("Take the treasure and leave the artifact", takeTreasure())
        return node

    def ignoreCircle():
        return StoryNode("You walk away, ignoring the circle. Suddenly, you're ambushed by forest spirits. You must fight to escape!")

    node = StoryNode("You encounter a hidden faerie circle. It seems to be shimmering with magical energy.")
    node.add_choice("Investigate the circle", investigateCircle())
    node.add_choice("Ignore and move on", ignoreCircle())
    return node

def encounterWoundedTraveler():
    def helpTraveler():
        def acceptSecretPath():
            return StoryNode("Taking the secret path, you find yourself in an ancient part of the forest, filled with forgotten secrets.")

        def declineOffer():
            return StoryNode("You decline the offer and continue on the main path, but you feel like you missed an important opportunity.")

        node = StoryNode("The traveler shares the secret path through the forest as a token of gratitude. Do you take it?")
        node.add_choice("Accept the secret path", acceptSecretPath())
        node.add_choice("Politely decline and stick to the main path", declineOffer())
        return node

    def ignoreTraveler():
        return StoryNode("Ignoring the traveler, you suddenly find yourself lost. The forest seems to change around you, leading you astray.")

    node = StoryNode("You find a wounded traveler leaning against a tree. They seem to be in need of help.")
    node.add_choice("Help the traveler", helpTraveler())
    node.add_choice("Ignore and move on", ignoreTraveler())
    return node

def choosePath():
    def leftPath():
        return encounterFaerieCircle()

    def rightPath():
        return encounterWoundedTraveler()

    node = StoryNode("You stand at a fork in the path. The left path leads deeper into the forest, while the right path seems to wind around a hill.")
    node.add_choice("Take the left path", leftPath())
    node.add_choice("Take the right path", rightPath())
    return node


# Starting Point in Forest of Shadows
forestOfShadowsStart = choosePath()

# Example Usage
current_node = forestOfShadowsStart
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

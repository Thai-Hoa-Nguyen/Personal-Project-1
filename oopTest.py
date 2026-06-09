# The Blueprint
class Dog:
    # The Constructor (initializes attributes)
    def __init__(self, name, breed):
        self.name = name   # Attribute
        self.breed = breed # Attribute

    # A Method (behavior)
    def bark(self):
        return f"{self.name} says Woof!"

# Creating Objects (Instances)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rex", "German Shepherd")

print(dog1.bark()) # Output: Buddy says Woof!
print(dog2.bark()) # Output: Buddy says Woof!
class Animal:
    def speak(self):
       pass
    def __str__(self):
       return "Animal"

class Dog(Animal):
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    def __str__(self):
        return "Cat"
#override al speak    

def display_animals(animals):
    for animal in animals:
        print(f"{animal}: {animal.speak()}")
animals = [Dog(),Cat()]
display_animals(animals)


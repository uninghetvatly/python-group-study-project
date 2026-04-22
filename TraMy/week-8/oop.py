class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print(self.name + " says Meow")

class Dog(Animal):
    def speak(self):
        print(self.name + " says Woof")

a = Cat("Tom")
b = Dog("Spike")

a.speak()
b.speak()
class Animal:
    def sound(self):
        print("animals make sounds")
class Dog(Animal):
    def sound(self):
        print("Dog says Bark")
class Cat(Animal):
    def sound(self):
        print("Cat says Meow")
dog=Dog()
dog.sound()
cat=Cat()
cat.sound()

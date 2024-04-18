#The author's names are Samantha Patin and Sydney Eidelbes
#L101

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p2 = Person("Bob", 10)

print(p2.name)
print(p2.age)

#The author's names are Samantha Patin and Sydney Eidelbes
#L103

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "("+str(self.age)+")"

p1 = Person("John", 36)

print(p1)

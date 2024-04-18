#The author's names are Samantha Patin and Sydney Eidelbes
#L104

class Fabric:
    def __init__(item, countryOfOrigin, color):
        item.countryOfOrigin = countryOfOrigin
        item.color = color

    def __str__(item):
        return item.countryOfOrigin + "("+item.color+")"

f1 = Fabric("Turkey","gold")

print(f1)

names = []

for i in range(5):
    name = input("Enter a name: ")
    names.append(name)

swapped = True

for i in range(0, len(names)):
    names[i] = names[i].lower()

while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True
            names[i], names[i + 1] = names[i + 1], names[i]

print(names)

names.reverse()

print(names)
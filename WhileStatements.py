count = 99
while count > 1:
    print(f"{count} bottles of beer on the wall")
    print(f"{count} bottles of beer")
    count -= 1
    print("Take one down, pass it around")
    if count > 1:
        print(f"{count} bottles of beer on the wall!\n")
    elif count == 1:
        print(f"{count} bottle of beer on the wall!\n")
print(f"{count} bottle of beer on the wall")
print(f"{count} bottle of beer")
count -= 1
print("Take one down, pass it around")
print("No bottles of beer on the wall!")
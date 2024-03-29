def main():
    #sets up initial list
    flowers = []
    #adds flowers from inputs until "done"
    while True:
        flower = input("Enter a flower name or 'done' to finish: ").title()
        if flower == "Done":
            break
        flowers.append(flower)
    #Sorts flowers in alphabetical order.
    flowers.sort()

    for i, flower in enumerate(flowers, start = 1):
        print(i, flower)

    search = input("Enter the number of a flower to search for it: ")

    try:
        index = flower.index(search)
        print(f"{search} found at index {index + 1}")
    except ValueError:
        print(f"{search} not found.")
    except IndexError:
        print("Invalid index entered")
    except:
        print("An error occurred")

main()
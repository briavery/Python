#open file in read mode
def main():
    try:
        file = open("sales_totals.txt", "r")

        total = 0
        numLines = 0

        for line in file:
        # strip newline
            floatVal = float(line.strip())
            total += floatVal
            numLines += 1
            print(line)
            average = "{:.2f}".format(total / numLines)

        print(f"Total: {total}\nNumber of entries: {numLines}\nAverage: {average}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error has occured", e)

main()
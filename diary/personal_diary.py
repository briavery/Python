def main():
    #user diary inputs
    date = input("Enter the date: ")
    time = input("Enter the time: ")
    entry = input("Enter your diary entry: ")

    #open files named diary.txt in append mode
    file = open('diary.txt', 'a')
    #add the inputs to text file
    file.write(f"Date: {date}\n")
    file.write(f"Time: {time}\n")
    file.write(f"{entry}\n\n")
    #close file
    file.close()

main()
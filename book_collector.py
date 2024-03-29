def main():
    #creates empty set
    bookList = []
    #begins while loop to add 10 titles
    while len(bookList) < 10:
        #asks for input and adds to list
        bookTitle = input("Enter a book title: ")
        bookList.append(bookTitle.title())

    #sorts previous list and adds it to sorted
    bookList.sort()
    sorted = bookList

    #prints each element in sorted
    for i in range(len(sorted)):
        print(sorted[i])

main()
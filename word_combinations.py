def two_letter_combinations(c):
    #left char
    for i in c:
        #right char
        for j in c:
            #gives us i + j concatenated
            yield i+j

def main():
    letters = ['l','m','n','o','p']
    combinations = two_letter_combinations(letters)
    for combo in combinations:
        print(combo)

main()
def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    if n > 1:
        return n * factorial(n-1)
    
def main():
    num = int(input("Enter a non-negative integer: "))
    answer = factorial(num)
    print(f"The factorial of {num} is {answer}")

main()
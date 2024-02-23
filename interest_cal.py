def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the interest rate as a whole number: "))
time = int(input("Enter the investment time in whole years: "))

result = calculate_interest(principal, rate, time)
print(f"The simple interest for a principal amount of ${principal:,.2f} at an interest rate of {rate}% over a period of {time} years is: ${result:,.2f}")
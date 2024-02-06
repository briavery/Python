#Takes in input for different categories
housing = float(input("How much do you spend on housing: "))
utilities = float(input("How much do you spend on Utilities: "))
groceries = float(input("How much do you spend on Groceries: "))
transportation = float(input("How much do you spend on Transporation: "))
health_care = float(input("How much do you spend on Health Care: "))
personal_care = float(input("How much do you spend on Personal Care: "))
clothing = float(input("How much do you spend on Clothing: "))
debt = float(input("How much do you spend on Debt: "))

#Calculates total amount of money used
total = housing+utilities+groceries+transportation+health_care+personal_care+clothing+debt

#Calculates percentages
housingperc = housing/total*100
utilitiesperc = utilities/total*100
groceriesperc = groceries/total*100
transportationperc = transportation/total*100
health_careperc = health_care/total*100
personal_careperc = personal_care/total*100
clothingperc = clothing/total*100
debtperc = debt/total*100

#Print percentages in order
print(f"you spend {housingperc:.2f}% on Housing, {utilitiesperc:.2f}% on Utilities, {groceriesperc:.2f}% on Groceries, {transportationperc:.2f}% on Transportation, {health_careperc:.2f}% on Health Care, {personal_careperc:.2f}% on Personal Care, {clothingperc:.2f}% on Clothing, and {debtperc:.2f}% on Debt. ")
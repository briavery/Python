# Define a variable for kilogram value
kg_value_1 = 10.6
kg_value_2 = 45.3
kg_value_3 = 94.7
kg_value_4 = 108.1

# Conversion factor: Pounds (lb) = Kilograms (kg)
conversion_factor = 2.20462 

# Calculating kilograms for each pound value
pounds_1 = kg_value_1 / conversion_factor
pounds_2 = kg_value_2 / conversion_factor
pounds_3 = kg_value_3 / conversion_factor
pounds_4 = kg_value_4 / conversion_factor

#The results
print(f"{kg_value_1} kilograms is equal to {pounds_1:.2f} pounds.")
print(f"{kg_value_2} kilograms is equal to {pounds_2:.2f} pounds.")
print(f"{kg_value_3} kilograms is equal to {pounds_3:.2f} pounds.")
print(f"{kg_value_4} kilograms is equal to {pounds_4:.2f} pounds.")
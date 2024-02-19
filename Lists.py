days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []

for i in days:
    steps_taken = int(input(f"How many steps did you take on {i}? "))
    steps.append(steps_taken)

print("")
for i in range(0, len(days)):
    print(f"You took {steps[i]} on {days[i]}")
print("\n")
print("Total steps:", sum(steps))

average = round(sum(steps) / len(days))
print(f"Average steps: {average}")
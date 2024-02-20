time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

heart_rates = []

total_bpm = 0

for i in time_slots:
    bpm = int(input(f"Enter your heart rate (in BPM) in the {i}: "))
    temp = [i, bpm]
    heart_rates.append(temp)
    total_bpm += bpm

print("Average heart rate today: ", total_bpm / len(time_slots), "BPM")
from datetime import datetime, timedelta

def main():
    try:
        #convert to datetime
        temp = input("Enter your birth date (YYYY-MM-DD): ")
        birthday = datetime.strptime(temp, "%Y-%m-%d")

        #birthday not in the past
        if birthday > datetime.now():
            raise ValueError("Birthday cannot be in the future.")

        age_diff = datetime.now() - birthday

        ageYear = int(age_diff.days / 365.25)
        daysRemaining = age_diff.days % 365.25
        age_months = int(daysRemaining / (365.25 / 12))
        daysRemaining %= 365 / 12
        age_days = int(daysRemaining)
        age_hours = int(age_diff.total_seconds() / 3600)
        age_minutes = int(age_diff.total_seconds() / 60)

        print(f"You are {ageYear} years, {age_months} months, and {age_days} days old.")
        print(f"That's approximately {age_diff.days} days, or {age_hours} hours, or {age_minutes} minutes! ")

    except ValueError as e:
        print("Error", e)

main()
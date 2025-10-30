from datetime import datetime
while True:
    date = input("Enter a future date and time (YYYY-MM-DD HH:MM): ")
    try:
        date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        today = datetime.now()
        diff = date - today
        if diff.seconds < 0:
            print:("Date is not in the future")
        else:
            days = diff.days
            hours = diff.seconds // 3600
            reminder = diff.seconds % 3600
            minutes = reminder // 60
            print(f"Time until event: {days} day{'s' if days != 1 else ''}, {hours} hour{'s' if hours != 1 else ''}, and {minutes} minute{'s' if minutes != 1 else ''}")
            if diff.total_seconds() < 24*3600:
                print("This event is in less than 24 hours!")
        break 
    except ValueError:
        print("Date not in correct format! Try again")

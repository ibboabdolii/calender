from datetime import datetime, timedelta

# Get today's date
today_date = datetime.today().strftime('%Y-%m-%d')

# Get information about the days
days_info = []

for i in range(7):
    day = datetime.today() + timedelta(days=i)
    day_info = {
        'date': day.strftime('%Y-%m-%d'),
        'day_name': day.strftime('%A'),
        'day_number': day.day,
        'month': day.strftime('%B'),
        'year': day.year,
    }
    days_info.append(day_info)

# Print the results
print(f"Today's date: {today_date}\n")

for info in days_info:
    print(f"Date: {info['date']}")
    print(f"Day Name: {info['day_name']}")
    print(f"Day Number: {info['day_number']}")
    print(f"Month: {info['month']}")
    print(f"Year: {info['year']}\n")

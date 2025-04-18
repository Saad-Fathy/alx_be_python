from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y %m %d %X")}")

display_current_datetime()

No_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=No_days)
    future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Futur date: {future_date}")

calculate_future_date()

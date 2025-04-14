import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y %m %d %X")}")

display_current_datetime()


int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=5)
    future_date = future_date.strftime("%Y %m %d")
    print(f"Futur date: {future_date}")

calculate_future_date()

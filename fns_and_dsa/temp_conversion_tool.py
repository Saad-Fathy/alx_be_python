FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9     # °C=(°F-32)×(5/9)   
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5     # °F=(9/5)*°C+32

Temp = float(input("Enter the temperature to convert: "))
Unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

def convert_to_celsius(fahrenheit):
    if type(Temp) is float:
        return (f"{Temp} °F is {((Temp-32)*FAHRENHEIT_TO_CELSIUS_FACTOR):.1f} °C")
    else:
        print(f"Invalid temperature. Please enter a numeric value.")
        
def convert_to_fahrenheit(celsius):
    if type(Temp) is float:
        return (f"{Temp} °C is {(CELSIUS_TO_FAHRENHEIT_FACTOR*Temp+32):.1f} °F")
    else:
        print(f"Invalid temperature. Please enter a numeric value.")

if Unit =="F":
    print(convert_to_celsius(Temp))

elif Unit == "C":
    print(convert_to_fahrenheit(Temp))


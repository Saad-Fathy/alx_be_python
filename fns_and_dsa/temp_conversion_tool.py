# fns_and_dsa/temp_conversion_tool.py
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9   
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5   

def convert_to_celsius(fahrenheit):
    celsius=(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit=(CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return fahrenheit

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))   
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
            
        elif unit == "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")

        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
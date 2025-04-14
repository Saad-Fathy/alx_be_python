# fns_and_dsa/temp_conversion_tool.py
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # °C = (°F - 32) × 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # °F = (9/5) × °C + 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))  # Allow decimals
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            celsius = convert_to_celsius(temp)
            print(f"{temp:.1f}°F is {celsius:.1f}°C")
        elif unit == "C":
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp:.1f}°C is {fahrenheit:.1f}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
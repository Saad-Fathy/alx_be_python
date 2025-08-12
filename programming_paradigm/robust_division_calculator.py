def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        return (numerator / denominator)
    
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
        
    except ValueError as e:
        print("Error: Please enter numeric values only.")

if __name__ == "__main__":
    print(safe_divide(10,"saad"))


    
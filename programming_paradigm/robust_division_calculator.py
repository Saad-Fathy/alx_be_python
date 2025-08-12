def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        return num / den
    
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    
    except ValueError:
        raise ValueError("Error: Please enter numeric values only.")
    
print(safe_divide(10,5))
print(safe_divide(10,0))
print(safe_divide(10,"X"))
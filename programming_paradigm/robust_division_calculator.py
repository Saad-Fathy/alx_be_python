def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return result
    
    except ValueError:
        return "Error: Please enter numeric values"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

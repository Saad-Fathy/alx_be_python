def perform_operation(num1,num2,operation):
       
    match operation:
        case 'add':
            result = num1 + num2
            return result
        
    match operation:
        case 'subtract':
            result = num1 - num2
            return result
        
    match operation:
        case 'multiply':
            result = num1 * num2
            return result
            
    match operation:
        case 'divide':
            if num2 == 0:
                print("can't divide by zero")
            result = num1 / num2
            return result
        
perform_operation(4,3,'divide')
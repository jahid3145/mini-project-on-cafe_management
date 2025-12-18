# Features of calcify
# - can do +,-,*,/ operations
#-Accepts full expression(example: 1+2*3-4/5)
#-shows error for division by zero
#-Allows only numbers and operations
#-Runs until user types 'exit'

def calcify():
    print("==== Welcome to Calcify-Simple Calculator===")
    print("Supports : Addtion(+),Subtraction(-),Multiplication(*),Division(/)")
    print("Type 'exit' to quit.\n")
    
    while True:
        
        expression = input('Enter Expression:')
        
        if expression.lower() =='exit':
            print('Exiting Calcify')
            break
        try:
            allowed='0123456789+-*/,()'
            
            if all(char in allowed for char in expression):
                result=eval(expression)
                print(f'Result:{result}')
            else:
                print("Error: Invalid char")
        except ZeroDivisionError:
            print('Error : Division by Zero')
        except exception as e:
            print('Error: Invalid Expression')

calcify()  
        
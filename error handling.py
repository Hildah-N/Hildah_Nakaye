while True:
    try:
        # Get input from user
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        # Convert inputs to float
        num1 = float(num1)
        num2 = float(num2)
        
        # Perform division
        result = num1 / num2
        
        # If we reach here, inputs are valid
        print(f"Result: {num1} / {num2} = {result}")
        break  # Exit loop on successful calculation
        
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue  # Continue loop for invalid input
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        continue  # Continue loop for division by zero
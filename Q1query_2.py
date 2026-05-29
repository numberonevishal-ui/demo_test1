Here's an example PyCharm-compatible script that solves the task you provided:

```python
#!/usr/bin/env python3
import math

def subtraction(a, b):
    """Calculates and returns the difference between two numbers"""
    
    if a < 0 and b > 0:
        return abs(b) - abs(a)
    elif a < 0 and b < 0:
        return abs(b) + abs(a)
    else:
        return a - b

def main():
    """Get command line arguments"""
    
    try:
        args = sys.argv[1:]
        if len(args) != 2:
            print("Invalid number of arguments")
            exit()
        
        a, b = map(int, args)
        if a < 0 or b < 0:
            print("The sum can't be negative and non-positive")
            exit()
        
        result = subtraction(a, b)
        
        print(f"The difference between {a} and {b} is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```

Explanation:

1. The script imports the math module to perform arithmetic operations, which includes functions for the absolute value and the sum of two numbers.
2. A try-except block is used to handle any possible errors that might occur during parsing or execution of the code. If a ValueError exception occurs in the `subtraction` function, it prints an error message with additional information about what happened.
3. The `sys.argv` variable contains the command line arguments (in this case, two integers separated by spaces).
4. The script loads these arguments and runs the `main()` function, which calls the `subtraction` function for each argument in turn.
5. Finally, the script prints a summary of the results using a combination of string interpolation and print() statements.

Make sure to update your command line arguments with the correct values before running this script as it will generate a user-friendly error message if any attempt is made to calculate a negative or non-positive sum.
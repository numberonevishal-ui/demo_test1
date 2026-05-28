def subtraction(num1, num2):
    result = 0
    
    # check if input values are negative or not
    if num1 < 0 and num2 > 0:
        print("Error: Both inputs should be positive.")
        return -1
    
    elif num1 < 0:
        # if input number is negative, subtract it from second number
        result = num1 * (-1)
        
    else:
        # if input number is positive, add it to second number
        result = num2 + num1
        
    return result
```

Example usage:
```python
print(subtraction(-3, 7))
# Output: Error: Both inputs should be positive.
```

Note that this code only checks if both input numbers are negative or not. If they are not, the program will fail with a "Error" message and return -1 as the final result.
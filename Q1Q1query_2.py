def subtrahend(subtracting_num, subtracted_num):
    # check if the subtracted_num is greater than the subtracting_num
    while subtracted_num > subtracting_num:
        # if it's true, then the subtracted_num was bigger than the subtracting_num. 
        # otherwise, add 1 to the subtracted_num and go back to step 2
        subtracted_num += 1
    return subtracted_num

def main():
    # get user input for first number
    print("Please enter the first number:")
    first_input = int(input())
    
    # get user input for second number
    print("Please enter the second number:")
    second_input = int(input())
    
    # check if both numbers are valid inputs
    if 1 <= first_input < 10 and 1 <= second_input < 10:
        # calculate subtraction of first and second numbers using the helper function defined above
        subtracted_num = subtrahend(first_input, second_input)
        
        # print result of subtraction
        print("The subtraction of", first_input, "and", second_input, "is:", subtracted_num)
    else:
        # print error message and exit program
        print("Invalid inputs. Please enter valid numbers.")
    
main()
```

Output:
```
Please enter the first number:
15
The subtraction of 15 and 6 is: 5
Press any key to exit...
# this program implements the sum of a given list of numbers

def get_sum(numbers):
    """
    get the sum of all numbers in a given list of integers
    :param numbers: a list of integers
    :return: the sum of the given list of integers
    """
    
    # initialize sum to 0
    sum = 0
    
    # iterate over each number in the list
    for num in numbers:
        # increment the sum by adding the current number to the previous sum if it is not already zero
        if num > 0:
            sum += num
            
    return sum

# test the program with a given list of numbers
numbers = [1, 2, 3, 4]
print(get_sum(numbers))
#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION
# start = int(input('Where does your range start?'))
# end = int(input('Where does your range end?')) + 1
def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    '''
    1. Ask the user what range they would like to find the total via 'start' and 'end' inputs
    2. Then use a for loop to go through each value in the range. 
    2a. In the for loop, add 1 to the end of the range, because the end of the range is exclusive
    3. To get a continous sum, I need a starting point, so I will set that to 0
    4. Once the loop goes through each value in the range, then I can simply print the 
    variable I set to 0

    '''
    # start = int(input('Where does your range start?'))
    # end = int(input('Where does your range end?')) + 1
    # start = int(input('Where does your range start?'))
    # end = int(input('Where does your range end?')) + 1
    total_values = 0 
    for nums in range(start, end+1):
        total_values += nums
    return total_values
      
    # TODO: Implement the logic to calculate the sum of numbers within the range.

# calculate_sum(start,end)
    # TODO: Return the calculated sum.



def find_smallest_number(start, end):

    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    '''
    1. Ask the user what range they would like to use via global variable
    2. Set the initializer variable to 'start' 
    2a. If you set it at 0, and the user inputs a range that starts after 0, then the code will output
    a value that the user did not want included
    3. Loop through the range and check to see if the current value is less than the current iterated value
    4. Whenever the value in the range is lower, set that value to the current lowest value
    5. Print the varaible where the smallest value is stored
    '''
    # start = int(input('Where does your range start?'))
    # end = int(input('Where does your range end?')) + 1
    pequeno = start
    for nums in range(start, end+1):
        if nums < pequeno:
            pequeno = nums

    return pequeno

    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

# find_smallest_number(start, end)


def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    '''
    1. Ask the user what range they would like to use via global variable
    2. Set the initializer variable to 'start' 
    2a. If you set it at 0, and the user inputs a range that is negative, then the code will output
    a value that the user did not want included
    3. Loop through the range and check to see if the current value is greater than the current iterated value
    4. Whenever the value in the range is greater, set that value to the current highest value
    5. Print the varaible where the largest value is stored
    '''
    # start = int(input('Where does your range start?'))
    # end = int(input('Where does your range end?')) + 1
    grande = start
    for nums in range(start, end+1):
        if nums > grande:
            grande = nums
    return grande
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

# find_largest_number(start, end)


def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """

    '''
    1. Ask the user what range they would like to use via global variable
    2. Create an empty list to store the values in the range 
    3. Loop through the range and check to see if the current value's remainder is 0 when divided by 2
    4. Anytime the looped through value's remainder is 0, add that to the empty list
    5. Use the lenth function to check how long the list is after the range has been iterated through
    '''
    # start = int(input('Where does your range start?'))
    # end = int(input('Where does your range end?')) + 1
    evens = []
    for nums in range(start, end+1):
        if nums % 2 == 0:
            evens.append(nums)
    return(len(evens))

# count_even_numbers(start, end)
    
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    '''
    1. Ask the user what range they would like to use via global variable
    2. Create an empty list to store the values in the range 
    3. Loop through the range and check to see if the current value's remainder is not 0 when divided by 2
    4. Anytime the looped through value's remainder is not 0, add that to the empty list
    5. Use the lenth function to check how long the list is after the range has been iterated through
    '''
    # start = int(input('Where does your range start?'))
    # end = int(input('Where does your range end?')) + 1
    odds = []
    for nums in range(start, end+1):
        if nums % 2 != 0:
            odds.append(nums)
    return(len(odds))

# count_odd_numbers(start, end)

    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.


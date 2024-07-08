def increasingTriplet(nums: list[int]) -> bool:
    # Check if the list has fewer than 3 elements
    if len(nums) < 3:
        return False

    # Initialize the first and second variables to positive infinity
    smallest, second = float('inf'),float('inf')

    # Iterate through the list
    for num in nums:
        if num <= smallest:
            # Update the smallest number found so far
            smallest = num
        elif num <= second:
            # Update the second smallest number found so far
            second = num
        else:
            # If we find a number greater than both first and second, return True
            return True

    # If no such triplet is found, return False
    return False


print(increasingTriplet([1,2,3,4,5]))
print(increasingTriplet([5,4,3,2,1]))
print(increasingTriplet([20,100,10,12,5,13]))
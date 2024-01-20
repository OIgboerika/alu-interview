#!/usr/bin/python3
def minOperations(n):
    """ Minimum Operations Function. """
    if n <= 1:
        return 0

    # Set the minimum operation variable to 0
    min_operations = 0
    # Set the current length variable to 1 as we start with 1 character 'H'
    current_length = 1
    # Set the clipboard variable to 0 as we are not copying anything yet
    clipboard = 0

    # Create an array dp where dp[i] represents the minimum number of operations required to create i characters
    dp = [0 for i in range(n + 1)]

    # Loop until current length is equal to n
    while current_length < n:
        # If n is divisible by current length, we can copy all
        if n % current_length == 0:
            # This is the only time we can copy
            clipboard = current_length
            # Minimum operation is incremented by 1 because we copied
            min_operations += 1

        # Paste the clipboard
        current_length += clipboard
        # Minimum operation is incremented by 1 because we pasted
        min_operations += 1

        # Update the dp array
        dp[current_length] = min_operations

    # Return minimum operation
    return dp[n]

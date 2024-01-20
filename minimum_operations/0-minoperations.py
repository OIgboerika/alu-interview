#!/usr/bin/python3
def min_operations(n):
    """
    Function to find the minimum number of operations required to achieve a specific number of characters
    in a text file using Copy All and Paste operations.

    :param n: The number of characters desired in the text file.
    :return: The minimum number of operations required to achieve the desired number of characters.
    """
    if n <= 1:
        return 0

    min_operations = 0
    current_length = 1
    clipboard = 0

    dp = [0 for _ in range(n + 1)]

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            min_operations += 1

        current_length += clipboard
        min_operations += 1

        dp[current_length] = min_operations

    return dp[n]

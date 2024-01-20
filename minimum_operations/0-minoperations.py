#!/usr/bin/python3
def minOperations(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            operations += 1
        else:
            n = n - 1
            operations += 1
    return operations + 1

def powers_of_two(n):
    if n == 0:
        return [1]
    return list([2**x for x in range(n+1)])
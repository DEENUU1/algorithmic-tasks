def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    minumum = min(numbers)
    new_numbers = numbers[:]
    new_numbers.remove(minumum)
    return new_numbers
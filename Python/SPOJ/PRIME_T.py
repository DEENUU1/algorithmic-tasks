from typing import List


def is_prime(test_num: int, nums: List[int]) -> List[str]:
    result = []

    for num in nums:
        if num == 1:
            result.append("NIE")
        
        elif num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    result.append("NIE")
                    is_prime = False
                    break
            
            if is_prime:
                result.append("TAK")

    return result


input_data = [11, 1, 4]
output = is_prime(len(input_data), input_data)
for result in output:
    print(result)

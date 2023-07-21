from typing import List 



def factorial(num: int) -> List[int]:
    if num == 1:
        return 1
    
    else:
        return (num * factorial(num - 1))


result = str(factorial(4)).strip()
print(" ".join(result))


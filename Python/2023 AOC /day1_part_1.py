

def get_data():
    with open("day1_part_1_input.txt") as f:
        return f.read().splitlines()



def solution(input):
    result = 0
    for word in input:
        nums = []

        for char in word:
            if char.isdigit():
                nums.append(char)

        if len(nums) == 1:
            nums.append(nums[0])

        res = ""
        res += nums[0]
        res += nums[-1]

        result += int(res)

    return result


data = get_data()
s = solution(data)
print(s)
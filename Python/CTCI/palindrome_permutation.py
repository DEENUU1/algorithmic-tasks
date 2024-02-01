# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
# Hints: #106, #121, #134, #136


def check(text: str) -> bool:
    text.lower()

    counter = {}

    for l in counter:
        if counter[l] not in counter:
            counter[l] = 1
        else:
            counter[l] += 1

    count_odd = sum(1 for letter, count in counter.items() if count % 2)
    return count_odd <= 2


print(check("Tact Coa"))

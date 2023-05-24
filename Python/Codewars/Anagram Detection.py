def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    countT, countO = {}, {}
    for i in range(len(test)):
        countT[test[i]] = 1 + countT.get(test[i], 0)
    for i in range(len(original)):
        countO[original[i]] = 1 + countO.get(original[i], 0)
    
    return countT == countO
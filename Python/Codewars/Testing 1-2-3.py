def number(lines):
    lst = []
    if len(lines) == 0:
        return []
    for index, char in enumerate(lines, start=1):
        lst.append(f"{index}: {char}")
        
    return lst
def flamaster(text: str) -> str:
    result = []
    count = 1

    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            result.append(text[i])
            if count > 1:
                result.append(str(count))
            count = 1

    result.append(text[-1])
    if count > 1:
        result.append(str(count))

    return "".join(result)

print(flamaster("AAAAAAAAAABBBBBBBBBBBBBBBB"))

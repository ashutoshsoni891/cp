def solve(arr):
    string = [str(item) for item in arr]
    length = len(string)
    i = length - 1
    j = i - 1

    while (j >= 0 and i >= 1):
        tempString = string[:]
        tempString[i], tempString[j] = tempString[j], tempString[i]  # swap
        numString = int(''.join(string))
        tempNumString = int(''.join(tempString))
        if (tempNumString > numString):
            return tempString
        i -= 1
        j -= 1

    return arr[::-1]


if __name__ == '__main__':
    result = solve(arr=[3, 2, 1])
    print(result)

def isMadhavArray(aList):
    start = 1
    i = 1

    while (start < len(aList)):
        i += 1
        sum = 0
        end = int(i * (i + 1) / 2)

        for j in range(start, end):
            sum += aList[j]

        if (aList[0] != sum):
            return 0

        start = end

    return 1

if __name__ == '__main__':
    result = isMadhavArray([3, 1, 2, 3, 0])
    print(result)
    
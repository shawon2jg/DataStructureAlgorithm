import math

def isPerfectSquare(n):
    if (n == 1):
        return False

    sqrt = abs(math.sqrt(n))

    if (sqrt % 1 != 0):
        return False;

    return True;

def countSquarePairs(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            for j in range(len(arr)):
                if arr[j] > 0:
                    if (arr[i] < arr[j]) & (isPerfectSquare(arr[i] + arr[j])):
                        count += 1

    return count

if __name__ == '__main__':
    print(countSquarePairs([9, 0, 2, -5, 7]))
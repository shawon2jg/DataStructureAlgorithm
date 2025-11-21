def isPrime(n):
    if(n < 1):
        return False

    for i in range(2, n//2):
        if(n % i) == 0:
            return False
    return True

def isEndNine(n):
    if(n % 10) == 9:
        return True
    return False

def findPorcupineNumber(n):
    while (True):
        n += 1
        if(isPrime(n)):
            if(isEndNine(n)):
                i = n
                while (True):
                    i += 1
                    if (isPrime(i)):
                        if (isEndNine(i)):
                            return n
                        break

if __name__ == '__main__':
    print(findPorcupineNumber(139))
def isPrime(n):
    if n < 1:
        return False

    for i in range(2, n//2):
        if n % i == 0:
            return False

    return True

def primeCount(start, end):
    count = 0
    for i in range(start, end + 1):
        if(isPrime(i)):
            count += 1
    return count

if __name__ == '__main__':
    result = primeCount(10, 30)
    print(result)
def isPrime(n):
    for i in range(2, n + 1):
        if (n % i != 0):
            return True
        else:
            return False


if __name__ == "__main__":
    print(isPrime(13))

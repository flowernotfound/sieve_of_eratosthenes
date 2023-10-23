def manual(n):
    sieve = [True] * (n + 1)
    primes = []
    i = 2
    while i <= n:
        if sieve[i]:
            primes.append(i)
            multiple = i * 2
            while multiple <= n:
                sieve[multiple] = False
                multiple += i
        i += 1
    return primes

n = int(input())
primes = manual(n)
print(primes)

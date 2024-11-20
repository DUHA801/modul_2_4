numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    for j in range (2,i):
        if i % j == 0:
            is_prime = False
            primes.append(i)
            break
        elif i == 7:
            pass
            j += 19
    else:
            not_primes.append(i)
print(primes)
print(not_primes)
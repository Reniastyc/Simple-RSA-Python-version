def ext_euclid(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
    return old_s, old_t, old_r

def CalculateNED(l_prime1, l_prime2, l_RSAe0):
    from math import gcd
    l_RSAn = l_prime1 * l_prime2
    l_RSAr = (l_prime1 - 1) * (l_prime2 - 1)
    l_RSAe = l_RSAe0
    while gcd(l_RSAe, l_RSAr) != 1:
        l_RSAe += 2
    l_RSAd = ext_euclid(l_RSAe, l_RSAr)[0]
    while l_RSAd < 0:
        l_RSAd += l_RSAn
    return l_RSAn, l_RSAe, l_RSAd
    
def CalculateRSA(l_keydigit, l_pubdigit, l_level = 3):
    from RdeEM_RandomPrime import GetRandomPrime
    from RdeEM_RandomPrime import GetRandomNumber
    from random import randint

    l_primedigit = (l_keydigit + 1) // 2
    l_primes = [GetRandomPrime(l_primedigit, l_level), GetRandomPrime(l_primedigit, l_level)]
    l_RSAe0 = GetRandomNumber(l_pubdigit) | 1

    while True:
        for l_prime in l_primes[0:-1]:
            l_RSAn, l_RSAe, l_RSAd = CalculateNED(l_prime, l_primes[-1], l_RSAe0)
            l_random = randint(2, l_RSAn - 1)
            if pow(pow(l_random, l_RSAe, l_RSAn), l_RSAd, l_RSAn) == l_random:
                return l_RSAn, l_RSAe, l_RSAd, len(l_primes)
        else:
            l_primes.append(GetRandomPrime(l_primedigit, l_level))

def RSACoding(l_code, l_RSAed, l_RSAn):
    if l_code >= l_RSAn:
        return 0
    else:
        return pow(l_code, l_RSAed, l_RSAn)
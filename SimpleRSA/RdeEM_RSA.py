import RdeEM_RandomPrime
import math
import random

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

def CalculateRSA(l_keydigit, l_pubdigit):
    l_primedigit = int(l_keydigit / 2)
    l_level = 25
    l_prime1 = RdeEM_RandomPrime.GetRandomPrime(l_primedigit, l_level)
    l_prime2 = RdeEM_RandomPrime.GetRandomPrime(l_primedigit, l_level)
    l_RSAn = l_prime1 * l_prime2
    l_RSAr = (l_prime1 - 1) * (l_prime2 - 1)
    l_RSAe = RdeEM_RandomPrime.GetRandomNumber(l_pubdigit - 2)
    l_RSAe <<= 1
    l_RSAe -= 1
    while math.gcd(l_RSAe, l_RSAr) != 1:
        l_RSAe += 2
    l_RSAd = ext_euclid(l_RSAe, l_RSAr)[0]
    while l_RSAd < 0:
        l_RSAd += l_RSAn
    l_random = random.randint(2, l_RSAn - 1)
    if pow(pow(l_random, l_RSAe, l_RSAn), l_RSAd, l_RSAn) == l_random:
        return l_RSAn, l_RSAe, l_RSAd
    else:
        return CalculateRSA(l_keydigit, l_pubdigit)

def RSAEncoding(l_code, l_RSAe, l_RSAn):
    if l_code >= l_RSAn:
        return 0
    else:
        return pow(l_code, l_RSAe, l_RSAn)
    
def RSADecoding(l_code, l_RSAd, l_RSAn):
    if l_code >= l_RSAn:
        return 0
    else:
        return pow(l_code, l_RSAd, l_RSAn)
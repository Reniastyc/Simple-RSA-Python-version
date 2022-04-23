def GetRandomNumber(l_digit):
    from random import randint

    if not isinstance(l_digit, int):
        return 0
    
    if l_digit < 2:
        l_digit = 2
    
    l_num = 1 << (l_digit - 1)

    l_random = randint(0, l_num - 1)
    l_random += l_num
    return l_random

def GetRandomPrime(l_digit, l_level = 3):
    from RdeEM_PrimeTest import MillerRabin

    if not isinstance(l_digit, int):
        return 0
    
    l_random = GetRandomNumber(l_digit) // 6 * 6 - 1

    while True:
        l_random += 2
        if MillerRabin(l_random, l_level):
            return l_random
        l_random += 4
        if MillerRabin(l_random, l_level):
            return l_random

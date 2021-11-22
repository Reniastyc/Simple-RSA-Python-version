import random
import RdeEM_PrimeTest

def GetRandomNumber(l_digit):
    if not isinstance(l_digit, int):
        return 0
    
    if l_digit < 2:
        l_digit = 2
    
    l_random = random.randint(1, 1 << l_digit - 1)
    l_random += 1 << l_digit
    return l_random

def GetRandomPrime(l_digit, l_level = 25):
    if not isinstance(l_digit, int):
        return 0
    
    l_random = GetRandomNumber(l_digit - 3)
    
    l_random *= 6
    l_random -= 1
    
    while True:
        l_random += 2
        if RdeEM_PrimeTest.MillerRabin(l_random, l_level):
            break
        l_random += 4
        if RdeEM_PrimeTest.MillerRabin(l_random, l_level):
            break
    
    return l_random
def MillerRabin(l_number, l_level = 15):
    from random import randint

    if not isinstance(l_number, int):
        return False
    
    if l_number < 2:
        return False
    if l_number == 2:
        return True
    if l_number & 1 == 0:
        return False
    
    r = 0
    d = l_number - 1
    while d & 1 == 0:
        r += 1
        d >>= 1
    
    if l_level > 100:
        l_level = 100
    elif l_level < 1:
        l_level = 1

    l_table = [0] * l_level
    for i in range(l_level):
        l_table[i] = randint(2, 2147483647)
    
    l_neone = l_number - 1

    for l_base in l_table:
        x = pow(l_base, d, l_number)
        if x == 1 or x == l_neone:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, l_number)
            if x == l_neone:
                break
        else:
            return False
    else:
        return True
    
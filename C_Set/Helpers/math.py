def factorials(szam: int) -> int:
    if szam == 0:
        return 1
    else:
        return szam * factorials(szam-1)

def factorials_iterativ(szam: int) -> int:
    eredmeny = 1
    for i in range(2, szam + 1):
        eredmeny *= i
    return eredmeny

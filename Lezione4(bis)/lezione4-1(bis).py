'''Dato un intero x restituisci True se x è palindromo, e False nel caso contrario'''

def palindromo(x: int) -> bool:
    s: str = str(x)
    i: int = 0
    s_length = len(s)
    while i < (s_length // 2):
        j = s_length - (i + 1)
        if s [i] != s[j]:
            return False
        i += 1
    return True

print(palindromo(12321))    
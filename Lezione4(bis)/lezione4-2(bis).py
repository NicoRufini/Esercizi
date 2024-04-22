'''Data una stringa che contiene parole e spazi, riporta la lungheza dell'ultima parola'''

def lenght_of_last_word(s: str) -> int:
    x: list = s.rsplit(" ")
    x0: str = ""
    n = 0
    while n < len(x):
            if x[-(len(x)) + n] == x0:
                n += 1
                return len(x[-(len(x)) + n])
        
            else:
                return len(x[-1]), x
        
#Finisco dopo a casa
print(lenght_of_last_word("hello bobffdy "))
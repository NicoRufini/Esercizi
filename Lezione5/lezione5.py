#La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
#Un errore nell'implementazione porta a risultati inaspettati.
#Trova l'errore e correggi il codice affinché soddisfi i casi di test.

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return 0
    
print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))
print(calculate_average([10, 20, 30]))
print("\n")


#Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
#L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
#La funzione ritorna "Accesso consentito" oppure "Accesso negato". 

def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
        
    else:
        return "Accesso negato"

print(check_access("admin", "12345", True))
print(check_access("admin", "12345", False))
print(check_access("user", "12345", True))
print(check_access("admin", "54321", True))
print(check_access("admin", "54321", False))
print("\n")


#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
#mantenendo l'ordine originale degli elementi.

def remove_duplicates(with_duplicates: list) -> list:
    with_duplicates = dict.fromkeys(with_duplicates)
    with_duplicates = list(with_duplicates)
    
    return with_duplicates

print(remove_duplicates([1, 2, 3, 1, 2, 4]))
print(remove_duplicates([4, 5, 'a', 4, 6]))
print(remove_duplicates(['a', 'b', 'a']))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([]))
print("\n")


#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(numbers: list[int], max_num: int) -> int:
    sum = 0
    for i in numbers:
        if i > max_num:
            sum += i
    return sum

print(sum_above_threshold([1, 10, 20, 30], 10))
print(sum_above_threshold([15, 5, 25], 20))
print(sum_above_threshold([3, 5, 8], 10))
print(sum_above_threshold([50, 60, 70], 25))
print(sum_above_threshold([2, 5, 1], 1))
print("\n")


#Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
#La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
#e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso 
#in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

def rotate_left(elements: list, k: int) -> list:
    # cancella pass e scrivi il tuo codice
    while k > len(elements):
        k -= len(elements)
    elements = elements[k:] + elements[:k]
    return elements

print(rotate_left([1, 2, 3, 4, 5], 2))
print(rotate_left([1, 2, 3, 4, 5], 1))
print(rotate_left([1, 2, 3, 4, 5], 5))
print(rotate_left([1, 2, 3, 4, 5], 8))
print(rotate_left(['a', 'b', 'c', 'd'], 3))
print("\n")


#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or conditionB == True and conditionC == True:
        return "Operazione permessa"
        
    else:
        return "Operazione negata"

print(check_combination(True, False, True))
print(check_combination(False, True, True))
print(check_combination(False, True, False))
print(check_combination(True, True, True))
print(check_combination(False, False, False))
print("\n")


#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
#cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

def check_parentheses(expression: str) -> bool:
    return expression.count("(") == expression.count(")") and expression[0] == "(" and expression[-1] == ")"

print(check_parentheses("()()"))
print(check_parentheses("(()))("))
print(check_parentheses("((()))"))
print(check_parentheses(")("))
print(check_parentheses("(())"))
print("\n")


#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
#Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

def count_isolated(mylist: list) -> int:
    iso: int = 0
    for i in range(len(mylist)):
        if mylist[i] != mylist[i - 1] and mylist[i] != mylist[i - (len(mylist) - 1)]:
            iso += 1

    return iso

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 1, 2, 2, 3, 4, 4]))
print(count_isolated([1, 2, 3, 4, 5]))
print(count_isolated([1, 1, 1, 1, 1]))
print(count_isolated([]))
print("\n")


#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, 
#ritorni un nuovo insieme senza i numeri specificati nella lista.

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for i in elements_to_remove:
        if i in original_set:
            original_set.remove(i)
    return original_set

print(remove_elements({1, 2, 3, 4}, [2, 3]))
print(remove_elements({5, 6, 7}, [7, 8, 9]))
print(remove_elements({1, 2}, [3]))
print(remove_elements(set(), [1, 2, 3]))
print(remove_elements({10, 20, 30}, []))
print("\n")


#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = dict1 | dict2
    for i in dict3:
        if i in dict1 and i in dict2:
            dict3[i] = dict1[i] + dict2[i]
    return dict3

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dictionaries({}, {'a': 10, 'b': 20}))
print(merge_dictionaries({'x': 5}, {'x': -5}))
print(merge_dictionaries({}, {}))
print(merge_dictionaries({'a': 3}, {'b': 4}))
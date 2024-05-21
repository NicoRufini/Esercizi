#Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.
#La lista di interi è formata così:
#    L'elemento in posizione 0 corrisponde alla radice
#    Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#    Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#    Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde a quell'indice è una foglia.

print("1", "-" * 50)

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool: ##list[-len(list) + (i + 2)
    return tree[3] != tree[5] or tree[4] != tree[6]
    #return tree[4] == tree[5]

print(symmetric([1,2,2,3,4,4,3]))
print(symmetric([1,2,2,None,3,None,3]))
print(symmetric([1,2,2,None,3,3,None]))
print(symmetric([1,2,2,None,3,3,None]))


#Data una stringa s e una lista di stringhe wordDict,
#restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più parole del dizionario; 
#False altrimenti.
#Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.

print("2", "-" * 50)

def word_break(s: str, wordDict: list[str]) -> bool: #list[-len(list) + (i + 1)]
    wordDict_2: list[str] = []                      
    for i in range(len(wordDict)):
        #a_word: str = wordDict[i] + wordDict[-len(wordDict) + (i + 1)] + wordDict[i]
        wordDict_2.append(wordDict[i] + wordDict[-len(wordDict) + (i + 1)])
        wordDict_2.append(wordDict[i] + wordDict[-len(wordDict) + (i + 1)] + wordDict[i])
    
    return s in wordDict_2

print(word_break("leetcode",["leet","code"]))
print(word_break("applepenapple", ["apple","pen"]))
print(word_break("catsandog",["cats","dog","sand","and","cat"]))


#Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
#Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
#in genere utilizzando tutte le lettere originali esattamente una volta.

print("3", "-" * 50)

def anagram(s: str, t: str) -> bool:
    # scrivere qui il codice
    s_list: list[str] = []
    t_list: list[str] = []
    
    for i in s:
        s_list.append(i.lower())
    
    for i in t:
        t_list.append(i.lower())
        
    for i in t_list:
        return s_list.count(i) >= 1
    
print(anagram("anagram","nagaram"))
print(anagram("rat", "car"))
print(anagram("silent","listen"))
print(anagram("NeurIPS","UniReps"))


#Progettare un sistema di gestione della biblioteca con i seguenti requisiti:
#    Classe Book:
#        Attributi:
#            book_id: str - Identificatore di un libro.
#            title: str - titolo del libro.
#            author: str - autore del libro
#            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
#        Metodi:
#            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
#            return_book()- Contrassegna il libro come restituito.
#
#    Classe Member:
#        Attributi:
#            member_id: str - identificativo del membro.
#            name: str - il nome del membro.
#            borrowed_books: list[Book] - lista dei libri presi in prestito.
#        Metodi:
#            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
#            return_book(book): rimuove il libro dalla lista borrowed_books.
#
#    Classe Library:
#        Attributi:
#            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
#            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
#        Methodi:
#            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
#            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
#            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
#            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
#            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.

print("4", "-" * 50)




#Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:
#    Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
#    Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
#    Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.
#Nota:
#    Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
#    Solo le celle riempite devono essere convalidate secondo le regole menzionate.

print("5", "-" * 50)

def valid_sudoku(tavola: list[list[int]]) -> bool:
    rows: dict[int, list[int]] = {i: [] for i in range(9)}
    # rows = {0: [], 1: [], ... , 8: []}
    cols: dict[int, list[int]] = {i: [] for i in range(9)}
    squares: dict[int, list[int]] = {f'{i}-{j}': [] for i in range(3) for j in range(3)}
    # squares = dict[int, list[int]] = {i: [] for i in range(9)
    for i in range(9):
       for j in range(9):
           curr_elem: str = tavola[i][j]
           if curr_elem != '.':
                square_i, square_j = i // 3, j // 3
                # square_index = 3 * square_i + square_j
                # if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[square_index]
                if curr_elem in rows[i] or curr_elem in cols[j] or curr_elem in squares[f'{square_i}-{square_j}']:
                    return False
                
                rows[i].append(curr_elem)
                cols[j].append(curr_elem)
                squares[f'{square_i}-{square_j}'].append(curr_elem)
                # squares[square_index].append(curr_elem)
    return True
                
# square_i = 0, square_j = 0 -> 0
# square_i = 0, square_j = 1 -> 1
# square_i = 0, square_j = 2 -> 2
# square_i = 1, square_j = 0 -> 3
# square_i = 1, square_j = 1 -> 4
# square_i = 1, square_j = 2 -> 5
# square_i = 2, square_j = 0 -> 6
# square_i = 2, square_j = 1 -> 7
# square_i = 2, square_j = 2 -> 8 ---> 3 * square_i + square_j

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))


#Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.

print("6", "-" * 50)

class ListNode:
    def __init__(self, val = 0, next = 0) -> None:
        self.val = 0
        self.next = next

def reverse_list(head: ListNode) ->list[int]:
    reversed_list: list[int] = []
    queque: list[ListNode] = [head]

    while queque:
        curr_node = queque.pop()

        if curr_node:
            reversed_list.append(curr_node.val)
            queque.append(curr_node.next)

    return reversed(reversed_list)

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))

head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head))


#Progettare un semplice sistema bancario con i seguenti requisiti:
#    Classe del Account:
#        Attributi:
#            account_id: str - identificatore univoco per l'account.
#            balance: float - il saldo attuale del conto.
#        Metodi:
#            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#            get_balance(): restituisce il saldo corrente del conto.
#    Classe Bank:
#        Attributi:
#            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#        Metodi:
#            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

print("7", "-" * 50)
#Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, 
#o None se il valore non è presente.

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    # cancella pass e scrivi il tuo codice
    for i in dizionario:
        if valore == dizionario[i]:
            return i
        
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'x': 5, 'y': 10, 'z': 15}, 15))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))
print(trova_chiave_per_valore({}, 10))


#Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
#Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codie
    tuples2: dict = {}
    for i, v in tuples:
        tuples2.setdefault(i, []).append(v)
    
    return tuples2

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([('a', 1)]))
print(lista_a_dizionario([]))
print(lista_a_dizionario([('b', 2), ('b', 3)]))
print(lista_a_dizionario([('c', 1), ('b', 2), ('c', 3), ('c', 4)]))


#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
#Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    # cancella pass e scrivi il tuo codice
    n = 0
    for i, v in da_rimuovere.items():
        if i in lista:
            while n < v:
                lista.remove(i)
                n += 1
    return lista

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([1, 1, 1, 1], {1: 2}))
print(rimuovi_elementi([4, 5, 6], {1: 3}))
print(rimuovi_elementi([], {2: 1}))


#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
#e aggrega i voti per studente in un nuovo dizionario.

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice
    persona: dict = {}
    for i in voti:

        persona.setdefault(i["nome"], []).append(i["voto"])
    return persona

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([{'nome': 'Alice', 'voto': 100}]))
print(aggrega_voti([{'nome': 'Bob', 'voto': 75}, {'nome': 'Bob', 'voto': 85}]))
print(aggrega_voti([]))
print(aggrega_voti([{'nome': 'Carl', 'voto': 60}, {'nome': 'Carl', 'voto': 70}, {'nome': 'Carl', 'voto': 80}]))


#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca 
#un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    # cancella pass e scrivi il tuo codice
    dict2: dict = {}
    for i, v in prodotti.items():
        if v > 20:
            dict2[i] = v - (v * 0.1)
    return dict2

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Tavolo': 120.0, 'Sedia': 85.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))
print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))
print(filtra_e_mappa({}))


#PARTE 1
#Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) 
#e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
#PARTE 2
#Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, 
#il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. 
#Questa funzione dovrebbe aggiornare il dizionario del contatto.

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    persona: dict = {"profile" : name, "email" : email, "telefono" : telefono}
    if email:
        persona["email"] = email
    
    if telefono:
        persona["telefono"] = telefono
    
    return persona
    

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    
    if email:
        dictionary["email"] = email
    
    if telefono:
        dictionary["telefono"] = telefono
    
    return dictionary
    
contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))

contact = create_contact("Laura Neri", email="laura.neri@domain.com")
print(create_contact("Laura Neri", email="laura.neri@domain.com"))
print(update_contact(contact, "Laura Neri", email="laura.new@domain.com", telefono=84736736))
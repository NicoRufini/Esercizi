'''
In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una 
simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. 
Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il contendente 
che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. 
C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali 
secondo le seguenti regole:

- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali 
(i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). 
Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. 
Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. 
Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' 
nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. 
Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre 
e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione. Tutte le posizioni di stampa diverse dalla 'T', 
dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. Se è così, 
stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". 
Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, 
potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, 
eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, 
  e determinare l'eventuale fine della gara.
 
SFIDE AGGIUNTIVE:
1. Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. 
Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
Modificatori mossa:
- La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
- La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
 
2. Energia o Stamina:
Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. 
Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. 
L'energia inziale per entrambi gli animali è 100.

Nuove regole di movimento:
- Tartaruga:
    - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, 
      essa guadagna 10 di energia. Non può superare l'energia iniziale.
    - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
    - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

- Lepre:
    - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
    - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
 
3. Ostacoli e Bonus
Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, che influenzano direttamente il movimento degli animali quando vengono calpestati. 
Gli ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.

Dettagli Implementativi:
- Ostacoli:
Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono la posizione dell'animale 
di un numero specificato di quadrati (es: -3, -5, -7). Gli ostacoli sono rappresentati da un dizionario 
che mappa le posizioni degli ostacoli sul percorso (chiave) ed i relativi effetti (valore). 
Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.

- Bonus:
Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione dell'animale 
di un numero determinato di quadrati (es: 5, 3, 10). I bonus sono rappresentati da un dizionario 
che mappa le posizioni dei bonus sul percorso (chiave) ed i relativi effetti (valore). 
Consentire agli animali di beneficiare pienamente dei bonus, ma non oltrepassare il traguardo.

'''

import random
'''#percorso: list[str] = ["_" for i in range(70)]

percorso: list[str] = [i for i in range(70)]
#percorso_2: list[str] = ["_" for i in range(70)] (?)
tartaruga: str = "T"
lepre: str = "H"
i_t: int = random.randint(1, 10)
i_h: int = random.randint(1, 10)
#posizione int per t e h (?)
#ciclo while

print("start")

if 1 <= i_t <= 5:
    print("passo veloce")
    if tartaruga not in percorso:
        percorso.remove(percorso[3])
        percorso.insert(3, tartaruga)

if 6 <= i_t <= 7:
    print("scivolata")
    if tartaruga not in percorso:
        pass

if 8 <= i_t <= 10:
    print("passo lento")
    if tartaruga not in percorso:
        percorso.remove(percorso[1])
        percorso.insert(1, tartaruga)




if 1 <= i_h <= 2:
    print("riposo")
    if lepre not in percorso:
        pass

if 3 <= i_h <= 4:
    print("grande balzo")
    if lepre not in percorso:
        percorso.remove(percorso[9])
        percorso.insert(9, lepre)

if i_h == 5:
    print("grande scivolata")
    if lepre not in percorso:
        pass

if 6 <= i_h <= 8:
    print("piccolo balzo")
    if lepre not in percorso:
        percorso.remove(percorso[1])
        percorso.insert(1, lepre)

if 9 <= i_h <= 10:
    print("piccola scivolata")
    if lepre not in percorso:
        pass

#print(percorso)'''
#global stamina
stamina_t: int = 100
stamina_h: int = 100

def mosse_della_tartarugha(posizione_t: int) -> int: #prova a mettere stamina prima di questa fun
    i: int = random.randint(1, 10)
    #stamina: int = 100
    global stamina_t
    if 1 <= i <= 5 and stamina_t >= 5:
        posizione_t += 3
        stamina_t -= 5 #5
    elif 6 <= i <= 7 and stamina_t >= 10:
        posizione_t -= 6
        stamina_t -= 10 #10
    elif 8 <= i <= 10 and stamina_t >= 3:
        posizione_t += 1
        stamina_t -= 3 #3
    else: 
        stamina_t += 10
        #pass

    while posizione_t < 1: #1
        posizione_t += 1
    
    return posizione_t

def mosse_della_lepre(posizione_h: int) -> int: #metti if se supera 100
    i: int = random.randint(1, 10)
    global stamina_h
    if 1 <= i <= 2:
        stamina_h += 10 #10
    elif 3 <= i <= 4 and stamina_h >= 15:
        posizione_h += 9
        stamina_h -= 15
    elif i == 5 and stamina_h >= 20:
        posizione_h -= 12
        stamina_h -= 20
    elif 6 <= i <= 8 and stamina_h >= 5:
        posizione_h += 1
        stamina_h -= 5
    elif 9 <= i <= 10 and stamina_h >= 8:
        posizione_h -= 2
        stamina_h -= 8

    if stamina_h > 100:
        stamina_h = 100

    while posizione_h < 1: #1
        posizione_h += 1

    return posizione_h

def gara() -> str:
    tartaruga: int = 1
    lepre:int = 1
    orlogio: int = 0
    clima = random.choice(["soleggiato", "pioggia"])
    time_clima: int = -1

    print("BANG !!!!! AND THEY'RE OFF !!!!!")

    while tartaruga < 70 and lepre < 70:
        percorso: list[str] = [i for i in range(70)]
        tartaruga: int = mosse_della_tartarugha(tartaruga)
        lepre: int = mosse_della_lepre(lepre)
        orlogio += 1
        time_clima += 1

        if time_clima == 10 and clima == "soleggiato":
            time_clima = 0
            clima = "pioggia"
        elif time_clima == 10 and clima == "pioggia":
            time_clima = 0
            clima = "soleggiato"

        if tartaruga == lepre and tartaruga < 70 and lepre < 70:
            percorso[tartaruga] = "OUCH!!!" #percorso[tartaruga - 1] = "OUCH!!!"

            print(percorso[tartaruga], "\n" + "-" * 30)
        elif tartaruga < 70 and lepre < 70:
            if clima == "soleggiato":
                percorso[tartaruga] = "T" #percorso[tartaruga - 1] = "T"
                percorso[lepre] = "H" #percorso[lepre - 1] = "H"
            elif clima == "pioggia":
                tartaruga -= 1
                lepre -= 2
                percorso[tartaruga] = "T" #percorso[tartaruga - 1] = "T"
                percorso[lepre] = "H" #percorso[lepre - 1] = "H"

            if tartaruga <= 1 and lepre <= 1: #prova a metterci anche l'uguale
                tartaruga = 1
                lepre = 1
                percorso[tartaruga] = "OUCH!!!" #percorso[tartaruga - 1] = "OUCH!!!"

                print(percorso[tartaruga], "\n" + "-" * 30)
            elif tartaruga < 1 and lepre > 1:
                percorso = [i for i in range(70)]
                tartaruga = 1
                percorso[tartaruga] = "T" #percorso[tartaruga - 1] = "T"
                percorso[lepre] = "H" #percorso[lepre - 1] = "H"
            elif lepre < 1 and tartaruga > 1: #lepre < 1 and tartaruga > 1:
                percorso = [i for i in range(70)]
                lepre = 1
                percorso[lepre] = "H" #percorso[lepre - 1] = "H"
                percorso[tartaruga] = "T" #percorso[tartaruga - 1] = "T"

            if tartaruga != 1 and lepre != 1 or tartaruga == 1 and lepre != 1 or tartaruga != 1 and lepre == 1: # and è il problema
                print("Clima:", clima, "Ticks:", time_clima) #
                print(*percorso, "\n" + "-" * 30)

    if tartaruga >= 70 and lepre >= 70:
        print("IT'S A TIE")
        print("Time:", orlogio)
    elif tartaruga >= 70:
        print("TORTOISE WINS! || VAY!!!")
        print("Time:", orlogio)
    else:
        print("HARE WINS || YUCH!!!")
        print("Time:", orlogio)

gara()



''' |\|+ |\|+(?)
time clima = 0
clima = solare # all'inizio
# un altra alternativa all'inizio il clima è lista con 
# str solare e pioggia e usi usa random.choice

nel while time clima+= 1
if time clima = 10 and clima = solare:
time clima = 0
clima = pioggia

elif time clima = 10 and clima = pioggia:
time clima = 0
clima = pioggia

if clima = solare:
tartaruga rimane uguale
lepre pure

elif clima = pioggia:
tartaruga - 1 # o forse è meglio tartaruga -=1
lepre - 2 # lepre -= 2

# forse si rischia di posizionare T o H prima di percorso[1]
# se succede prova a risolvere con mettere in "elif tartaruga < 70 and lepre < 70:":
#- si potrebbe mettere if tartaruga < 1: tartarugha = 1
#- stressa cosa per lepre
------------------------------
nel 2. energia o chiamata anche stamina (a inizio è uguale 100) deve esser 
presente nella funzion delle mosse della tartarugha e della lepre
metti ogni and negli if se stamina è > di 0 
(forse è meglio and stamina >= valore, valore varia a seconda quanta stamina richiede la mossa): 
se vero a energia sotrai punti a seconda della mossa

quando recuperano punti: 
-lepre: nel riposo recupera 10 stamina
-tartarugha: se gli if non vengono rispettati metti un else che da 10 di stamina

#forse metti while stamina < 0: stamina += 1

nel 3.
es:
key: posizione del percorso, value: di qunato riduce o aumenta la posizione dell'animale
ostacoli: dict = {15: -3 , 30: -5, 45: -7}
bonus: dict = {10: 5, 25 3:, 50: 10}

if animale == ostacoli[0] or ostacoli[1] or ostacoli[2]: # stessa ondizione con i bonus
animale += ostacoli[animale] # visto che i value di ostacoli sono negativi, in teoria va bene,
                             # ma nel dubbio controlla prima

#ho controllato, non sembra funzionare
#if alternativo che sembra funzionare:
if animale in ostacoli.keys(): #stessa condizione con i bonus
animale += ostacoli[animale] #nel pratica sembra che i valori negativi funzionano come previsto




# ho controlato la traccia, sembra che non ho dimenticato niente, nel dubbio ricontrolla a casa
'''
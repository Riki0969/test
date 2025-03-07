'''
print ("Hello World")

nome_studente=input("Ciao, come ti chiami? ")
print("Ciao " + nome_studente)
'''

'''
#Esercizio 1
#Questo codice deve chiedere in input il nome
#e il cognome e poi stampare per esempio:
#"Mi chiamo Iacopo Zerbetto"

nome = input("Dimmi il tuo Nome: ")
cognome = input("Dimmi il tuo Cognome: ")

print ("Mi chiamo " + nome + " " + cognome)
'''

#print()
#input()
#type()

#nome = "Vittoria"
#eta = 24
#altezza = 1.75
#print(type(nome))
#print(type(eta))
#print(type(altezza))

'''
arance_rick = 17

print("rick ha comprato: " + str(arance_rick) + " arance. ")
print(type(arance_rick))

arance_rick = str(arance_rick)
print(type(arance_rick))
'''


'''
prova1 = input("inserisci quello che vuoi : ")
print(type(prova1))
'''

'''
anno_corrente = 2024
anno_nascita = int(input("in che anno sei nato :"))


eta = anno_corrente - int(anno_nascita)

print("Hai " + str(eta) + " anni! ")
'''

'''
num1 = 10
num2 = 16

media = (num1 + num2)/ 2

print (media)
'''



#ES 1 scrivi un programma che chieda all'utente la base e l'altezza di un triangolo e scrivi l'area  triangolo

'''
base=input("Dammi la base: ")
altezza=input("Dammi la altezza: ")

area= int(base) * int(altezza)/2

print ("ecco a te l area" + str(area))

'''
'''
#ES 2 scrivi un programma un programma che chieda all'utente 3 numeri e scriva la media dei 3 numeri 


num1=input("Dammi primo numero: ")
num2=input("Dammi secondo numero:")
num3=input("Dammi terzo numero: ")

media = int(num1) + int(num2) + int(num3)/ 3

print ("ecco a te la media" + str(media))

'''
'''
count=0

while count < 5:
    print("Ciao")
    count = count + 1
    print(count)

'''
'''
#variabili
nome = "Riccardo"
eta = 18
#Liste
voti = [7, 8, 10, 4]
nomi = ["francesco," "serena," "jacopo"]

#stampa
print(voti)
print(voti[2] )

#aggiungi
citta = []
citta.append("Parigi")
citta.append("Firenze")
print(citta)

#nome_lista.append(nuovo_elemento)

'''
'''
num_voti =int(input("Qaunti voti vuoi inserire"))

count_voto = 1  #inizializzo il contatore
lista_voti = []  #inizializzo la lista di voti 

while count_voto <= num_voti:

    voto = int(input("dammi il voto n. " + str(count_voto) + ": "))
    lista_voti.append(voto) #aggiugo il voto alla lista 

    count_voto = count_voto + 1 #incremento il contatore

print(lista_voti)

print( len(lista_voti) )
'''


#esercizio1
'''
num = int(input("Inserisci numeri"))
count_numero = 1
lista_numero =[]
while count_numero <= num:
    numero = int(input("dammi il numero n. " + str(count_numero) + ": "))
    lista_numero.append(numero)

    count_numero = count_numero + 1

print(lista_numero)
print( len(lista_numero) )

'''
#Esercizio1
'''
numero = []
for a in range (2):
    numero.append(input("dammi un numero "))

print("I due numeri " + str(numero))
'''
#esercizio2
'''

film = str(input("Inserisci nome film"))
count_film = 1
lista_film =[]
while count_film <= 6:
    film = str(input("dammi il nome film n. " + str(count_film) + ": "))
    lista_film.append(film)

    count_film = count_film + 1

print(lista_film)
print( len(lista_film) )
'''
#Esercizio2
'''
lista_film = []
a = 
for a in range (6):
    lista_film.append(input("dammi dei film,"))

print("I sei film " + str(lista_film))
'''
#esercizio3
'''
lista = [1, 2, 3, 4, 5, 6]
count = 0
somma = 0
while count < len(lista):
    num = lista ( count)
    somma+= num
    count += 1
    media = (somma)/len(lista)
print (media)

'''
#esercizio3
'''
numeri = [9,10,8,4,6]

print(len(numeri))

somma = 0
'''
#eserizio3
'''
somma = 0
lista_numeri = [5, 6, 9, 6, 9, 10, 8]
for numero in lista_numeri:
    somma += numero
risultato= somma / len(lista_numeri)
print(risultato)
'''

                      
#esecizio5

'''


lista = [12, 45, 78, 34, 89, 23]
count = 0

while count < len(lista):

    numero = lista[count]

    if numero % 2 == 0:
        print ("il numero è pari" + str(numero))
        
    count = count + 1
  
'''
'''
numeri =  [12, 45, 78, 34, 89, 23]

for numero in numeri:
    if numero % 2 == 0:
        print(numero)
 '''       

#esercizio4
'''
lista_num = [8, 2, 10, 4, 6,]
num_max = lista_num[0]
count = 0
while count < len(lista_num):
    if lista_num[count] > num_max:
        num_max = lista_num[count]

    count = count + 1

print(" num max lista è " + str(num_max))
'''
#esercizio4
''''
lista_numeri = [8, 2, 10, 4, 6,]
num_max = 0 
for numero in lista_numeri:
   if numero> num_max:
       num_max = numero

print("il numero piu grande della lista è: " + str(num_max))
'''
      

#esercizio7

'''
lista_num = [8, 2, 10, 2, 8,]
lista_quadrati = []
count = 0

while count < len(lista_num):
    lista_quadrati.append(lista_num[count] * lista_num[count]
    count = count + 1
print(lista_quadrati)
'''
#esercizio ??
'''
dividendo = int(input("dammi il prino numero"))
divisore = int(input("dammi il secondo numero"))

somma = 0
count = 0
while somma < divisore:
    somma = somma + divisore
    if somma < dividendo:
        count = count + 1


    print("somma: " + str (somma) + ", count: "  + str(count))
resto = dividendo - (divisore * count)
print ("il risultato è" + str(count))

'''
#esercizio fibonacci


'''
num1 = 1
num2= 1

while num2 <=100:
    risultato = num1 + num2
    print(risultato)
    num1 = num2
    num2 = risultato 
'''

#while
'''

count = 0


while count < 5:            #con < 5 dici ci che la variabile fin quando è minore di 5 continua a ripetere
    print(str(count) +  " - ciao")   #con count stampi i numeri 
    count = count + 1  #aggiungi uno per far si che si aggiunga uno 

print("fine")



#liste
citta_preferite = ["Parigi", "Verona","Madrid"]

print(citta_preferite)

print(len(citta_preferite[0]))

pos = 0
while pos < len(citta_preferite):
    print("citta preferite: " + (citta_preferite[pos]))
    pos = pos + 1

#come aggiungere un elemento ad una lista

citta_preferite = ["Parigi", "Verona","Madrid"]

print(citta_preferite)
#citta_preferite.append(nuova_citta)
#citta_preferite[1] = "roma"
del citta_preferite[1]
print(citta_preferite)
'''

#for


'''
citta_preferite = ["Parigi", "Verona","Madrid"]

print("ciclo while")

count = 0
while count < len(citta_preferite):
    print (citta_preferite[count])
    count = count + 1

print()
print("ciclo for")
count = 0 
for citta in citta_preferite: #scorre tutti gli elementi della lista 
    print(citta)

'''
'''
num_start = int(input("da che numero vuoi iniziare a contare"))
num_max = int(input("fio a che numero vuoi contare"))
for num in range (num_start, num_max, 3):
    print(num + 1)


inserimento = input("vuoi rimanere nel ciclo")

while inserimento == "sii":
    inserimento = input("vuoi rimanere nel ciclo ??")

print("sei uscito dal ciclo ")
'''

'''
i = 0
pari = 0
while i < 5:
    num = int(input("Inserisci un numero: "))
    if num % 2 == 0:
        pari += 1
    i += 1
print("I numeri pari inseriti sono:", pari)

'''
'''
n = int(input("Inserisci un numero per calcolare il fattoriale: "))
fattoriale = 1
i = 1
while i <= n:
    fattoriale *= i
    i += 1
print("Il fattoriale di", n, "è:", fattoriale)

'''
#dizionari
'''
lista_numeri = [8, 15, 17, 47]

lista_docente = ["iacopo", 25 , "01/02/1999", "Caldiero", "Verona"]

diz_docente = {
    "nome": "iacopo",
    "eta" : 25,
    "data_nascita": "01/02/1999",
    "luogo_residenza": "Caldiero",
    "luogo_diploma": "Verona",
    "film_preferiti": ['harry potter, star wars, ritorno al futuro']
    }
'''
'''
print(diz_docente["eta"])

diz_docente["eta"] = diz_docente ["eta"] + 1
print(diz_docente["eta"])


for chiave in diz_docente:
    print(chiave, end=' - ')
    print(diz_docente[chiave])



'''
'''
diz = {}
diz["nome"] = "Elia"
print ( diz)
print()

diz ["nome"] = " Carlo"
print (diz) 



for film in diz_docente["film_preferiti"]:
    print(film)
'''
#eliminare qualcosa
'''
lista_numeri = [3, 5, 16]

print(lista_numeri)
del lista_numeri[1]
print(lista_numeri)

print (diz_libro)
del diz_libro["num_pagine"]
print(diz_libro)
'''
#Partendo da questo dizionario calcoalre la media dei voti per ogni maeteria e stamparla in questo modo:
#matematica :6,5
#storia :8
#....
#se ci sono piu o meno voti 
'''
registro= {
    "matematica" : [8, 4, 7, 7],
    "storia" : [8, 6, 10],
    "italiano" :[4, 9, 5, 7, 8, 8],
    "informatica" : [10, 10, 9, 10]
    }


for lezione in registro:
    voti = registro[lezione]
    media = sum(voti) / len(voti)
    print (media)

'''

#funzioni
'''
def saluta (nome):
    print("Ciao" + nome)

saluta("JIJI")
saluta("SEBA")
saluta("RIK")


nome_input = input("Ciao come ti chiami? ")
saluta(nome_input)
'''
'''
def disegnaQuadrato(lato, simbolo):
    for y in range(lato):
        for x in range(lato):
            print(simbolo, end="")
        print()

'''
'''
while True: 
    print("Cosa vuoi fare?")
    print("1 - quadrato bordi")
    print("2 - quadrato bordi")
    print("3 - solo X")
    azione = input("Azione:")
    lato_input = int(input("quanto grande il lato? "))
    simbolo_input = input("quale simbolo vuoi disegnare? ")

    if (azione == "1"):
        disegnaQuadratoPieno(lato_input, simbolo_input)
    elif(azione == "2"):
        disegnaQuadratoConBordi(lato_input, simbolo_input)
    elif(azione == "3"):
        disegnaSoloX(lato_input, simbolo_input)
    else:
            print("Azione non valida")
            print()

'''

#Ciao :)
#Scrivere un programma che simuli un registro elettronico
#utilizzando un dizionario di partenza con delle materie
# Registro con i voti
'''
registro = {
    "Italiano": [6, 8, 9],
    "Matematica": [5, 9, 7],
    "Storia": [8, 8, 9],
    "Informatica": [7, 6, 5, 9]
}

def mostra_voti():
    for materia in registro:
        print(f"{materia}: {registro[materia]}")

def aggiungi_voto():
    materia = input("Inserisci il nome della materia: ")
    if materia in registro:
        voto = int(input("Inserisci il voto da aggiungere: "))
        registro[materia].append(voto)
        print(f"Voto {voto} aggiunto a {materia}")
    else:
        print("Materia non trovata")

def calcola_media_materia():
    for materia in registro:
        voti = registro[materia]
        media = sum(voti) / len(voti)
        print(f"Media di {materia}: {media}")

# Funzione per calcolare la media totale
def calcola_media_totale():
    tutti_i_voti = []
    for materia in registro:
        for voto in registro[materia]:
            tutti_i_voti.append(voto) 
    media_totale = sum(tutti_i_voti) / len(tutti_i_voti)
    print(f"La tua media totale è: {media_totale}")

# Menu principale
def menu():
    print("1 - Mostra voti registro")
    print("2 - Aggiungi voto")
    print("3 - Calcola media per materia")
    print("4 - Calcola media totale")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        mostra_voti()
    elif scelta == "2":
        aggiungi_voto()
    elif scelta == "3":
        calcola_media_materia()
    elif scelta == "4":
        calcola_media_totale()
    else:
        print("Scelta non valida")

menu()

'''



















#il programma deve permetterci di fare le seguenti azioni:
# 1 mostra voti registro di tutte le materie
# 2 aggiungi voto ad una meteria 
# 3 calcola media di ogni materia
#  calcola la media totale di tutti i voti 


#il terzo dovra venire cosi:
'''
Italiano: 7.5
Matematica: 6.4
Storia: 4
Informatica: 9.9
'''
'''
while True:
    print("Cosa vuoi fare ?")
    print("1 - Voti materie")
    print("2 - Aggiungi voto ad una materia")
    print("3 - Calcola media di ogni materia")
    print("4 - Calcola media totale di tutti i voti
    azione = input("Azione:")
    
if ( 
'''


'''
while True: 
    print("Cosa vuoi fare?")
    print("1 - quadrato bordi")
    print("2 - quadrato bordi")
    print("3 - solo X")
    azione = input("Azione:")
    lato_input = int(input("quanto grande il lato? "))
    simbolo_input = input("quale simbolo vuoi disegnare? ")

    if (azione == "1"):
        disegnaQuadratoPieno(lato_input, simbolo_input)
    elif(azione == "2"):
        disegnaQuadratoConBordi(lato_input, simbolo_input)
    elif(azione == "3"):
        disegnaSoloX(lato_input, simbolo_input)
    else:
            print("Azione non valida")
            print()
'''



#fast sercizi
'''
def customLen():
    



lista = ["1", "2", "3", "4", ]
customLen(lista)
'''

'''
def calcolaMedia(lista_numeri):
    somma = 0
    for numero in lista_numeri :
        somma += numero 
        return somma
def calcolaSomma(lista_numeri):
    somma= calcolasomma(lista_numeri)
    media = somma / len(lista_numeri)
    return media 

numeri = [26, 17, 98]
risulatato_media = calcola_somma(numeri)
print(risulatato_Somma)
risulatato_media = calcola_media(numeri)
print(risulatato_Media)
'''

#Esercizi per natale
'''
nome=input("Come ti chiami ?")
print ("ciao"  + nome )
'''
#es2
'''
num1=input("Dammi primo numero")
num2=input("Dammi secondo numero")

somma = int(num1) + int(num2);
print(somma)
'''
#es3
'''
parola=input("dimmi la parola:")
print(len(parola))
print(type(parola))
'''
#es4
'''
temperatura=input("Dammi la temperatura")
float()


'''
#es5
'''
numero = int(input("Inserisci un numero: "))

if numero > 10:
    print("Il numero è maggiore di 10.")
else:
    print("Il numero non è maggiore di 10.")
'''
#es6
'''
numero=int(input("Dammi un numero:"))

if numero% 2 ==0:
    print("il numero è pari")
else:
    print("il numero è dispari")
'''
#es7
'''
numero = int(input("Inserisci un numero: "))

if numero > 0:
    print("Il numero è positivo.")
elif numero < 0:
    print("Il numero è negativo.")
else:
    print("Il numero è zero.")
'''
#es8
'''
voto = int(input("Inserisci un voto (da 0 a 100): "))

if voto >= 90:
    giudizio = "Ottimo"
elif 70 <= voto <= 89:
    giudizio = "Buono"
elif 50 <= voto <= 69:
    giudizio = "Sufficiente"
else:
    giudizio = "Insufficiente"


print("Giudizio:" , giudizio)
'''
#es9
'''
numero1= int(input("Inserisci il primo numero: "))
numero2= int(input("Inserisci il secondo numero: "))

if numero1 > numero2:
    print("Il numero è maggiore:", numero1)
elif numero2 > numero1:
    print("Il numero è maggiore:", numero2)
else:
    print("I numeri sono uguali ")
'''
#es10
'''
eta = int(input("Inserisci la tua eta (da 0 a 100): "))

if eta < 18 :
    risulta = "Minorenne"
elif 18>= eta <= 65:
    risulta = "Adulto"
elif eta > 65:
    risulta = "Anziano"
else:
    risulta = "Deceduto"


print("Sei un " + risulta)

'''

#es11
'''
numero = int(input("Inserisci un numero: "))


if numero % 3 == 0 and numero % 5 == 0:
    print("Multiplo di 3 e 5")
elif numero % 3 == 0:
    print("Multiplo di 3")
elif numero % 5 == 0:
    print("Multiplo di 5")
else:
    print("Non è un multiplo")
'''
#es12





#es 13


#es14

#es15

'''
count= 0 
while count < 11:            #con < 5 dici ci che la variabile fin quando è minore di 5 continua a ripetere
    print(str(count))   #con count stampi i numeri 
    count = count + 1  #aggiungi uno per far si che si aggiunga uno 
'''
#es16
'''
count= 2
while count <21:
    print(str(count))
    count = count + 2

'''
    
#es17
'''
parola = input("Inserisci una parola: ")

count= 0

while count< len(parola):  
    count += 1


print("Numero di caratteri:", count)
'''
#es18
'''
somma = 0
numero = 0

while numero <=10:
    somma +=numero  # Aggiunge il numero alla somma
    numero +=1   # Passa al numero successivo

print("La somma dei numeri da 1 a 10 è:" , somma)
'''

#es19
'''
parola = input("Inserisci una parola: ")
numero = int(input("Inserisci un numero: "))

contatore = 0

while contatore < numero:
    print(parola)
    contatore += 1  
'''
#es20
'''
numero = 1

while numero <= 10:
    risultato = 3 * numero  # Calcola il prodotto
    print(f"3 x {numero} = {risultato}")  # Stampa il risultato #la f prende il valore che c'è dentro le parentesi graffe 
    numero += 1  # Incrementa il contatore
'''
#es21
'''
somma = 0

numero = int(input("Inserisci un numero (0 per terminare): "))

while numero != 0:  #il ! è per dire diverso da 0 
    somma += numero
    numero = int(input("Inserisci un numero (0 per terminare): "))
    
print(f"La somma totale è: {somma}")
'''
#es22
'''
numero_segreto = 42

tentativi = 0

while True:
    tentativo = int(input("Indovina il numero segreto (tra 1 e 100): "))
    tentativi += 1

    if tentativo < numero_segreto:
        print("Troppo basso! Riprova.")
        elif tentativo > numero_segreto:
        print("Troppo alto! Riprova.")
    else:
        print(f"Congratulazioni! Hai indovinato il numero in {tentativi} tentativi.")
        break  
'''

#es23
'''
numeri_positivi = 0

while True:
    numero = int(input("Inserisci un numero (inserisci un numero negativo per terminare): "))
    
    if numero < 0:
        break  # Termina il ciclo se il numero è negativo
    
    numeri_positivi += 1 

print(f"Hai inserito {numeri_positivi} numeri positivi.")
'''

#es24
'''
numero = int(input("Inserisci un numero: "))


multiplo = numero

while multiplo <= 100:
    print(multiplo)
    multiplo += numero  
'''
#es25
'''
somma = 0
conteggio = 0

while True:
    numero = int(input("Inserisci un numero (0 per terminare): "))
    
    if numero == 0:
        break  # Interrompe il ciclo se l'utente inserisce 0
    
    somma += numero  
    conteggio += 1  

# Calcola la media se ci sono numeri inseriti
if conteggio > 0:
    media = somma / conteggio
    print("La media è:", media)
else:
    print("Non sono stati inseriti numeri.")
'''
#es26
'''
numero = int(input("Inserisci un numero per il conto alla rovescia: "))

# Esegue il conto alla rovescia fino a 0
while numero >= 0:
    print(numero)
    numero -= 1  # toglie il numero 
'''
#es27
'''
numero = int(input("Inserisci un numero intero positivo: "))

# Inizializza la variabile per il fattoriale
fattoriale = 1

# Verifica che il numero sia positivo
if numero < 0:
    print("Il numero deve essere positivo.")
else:
    # Calcola il fattoriale usando un ciclo while
    while numero > 1:
        fattoriale *= numero  # Moltiplica il fattoriale per il numero corrente
        numero -= 1  # Decrementa il numero di 1

    # Stampa il risultato
    print(f"Il fattoriale è: {fattoriale}")
'''
#es28
'''
# Usa un ciclo for per stampare i numeri da 1 a 10
for numero in range(1, 11):
    print(numero)
'''
#es29
'''
# Usa un ciclo for per stampare i quadrati dei numeri da 1 a 5
for numero in range(1, 6):
    quadrato = numero ** 2  # Calcola il quadrato del numero
    print("il quadrato è di:" ,  quadrato)
'''
#es30
'''
parola = input("Inserisci una parola: ")

# Chiede quante volte vuole stamparla
numero = int(input("Quante volte vuoi stampare la parola? "))

# Usa un ciclo for per stampare la parola il numero di volte richiesto
for _ in range(numero):
    print(parola)
'''
#es31
'''
somma = 0

# Usa un ciclo for per sommare i numeri da 1 a 10
for numero in range(1, 11):
    somma += numero  # Aggiunge il numero corrente alla somma

# Stampa la somma totale
print("La somma dei numeri da 1 a 10 è:", somma)
'''

#es32
'''
# Usa un ciclo for per stampare i numeri pari da 1 a 20
for numero in range(1, 21):
    if numero % 2 == 0:  # Controlla se il numero è pari
        print(numero)
'''
#es33
'''
contatore = 0

# Usa un ciclo for per verificare i numeri da 1 a 30
for numero in range(1, 31):
    if numero % 3 == 0:  # Verifica se il numero è divisibile per 3
        contatore += 1  # Incrementa il contatore

# Stampa il risultato
print(f"I numeri da 1 a 30 divisibili per 3 sono: {contatore}")
'''
#es34
'''
# Chiede all'utente di inserire un numero
n = int(input("Inserisci il numero di righe per il triangolo: "))

# Usa un ciclo for per stampare il triangolo
for i in range(1, n + 1):
    print('*' * i)  # Stampa i asterischi per la riga

'''
#es35
'''
numeri = [1, 2, 3, 4, 5]
print(numeri)
'''
#es36
'''
numeri = [1, 2, 3, 4, 5]

# Chiede all'utente di aggiungere un numero alla lista
numero = int(input("Inserisci un numero da aggiungere alla lista: "))

# Aggiunge il numero alla lista
numeri.append(numero)

print("Lista aggiornata:", numeri)
'''

#es37


#es38


#es39
'''
numeri = [3, 7, 12, 19, 25]

# Chiede all'utente di inserire un numero
numero_da_verificare = int(input("Inserisci un numero per verificare se è presente nella lista: "))

if numero_da_verificare in numeri:
    print(f"Il numero {numero_da_verificare} è presente nella lista.")
else:
    print(f"Il numero {numero_da_verificare} non è presente nella lista.")
'''

#es40
'''
numeri = []

# Chiede all'utente di inserire 5 numeri
for i in range(5):
    numero = int(input(f"Inserisci il {i + 1}° numero: "))
    numeri.append(numero)  # Aggiunge il numero alla lista

# Trova il valore massimo nella lista
massimo = max(numeri)

# Stampa il valore massimo
print(f"Il valore massimo inserito è: {massimo}")
'''
#es41
'''
# Crea un dizionario con alcune informazioni
persona = {
    "nome": "Alice",
    "età": 25,
    "città": "Roma"
}

# Stampa il dizionario
print(persona)
'''

#es42
'''
# Crea un dizionario vuoto
persona = {}

nome = input("Inserisci il tuo nome: ")

# Aggiunge la chiave "nome" con il valore inserito
persona["nome"] = nome

print(persona)
'''

#es43
'''
persona = {
    "nome": "Alice",
    "età": 25,
    "città": "Roma"
}

# Chiede all'utente quale chiave vuole cercare
chiave = input("Inserisci la chiave che vuoi cercare (nome, età, città): ")

# Verifica se la chiave esiste nel dizionario
if chiave in persona:
    # Stampa il valore associato alla chiave
    print(f"Il valore della chiave '{chiave}' è: {persona[chiave]}")
else:
    print(f"La chiave '{chiave}' non esiste nel dizionario.")
'''

#es44
'''
# Crea un dizionario con alcune informazioni
persona = {
    "nome": "Alice",
    "età": 25,
    "città": "Roma"
}

# Modifica il valore della chiave "nome"
persona["nome"] = "Marco"

# Stampa il dizionario aggiornato
print(persona)
'''

#es45
'''
# Crea un dizionario con alcune informazioni
persona = {
    "nome": "Alice",
    "età": 25,
    "città": "Roma"
}

# Chiede all'utente quale chiave rimuovere
chiave_da_rimuovere = input("Inserisci la chiave da rimuovere (nome, età, città): ")

# Verifica se la chiave esiste nel dizionario
if chiave_da_rimuovere in persona:
    # Rimuove l'elemento con la chiave specificata
    del persona[chiave_da_rimuovere]
    print(f"Elemento con chiave '{chiave_da_rimuovere}' rimosso.")
else:
    print(f"La chiave '{chiave_da_rimuovere}' non esiste nel dizionario.")


print(persona)
'''
#es46
'''
# Crea un dizionario con alcune informazioni
persona = {
    "nome": "Alice",
    "età": 25,
    "città": "Roma"
}

# Chiede all'utente di inserire una chiave da cercare
chiave_da_cercare = input("Inserisci la chiave da cercare (nome, età, città): ")

# Verifica se la chiave esiste nel dizionario
if chiave_da_cercare in persona:
    print(f"La chiave '{chiave_da_cercare}' esiste nel dizionario.")
else:
    print(f"La chiave '{chiave_da_cercare}' non esiste nel dizionario.")
'''
#es47
'''
# Crea un dizionario con almeno 3 chiavi
persona = {
    "nome": "Alice",
    "età": 25,
    "città": "Roma"
}

# Cicla attraverso il dizionario e stampa ciascuna chiave e il suo valore
for chiave, valore in persona.items():
    print(f"Chiave: {chiave}, Valore: {valore}")
'''
#es48
'''
# Crea due dizionari con alcune chiavi comuni

dizionario1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dizionario2 = {
    "a": 5,
    "b": 15,
    "d": 25
}

# Crea un nuovo dizionario per contenere i risultati della somma
somma_dizionari = {}

# Cicla attraverso le chiavi del primo dizionario
for chiave in dizionario1:
    if chiave in dizionario2:
        # Somma i valori per le chiavi comuni
        somma_dizionari[chiave] = dizionario1[chiave] + dizionario2
'''

#class
'''
def chiediDatiPG(tipo_pg):
    diz_personaggio = {}
    print("### " + tipo_pg + " ###")
    diz_personaggio["nome"] = input("Come si chiama il personaggio? ")
    diz_personaggio["classe"] = input("Qual è la classe del personaggio? ")
    diz_personaggio["attacco"] = int(input("Quanto attacco ha il personaggio? "))
    diz_personaggio["vita"] = int(input("Quanta vita ha il personaggio? "))
    return diz_personaggio

class Personaggio:
    def __init__(self, nome, classe, attacco, vita, pozioni):
        self.nome = nome
        self.classe = classe
        self.attacco = attacco
        self.vita = vita
        self.vita_max = vita
        self.pozioni = pozioni

    def info(self):
        print("Nome: " + self.nome)
        print("Classe: " + self.classe)
        print("Attacco: " + str(self.attacco))
        print("Vita: " + str(self.vita) + "/" + str(self.vita_max))
        print("Qta Pozioni: " + str(self.pozioni))
        print()

    def attacca(self, nemico):
        nemico.vita = nemico.vita - self.attacco
        
        if nemico.vita > 0:
            print(self.nome + " ha attaccato " + nemico.nome + " e ora "
              + nemico.nome + " ha " + str(nemico.vita) + " di vita!")
        else:
            print("Il/La " + nemico.classe + " " + nemico.nome
                  + " è stat* sconfitt*...ora è negli inferi!")
            nemico.vita = 0
        print()

    def siCura(self):
        if self.pozioni > 0:
            if self.vita + 30 >  self.vita_max:
                self.vita = self.vita_max
            else:
                self.vita = self.vita + 30
            print(self.nome + " si è curat*! Queste sono le sue statistiche ora:")
            self.pozioni = self.pozioni - 1
            self.info()
        
# dati protagonista
diz_protagonista = chiediDatiPG("Protagonista")
protagonista = Personaggio(diz_protagonista["nome"],
                           diz_protagonista["classe"],
                           diz_protagonista["attacco"],
                           diz_protagonista["vita"],
                           3)


diz_nemico1 = chiediDatiPG("Nemico")
nemico1 = Personaggio(diz_nemico1["nome"],
                      diz_nemico1["classe"],
                      diz_nemico1["attacco"],
                      diz_nemico1["vita"],
                      0)

while True:
    print("Cosa vuoi fare?")
    print("info - Mostra informazioni sul protagonista")
    print("attacca - Attacca il nemico")
    print("difendi - Il nemico attacca te")
    print("cura - Usa una pozione per curarti")
    print("esci - Termina il gioco")

    azione = input("Azione: ")

    if azione == "info":
        protagonista.info()

    elif azione == "attacca":
        protagonista.attacca(nemico1)
        if nemico1.vita <= 0:  # Controllo che la vita sia minore o uguale a 0 
            print("Hai vinto il combattimento!") # Dopo l'attacco, verrà controllato se i tuoi punti vita sono scesi a zero o sotto. 
            break

    elif azione == "difendi":
        nemico1.attacca(protagonista)
        if protagonista.vita <= 0:  # Controllo che la vita sia minore o uguale a 0
            print("Hai perso il combattimento")
            break

    elif azione == "cura":
        protagonista.siCura()

    elif azione == "esci":
        print("Hai terminato il gioco")
        break

    else:
        print("Azione non valida")



'''
def chiediDatiPG(tipo_pg):
    diz_personaggio = {}
    print("### " + tipo_pg + " ###")
    diz_personaggio["nome"] = input("Come si chiama il personaggio? ")
    diz_personaggio["classe"] = input("Qual è la classe del personaggio? ")
    diz_personaggio["attacco"] = int(input("Quanto attacco ha il personaggio? "))
    diz_personaggio["vita"] = int(input("Quanta vita ha il personaggio? "))
    return diz_personaggio

class Personaggio:
    def __init__(self, nome, classe, attacco, vita, pozioni):
        self.nome = nome
        self.classe = classe
        self.attacco = attacco
        self.vita = vita
        self.vita_max = vita
        self.pozioni = pozioni
        self.oro = 50  # Aggiunto oro iniziale

    def info(self):
        print("Nome: " + self.nome)
        print("Classe: " + self.classe)
        print("Attacco: " + str(self.attacco))
        print("Vita: " + str(self.vita) + "/" + str(self.vita_max))
        print("Qta Pozioni: " + str(self.pozioni))
        print("Oro: " + str(self.oro))
        print()

    def attacca(self, nemico):
        nemico.vita = nemico.vita - self.attacco
        
        if nemico.vita > 0:
            print(self.nome + " ha attaccato " + nemico.nome + " e ora " + nemico.nome + " ha " + str(nemico.vita) + " di vita!")
        else:
            print("Il/La " + nemico.classe + " " + nemico.nome + " è stat* sconfitt*...ora torna nel gulag !")
            nemico.vita = 0
            self.oro += 20  # Guadagno oro dopo aver sconfitto un nemico
        print()

    def siCura(self):
        if self.pozioni > 0:
            if self.vita + 30 >  self.vita_max:
                self.vita = self.vita_max
            else:
                self.vita = self.vita + 30
            print(self.nome + " si è curat*! Queste sono le sue statistiche ora:")
            self.pozioni = self.pozioni - 1
            self.info()
        else:
            print("Non hai più pozioni!")

    def difendi(self, nemico):
        danno = nemico.attacco // 2  # Riduce il danno alla metà
        self.vita -= danno
        print(self.nome + " si è difeso e ha subito solo " + str(danno) + " danni!")
        if self.vita <= 0:
            print(self.nome + " è stato sconfitto!")

    def compraPozione(self):
        costo = 10
        if self.oro >= costo:
            self.oro -= costo
            self.pozioni += 1
            print("Hai comprato una pozione! Ora hai " + str(self.pozioni) + " pozioni e " + str(self.oro) + " oro rimanente.")
        else:
            print("Non hai abbastanza oro per comprare una pozione!")

# dati protagonista
diz_protagonista = chiediDatiPG("Protagonista")
protagonista = Personaggio(diz_protagonista["nome"],
                           diz_protagonista["classe"],
                           diz_protagonista["attacco"],
                           diz_protagonista["vita"],
                           3)


diz_nemico1 = chiediDatiPG("Nemico")
nemico1 = Personaggio(diz_nemico1["nome"],
                      diz_nemico1["classe"],
                      diz_nemico1["attacco"],
                      diz_nemico1["vita"],
                      0)

while True:
    print("Cosa vuoi fare?")
    print("info - Mostra informazioni sul protagonista")
    print("attacca - Attacca il nemico")
    print("difendi - Il nemico attacca te")
    print("cura - Usa una pozione per curarti")
    print("negozio - Compra una pozione (10 oro)")
    print("esci - Termina il gioco")

    azione = input("Azione: ")

    if azione == "info":
        protagonista.info()

    elif azione == "attacca":
        protagonista.attacca(nemico1)
        if nemico1.vita <= 0:  # Controllo che la vita sia minore o uguale a 0 
            print("Hai vinto il combattimento!")
            break

    elif azione == "difendi":
        protagonista.difendi(nemico1)
        if protagonista.vita <= 0:  # Controllo che la vita sia minore o uguale a 0
            print("Hai perso il combattimento")
            break

    elif azione == "cura":
        protagonista.siCura()

    elif azione == "negozio":
        protagonista.compraPozione()

    elif azione == "esci":
        print("Hai terminato il gioco")
        break

    else:
        print("Azione non valida")


        
        

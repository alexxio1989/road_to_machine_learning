# -----------------------------------------------------
# Demo: Input/Output in Python
# -----------------------------------------------------

# 1. Lettura di input da tastiera con la funzione input()
#    Ricorda: qualunque valore ritorna sempre come stringa!
nome = input("Inserisci il tuo nome: ")

# 2. Stampa di base con print()
#    Possiamo passare più argomenti, che verranno separati da uno spazio di default.
print("Ciao", nome, "!")

# 3. Uso di print() con f-string per formattazione più elegante
#    Le f-string (f"testo {variabile}") permettono di inserire variabili
#    direttamente dentro la stringa.
print(f"È un piacere conoscerti, {nome}.")

# 4. Conversione di tipo dopo input (da stringa a intero)
eta_str = input("Inserisci la tua età: ")
# Proviamo a convertire in int. Attenzione: se l'utente non digita un numero valido,
# genererà un errore ValueError.
eta = int(eta_str)

# 5. Stampa con .format() (un metodo alternativo alle f-string)
print("Tra 5 anni avrai {} anni!".format(eta + 5))

# 6. Dimostrazione di parametri aggiuntivi di print()
#    - sep: specifica il separatore tra gli argomenti
#    - end: specifica la stringa da stampare alla fine (di default è "\n", il newline)
print("Questo", "testo", "è", "separato", "da", "trattini", sep="-", end=" *** ")
print("e continua sulla stessa riga!")

# 7. Chiediamo un altro input, per mostrare come leggere dati numerici
#    e fare operazioni prima di stampare il risultato
numero1_str = input("\nDigita un numero: ")
numero2_str = input("Digita un altro numero: ")

# Converto le stringhe in numeri interi
numero1 = int(numero1_str)
numero2 = int(numero2_str)

somma = numero1 + numero2
prodotto = numero1 * numero2

# Stampo i risultati con diversi approcci
print("\n*** RISULTATI ***")
print("La somma di", numero1, "e", numero2, "è:", somma)
print("Il prodotto è:", prodotto)

# Oppure uso una f-string per essere più conciso
print(f"La somma di {numero1} e {numero2} è: {somma}")
print(f"Il prodotto è: {prodotto}")

# 8. Uso dell'operatore 'in' con stringhe
#    (Mostra come l’input, essendo string, si possa gestire con operazioni su stringhe)
frase = input("\nScrivi una frase a piacere: ")
parola_cercata = input("Quale parola vuoi cercare nella frase? ")

if parola_cercata in frase:
    print(f"La parola '{parola_cercata}' è presente nella frase.")
else:
    print(f"La parola '{parola_cercata}' non è presente nella frase.")

# Fine del demo!
print("\n--- FINE DEMO ---")

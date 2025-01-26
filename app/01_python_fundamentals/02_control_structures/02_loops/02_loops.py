"""
SCOPO DEL CODICE:
Questo script mostra come funzionano i cicli in Python, con esempi essenziali per `for`, `while` e cicli condizionati.
Inoltre, include spiegazioni su `break`, `continue`, e `else` nei cicli, con particolare attenzione ai cicli for condizionati
(list comprehension con filtri) e allo scope delle variabili nei loop.

ARGOMENTO:
- Ciclo `for` e iterazioni su sequenze
- Cicli for condizionati (list comprehension)
- Ciclo `while` con condizione dinamica
- Uso di `break`, `continue` e `else` nei cicli
- Scope delle variabili nei loop
"""

# -----------------------------------------------------
# SEZIONE A: CICLO FOR
# -----------------------------------------------------

# Iterazione su una sequenza semplice (lista)
print("ESEMPIO 1: Iterazione su una lista")
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(f"Numero: {numero}")
print()

# Iterazione con range()
print("ESEMPIO 2: Iterazione con range()")
for i in range(1, 6):  # Da 1 a 5
    print(f"Iterazione: {i}")
print()

# Iterazione su un dizionario
print("ESEMPIO 3: Iterazione su un dizionario")
dati = {"nome": "Anna", "età": 28}
for chiave, valore in dati.items():
    print(f"{chiave}: {valore}")
print()

# -----------------------------------------------------
# SEZIONE B: CICLI FOR CONDIZIONATI
# -----------------------------------------------------

# Creazione di una lista di numeri pari con list comprehension
print("ESEMPIO 4: Ciclo for condizionato (list comprehension)")
numeri = [1, 2, 3, 4, 5, 6]
numeri_pari = [n for n in numeri if n % 2 == 0]  # Solo i numeri pari
print("Numeri originali:", numeri)
print("Numeri pari:", numeri_pari)

# Creazione di una lista con operazioni (quadrati dei numeri dispari)
numeri_dispari_quadrati = [n**2 for n in numeri if n % 2 != 0]
print("Quadrati dei numeri dispari:", numeri_dispari_quadrati)
print()

# -----------------------------------------------------
# SEZIONE C: CICLO WHILE
# -----------------------------------------------------

# Ciclo while con condizione dinamica
print("ESEMPIO 5: Ciclo while con condizione dinamica")
numero = -1
while numero < 0:
    numero = int(input("Inserisci un numero positivo: "))
print(f"Hai inserito un numero valido: {numero}")
print()

# -----------------------------------------------------
# SEZIONE D: BREAK, CONTINUE ED ELSE NEI CICLI
# -----------------------------------------------------

# Uso di break per interrompere un ciclo
print("ESEMPIO 6: Uso di break")
for numero in range(1, 10):
    if numero == 5:
        print("Interruzione del ciclo: trovato 5")
        break
    print(f"Numero: {numero}")
print()

# Uso di continue per saltare un'iterazione
print("ESEMPIO 7: Uso di continue")
for numero in range(1, 6):
    if numero % 2 == 0:
        continue  # Salta i numeri pari
    print(f"Numero dispari: {numero}")
print()

# Ciclo con else
print("ESEMPIO 8: Ciclo con else")
for numero in range(1, 6):
    if numero == 0:  # Condizione che non si verifica
        break
else:
    print("Il ciclo è terminato senza interruzioni.")
print()

# -----------------------------------------------------
# SEZIONE E: SCOPE DELLE VARIABILI NEI CICLI
# -----------------------------------------------------

print("ESEMPIO 9: Scope delle variabili nei cicli")
for x in range(3):
    variabile_locale = f"Valore di x: {x}"
    print(variabile_locale)

# Anche fuori dal ciclo, x e variabile_locale sono accessibili
print("Fuori dal ciclo for:")
print(f"x = {x}")
print(f"variabile_locale = {variabile_locale}")
print()

# -----------------------------------------------------
# NOTE FINALI
# -----------------------------------------------------
"""
In Python:
- Il ciclo `for` è ideale per iterare su sequenze (liste, range, dizionari).
- I cicli for condizionati (list comprehension) permettono di creare liste filtrate o trasformate in una riga.
- Il ciclo `while` è utile per ripetizioni basate su una condizione dinamica.
- `break` interrompe il ciclo, `continue` salta l'iterazione corrente, ed `else` esegue un'azione se il ciclo termina normalmente.
- I cicli non creano uno scope separato: le variabili definite nei loop sono visibili nel contesto esterno.
"""

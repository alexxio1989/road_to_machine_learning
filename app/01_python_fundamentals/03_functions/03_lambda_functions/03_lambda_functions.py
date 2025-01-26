"""
SCOPO DEL CODICE:
Questo script esplora le funzioni lambda in Python, che sono funzioni anonime definite con una sintassi compatta.
Viene mostrato come creare e utilizzare funzioni lambda in scenari semplici e complessi.
Inoltre, vengono illustrati gli ambiti (scope) delle variabili nelle lambda.

ARGOMENTO:
- Cos'è una funzione lambda
- Creazione e utilizzo di funzioni lambda
- Funzioni lambda con più parametri
- Uso di lambda con funzioni integrate (`map`, `filter`, `sorted`)
- Lambda all'interno di funzioni
- Scope delle variabili nelle lambda
"""

# -----------------------------------------------------
# SEZIONE A: COS'È UNA FUNZIONE LAMBDA
# -----------------------------------------------------

# 1. Una funzione normale per sommare due numeri
def somma_normale(a, b):
    return a + b

# Equivalente con una funzione lambda
somma_lambda = lambda a, b: a + b

print("ESEMPIO 1: Funzione lambda base")
print(f"Somma normale (3, 5): {somma_normale(3, 5)}")
print(f"Somma lambda (3, 5): {somma_lambda(3, 5)}")
print()

# -----------------------------------------------------
# SEZIONE B: LAMBDA CON PARAMETRI E SCENARI PRATICI
# -----------------------------------------------------

# 2. Lambda per calcolare il quadrato di un numero
quadrato = lambda x: x**2

print("ESEMPIO 2: Lambda per calcolare il quadrato")
print(f"Quadrato di 4: {quadrato(4)}")
print(f"Quadrato di 7: {quadrato(7)}")
print()

# 3. Lambda con condizione (pari o dispari)
pari_dispari = lambda x: "pari" if x % 2 == 0 else "dispari"

print("ESEMPIO 3: Lambda con condizione")
print(f"5 è: {pari_dispari(5)}")
print(f"8 è: {pari_dispari(8)}")
print()

# -----------------------------------------------------
# SEZIONE C: USO DI LAMBDA CON FUNZIONI INTEGRATE
# -----------------------------------------------------

# 4. Uso di lambda con `map` (applicare una funzione a ogni elemento di una lista)
numeri = [1, 2, 3, 4, 5]
numeri_doppi = list(map(lambda x: x * 2, numeri))

print("ESEMPIO 4: Lambda con map")
print("Numeri originali:", numeri)
print("Numeri doppiati:", numeri_doppi)
print()

# 5. Uso di lambda con `filter` (filtrare elementi da una lista)
numeri_pari = list(filter(lambda x: x % 2 == 0, numeri))

print("ESEMPIO 5: Lambda con filter")
print("Numeri originali:", numeri)
print("Numeri pari:", numeri_pari)
print()

# 6. Uso di lambda con `sorted` (ordinare una lista di tuple)
persone = [("Anna", 30), ("Marco", 25), ("Luca", 35)]
ordinato_per_età = sorted(persone, key=lambda persona: persona[1])

print("ESEMPIO 6: Lambda con sorted")
print("Persone ordinate per età:", ordinato_per_età)
print()

# -----------------------------------------------------
# SEZIONE D: LAMBDA ALL'INTERNO DI FUNZIONI
# -----------------------------------------------------

# 7. Una funzione che restituisce una lambda per calcolare il moltiplicatore
def crea_moltiplicatore(n):
    """
    Restituisce una funzione lambda che moltiplica il valore di input per 'n'.
    :param n: Fattore di moltiplicazione
    :return: Funzione lambda
    """
    return lambda x: x * n

print("ESEMPIO 7: Lambda generata da una funzione")
doppio = crea_moltiplicatore(2)
triplo = crea_moltiplicatore(3)
print(f"Doppio di 5: {doppio(5)}")
print(f"Triplo di 5: {triplo(5)}")
print()

# -----------------------------------------------------
# SEZIONE E: SCOPE DELLE VARIABILI NELLE LAMBDA
# -----------------------------------------------------

# 8. Scope delle variabili
def somma_con_offset(offset):
    """
    Restituisce una lambda che somma un valore a un offset fisso.
    """
    return lambda x: x + offset

print("ESEMPIO 8: Scope delle variabili nelle lambda")
somma_10 = somma_con_offset(10)
somma_20 = somma_con_offset(20)
print(f"5 + 10 (offset): {somma_10(5)}")
print(f"5 + 20 (offset): {somma_20(5)}")
print()

# -----------------------------------------------------
# SEZIONE F: ESEMPI COMPLESSI
# -----------------------------------------------------

# 9. Calcolo di una tabella moltiplicativa usando lambda
print("ESEMPIO 9: Tabella moltiplicativa con lambda")
tabella = [[(lambda x, y: x * y)(x, y) for y in range(1, 6)] for x in range(1, 6)]
for riga in tabella:
    print(riga)
print()

# 10. Filtrare e trasformare una lista complessa
print("ESEMPIO 10: Filtrare e trasformare con lambda")
dati = [
    {"nome": "Anna", "età": 30},
    {"nome": "Marco", "età": 25},
    {"nome": "Luca", "età": 35},
]
# Filtrare persone con età > 28 e ottenere solo i nomi
nomi_filtrati = list(map(lambda persona: persona["nome"], filter(lambda p: p["età"] > 28, dati)))
print("Nomi filtrati (età > 28):", nomi_filtrati)
print()

# -----------------------------------------------------
# NOTE FINALI
# -----------------------------------------------------
"""
- Le funzioni lambda sono utili per definire funzioni compatte e anonime.
- Sono ideali per l'uso con funzioni integrate come `map`, `filter` e `sorted`.
- Scope: le lambda possono catturare variabili dallo scope esterno, come negli esempi con `offset`.
- Non sono adatte per logiche complesse: in questi casi, usa funzioni normali con `def`.
"""

"""
SCOPO DEL CODICE:
Questo script dimostra i vari operatori in Python (aritmetici, di confronto, logici, membership, identità, bitwise, assegnamento),
fornendo esempi pratici. Viene anche evidenziato il concetto di "scope" delle variabili per sottolineare la differenza
fra variabili globali e variabili locali.

ARGOMENTO:
- Operatori aritmetici (+, -, *, /, //, %, **)
- Operatori di confronto (<, >, <=, >=, ==, !=)
- Operatori logici (and, or, not)
- Operatori di membership (in, not in)
- Operatori di identità (is, is not)
- Operatori bitwise (&, |, ^, ~, <<, >>)
- Operatori di assegnamento combinata (+=, -=, *=, ecc.)
- Concetto di scope (variabili globali vs variabili locali a una funzione)
"""

# -----------------------------------------------------
# SEZIONE A: OPERATORI ARITMETICI E DI CONFRONTO
# -----------------------------------------------------

# Variabili globali
a = 10
b = 3

print("=== OPERATORI ARITMETICI ===")
print(f"a = {a}, b = {b}")
print("Somma (a + b) =", a + b)           # 13
print("Differenza (a - b) =", a - b)      # 7
print("Prodotto (a * b) =", a * b)        # 30
print("Divisione (a / b) =", a / b)       # 3.3333...
print("Divisione intera (a // b) =", a // b)  # 3
print("Resto (a % b) =", a % b)           # 1
print("Potenza (a ** b) =", a ** b)       # 1000
print()

print("=== OPERATORI DI CONFRONTO ===")
print(f"{a} > {b}  ->", a > b)    # True
print(f"{a} >= {b} ->", a >= b)   # True
print(f"{a} < {b}  ->", a < b)    # False
print(f"{a} <= {b} ->", a <= b)   # False
print(f"{a} == {b} ->", a == b)   # False
print(f"{a} != {b} ->", a != b)   # True
print()

# -----------------------------------------------------
# SEZIONE B: OPERATORI LOGICI
# -----------------------------------------------------
print("=== OPERATORI LOGICI ===")
val1 = True
val2 = False

print("val1 =", val1, ", val2 =", val2)
print("val1 AND val2 =", val1 and val2)  # False
print("val1 OR val2  =", val1 or val2)   # True
print("NOT val1      =", not val1)       # False
print()

# Esempio combinato con operatori di confronto
eta = 25
print("Controllo se 18 <= eta <= 30:", (eta >= 18 and eta <= 30))  # True
print()

# -----------------------------------------------------
# SEZIONE C: OPERATORI DI MEMBERSHIP E IDENTITÀ
# -----------------------------------------------------
print("=== OPERATORI DI MEMBERSHIP ===")
testo = "Benvenuto in Python!"
print("testo:", testo)
print("'Python' in testo?  ->", "Python" in testo)    # True
print("'Java' in testo?    ->", "Java" in testo)      # False
print()

print("=== OPERATORI DI IDENTITÀ ===")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print("lista1 =", lista1, "\nlista2 =", lista2, "\nlista3 =", lista3)
print("lista1 == lista2 ->", lista1 == lista2)   # True (stesso contenuto)
print("lista1 is lista2 ->", lista1 is lista2)   # False (oggetti diversi in memoria)
print("lista1 is lista3 ->", lista1 is lista3)   # True  (stesso identico oggetto)
print()

# -----------------------------------------------------
# SEZIONE D: OPERATORI BITWISE
# -----------------------------------------------------

"""
OPERATORE BITWISE (A LIVELLO DI BIT):
In Python, gli operatori bitwise lavorano direttamente sulla rappresentazione binaria dei numeri interi (base 2).
Quando applichi un operatore bitwise, ogni bit dei numeri viene confrontato o manipolato indipendentemente.

Ecco i principali operatori bitwise e la loro funzione:

1. AND (&):
   - Prende due operandi e confronta ciascun bit corrispondente.
   - Restituisce 1 in quella posizione se entrambi i bit sono 1, altrimenti 0.

2. OR (|):
   - Restituisce 1 se almeno uno dei due bit corrispondenti è 1, altrimenti 0.

3. XOR (^):
   - Restituisce 1 se i bit corrispondenti sono diversi (1-0 o 0-1), altrimenti 0 se sono uguali (1-1 o 0-0).

4. NOT (~):
   - Inverte i bit del numero, calcolando il "complemento" (negazione bit a bit).
   - In Python, ~x corrisponde a -x-1 (in notazione complemento a due).

5. SHIFT A SINISTRA (<<):
   - Sposta tutti i bit di un numero a sinistra di un dato numero di posizioni.
   - Ogni shift a sinistra moltiplica di fatto il valore per 2 alla n (dove n è il numero di posizioni di shift).

6. SHIFT A DESTRA (>>):
   - Sposta tutti i bit di un numero a destra di un dato numero di posizioni.
   - Ogni shift a destra esegue, di fatto, una divisione intera per 2 alla n (dove n è il numero di posizioni di shift).
   - In Python, se il numero è positivo, viene riempito con zeri (shift logico), se negativo, con 1 (shift aritmetico).

Questi operatori sono utili in diversi casi come l’elaborazione a basso livello, la manipolazione di maschere (bitmask),
operazioni di crittografia, compressione, e ottimizzazioni di performance laddove lavorare sui bit sia vantaggioso.
"""

print("=== OPERATORI BITWISE ===")
c = 5   # binario: 0101
d = 3   # binario: 0011
print(f"c = {c} (bin: {c:04b}), d = {d} (bin: {d:04b})")
print("c & d  -> AND bit a bit =", c & d,  f"(bin: {(c & d):04b})")   # 1  (0001)
print("c | d  -> OR bit a bit  =", c | d,  f"(bin: {(c | d):04b})")   # 7  (0111)
print("c ^ d  -> XOR bit a bit =", c ^ d,  f"(bin: {(c ^ d):04b})")   # 6  (0110)
print("~c     -> NOT c =", ~c,             f"(bin: {~c:08b})")        # -6 (in complement)
print("c << 1 -> shift left di 1 =", c << 1, f"(bin: {(c << 1):04b})") # 10 (1010)
print("d >> 1 -> shift right di 1 =", d >> 1, f"(bin: {(d >> 1):04b})")# 1  (0001)
print()

# -----------------------------------------------------
# SEZIONE E: OPERATORI DI ASSEGNAMENTO COMBINATA
# -----------------------------------------------------
print("=== OPERATORI DI ASSEGNAMENTO COMBINATA ===")
numero = 10
print("numero =", numero)

numero += 5   # numero = numero + 5
print("numero += 5  ->", numero)

numero -= 3   # numero = numero - 3
print("numero -= 3  ->", numero)

numero *= 2   # numero = numero * 2
print("numero *= 2  ->", numero)

numero //= 4  # numero = numero // 4
print("numero //= 4 ->", numero)

numero **= 2  # numero = numero ** 2
print("numero **= 2 ->", numero)
print()

# -----------------------------------------------------
# SEZIONE F: ESEMPIO DI SCOPE (VARIABILI GLOBALI VS LOCALI)
# -----------------------------------------------------
variabile_globale = 100

def esempio_scope():
    """
    Questa funzione crea una variabile locale (variabile_locale).
    Accede anche a variabile_globale (in lettura).
    """
    variabile_locale = 5
    print("Dentro la funzione esempio_scope():")
    print("variabile_globale =", variabile_globale)  # accesso in sola lettura
    print("variabile_locale  =", variabile_locale)

    # Possibile modifica della variabile globale tramite 'global' (non consigliato in genere):
    # global variabile_globale
    # variabile_globale = 999
    print()

esempio_scope()

# Fuori dalla funzione non possiamo accedere a 'variabile_locale'
# perché è definita nello scope locale di esempio_scope().
# print(variabile_locale)  # -> NameError se scommentato

print("Fuori dalla funzione:")
print("variabile_globale =", variabile_globale)  # Ancora 100 (se non abbiamo usato 'global')
print("--- FINE DEMO ---")

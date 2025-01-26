"""
SCOPO DEL CODICE:
Questo script illustra il concetto di ricorsione in Python. La ricorsione è una tecnica in cui una funzione richiama sé stessa per risolvere
un problema, suddividendolo in sottoproblemi più semplici. Vengono trattati esempi di base, casi pratici e scenari complessi.

ARGOMENTO:
- Cos'è la ricorsione
- Struttura base di una funzione ricorsiva
- Caso base e caso ricorsivo
- Esempi pratici (fattoriale, somma, sequenza di Fibonacci)
- Esempi avanzati (ricorsione su strutture nidificate)
"""

# -----------------------------------------------------
# SEZIONE A: COS'È LA RICORSIONE
# -----------------------------------------------------

# La ricorsione consiste nel dividere un problema in sottoproblemi più semplici. Una funzione ricorsiva deve sempre:
# 1. Definire un caso base che interrompa la ricorsione.
# 2. Avere un caso ricorsivo in cui la funzione richiama sé stessa.

# -----------------------------------------------------
# SEZIONE B: ESEMPI BASE DI RICORSIONE
# -----------------------------------------------------

# 1. Calcolo del fattoriale di un numero (n!)
def fattoriale(n):
    """
    Calcola il fattoriale di un numero n utilizzando la ricorsione.
    Caso base: n == 0 -> ritorna 1.
    Caso ricorsivo: n * fattoriale(n - 1).
    """
    if n == 0:
        return 1  # Caso base
    return n * fattoriale(n - 1)  # Caso ricorsivo

print("ESEMPIO 1: Fattoriale")
print(f"Fattoriale di 5: {fattoriale(5)}")  # 5! = 120
print()

# 2. Somma dei numeri da 1 a n
def somma(n):
    """
    Calcola la somma dei numeri da 1 a n utilizzando la ricorsione.
    Caso base: n == 0 -> ritorna 0.
    Caso ricorsivo: n + somma(n - 1).
    """
    if n == 0:
        return 0  # Caso base
    return n + somma(n - 1)  # Caso ricorsivo

print("ESEMPIO 2: Somma dei numeri")
print(f"Somma dei numeri da 1 a 5: {somma(5)}")  # 1 + 2 + 3 + 4 + 5 = 15
print()

# -----------------------------------------------------
# SEZIONE C: RICORSIONE SU SEQUENZE
# -----------------------------------------------------

# 3. Calcolo della sequenza di Fibonacci
def fibonacci(n):
    """
    Calcola l'n-esimo numero della sequenza di Fibonacci.
    Caso base: n == 0 o n == 1.
    Caso ricorsivo: fibonacci(n-1) + fibonacci(n-2).
    """
    if n == 0:
        return 0  # Caso base
    if n == 1:
        return 1  # Caso base
    return fibonacci(n - 1) + fibonacci(n - 2)  # Caso ricorsivo

print("ESEMPIO 3: Fibonacci")
print(f"Decimo numero della sequenza di Fibonacci: {fibonacci(10)}")  # 55
print()

# -----------------------------------------------------
# SEZIONE D: ESEMPI AVANZATI DI RICORSIONE
# -----------------------------------------------------

# 4. Ricorsione su una struttura nidificata (somma di una lista annidata)
def somma_lista_nidificata(lista):
    """
    Calcola la somma degli elementi di una lista, che può contenere sottoliste.
    Caso base: lista vuota -> ritorna 0.
    Caso ricorsivo: somma il primo elemento (o ricorri se è una lista) e richiama sulla coda.
    """
    if not lista:
        return 0  # Caso base: lista vuota
    primo, *resto = lista
    if isinstance(primo, list):
        return somma_lista_nidificata(primo) + somma_lista_nidificata(resto)
    return primo + somma_lista_nidificata(resto)

print("ESEMPIO 4: Somma di una lista nidificata")
lista_nidificata = [1, [2, [3, 4]], 5]
print(f"Somma della lista nidificata {lista_nidificata}: {somma_lista_nidificata(lista_nidificata)}")
print()

# 5. Ricorsione con una funzione che calcola tutte le combinazioni di una lista
def combina(lista):
    """
    Genera tutte le combinazioni di una lista di elementi.
    Caso base: lista vuota -> ritorna una lista contenente una lista vuota.
    Caso ricorsivo: include ed esclude il primo elemento.
    """
    if not lista:
        return [[]]  # Caso base
    primo, *resto = lista
    combinazioni_resto = combina(resto)
    return combinazioni_resto + [[primo] + combinazione for combinazione in combinazioni_resto]

print("ESEMPIO 5: Combinazioni di una lista")
lista = [1, 2, 3]
print(f"Combinazioni della lista {lista}: {combina(lista)}")
print()

# -----------------------------------------------------
# SEZIONE E: SCOPE E LIMITI DELLA RICORSIONE
# -----------------------------------------------------

# 6. Scope e stack ricorsivo
def stampa_discendente(n):
    """
    Stampa i numeri da n a 1 utilizzando la ricorsione.
    Mostra come le chiamate ricorsive usano lo stack.
    """
    if n == 0:
        return  # Caso base
    print(f"Entrata ricorsione: n = {n}")
    stampa_discendente(n - 1)  # Chiamata ricorsiva
    print(f"Uscita ricorsione: n = {n}")

print("ESEMPIO 6: Traccia delle chiamate ricorsive")
stampa_discendente(3)
print()

# -----------------------------------------------------
# NOTE FINALI
# -----------------------------------------------------
"""
- La ricorsione è utile per problemi che possono essere suddivisi in sottoproblemi simili al problema originale.
- Ogni funzione ricorsiva deve avere un caso base per evitare chiamate infinite (StackOverflowError).
- La ricorsione è utile ma non sempre ottimale: in alcuni casi, algoritmi iterativi sono più efficienti.
- Python ha un limite di profondità dello stack ricorsivo (controllabile con `sys.getrecursionlimit()`).
"""

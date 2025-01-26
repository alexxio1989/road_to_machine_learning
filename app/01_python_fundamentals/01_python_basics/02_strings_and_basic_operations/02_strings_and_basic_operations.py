"""
SCOPO DEL CODICE:
Questo script mostra i concetti fondamentali sulle STRINGS in Python e le operazioni basilari
(es. concatenazione, slicing, formattazione, appartenenza, ecc.).
Inoltre, include un esempio di "scope" delle variabili, ovvero l'ambito in cui esse sono
visibili o utilizzabili (scope globale o locale a una funzione).

ARGOMENTO:
- Creazione e manipolazione delle stringhe
- Operazioni comuni (concatenazione, ripetizione, slicing, membership)
- Formattazione delle stringhe (f-string)
- Operazioni aritmetiche di base per mostrare la sintassi
- Scope: differenza tra variabili globali e variabili locali
"""

# -----------------------------------------------------
# SEZIONE A: STRINGHE - CREAZIONE E MANIPOLAZIONE
# -----------------------------------------------------

# 1. Creazione di stringhe con apici singoli e doppi
testo_singolo = 'Ciao'
testo_doppio = "Mondo"
print("testo_singolo:", testo_singolo, "->", type(testo_singolo))
print("testo_doppio:", testo_doppio, "->", type(testo_doppio))
print()

# 2. Concatenazione di stringhe (operatore +) e ripetizione (operatore *)
concatenato = testo_singolo + " " + testo_doppio + "!"
ripetuto = testo_singolo * 3
print("Concatenazione:", concatenato)
print("Ripetizione:", ripetuto)
print()

# 3. Indici e slicing
#    - gli indici partono da 0 (prima lettera)
#    - gli indici negativi contano da destra (-1 è l'ultimo carattere)
frase = "Python"
prima_lettera = frase[0]    # 'P'
ultima_lettera = frase[-1]  # 'n'
sottostringa = frase[1:4]   # 'yth' (include index 1, 2, 3)

print("frase:", frase)
print("Prima lettera:", prima_lettera)
print("Ultima lettera:", ultima_lettera)
print("Sottostringa [1:4]:", sottostringa)
print()

# 4. Membership: verificare se una sottostringa è contenuta in un'altra
testo = "Benvenuto nel mondo di Python"
print("testo:", testo)
print("'Python' in testo?", "Python" in testo)  # True
print("'Ciao' in testo?", "Ciao" in testo)      # False
print()

# 5. Formattazione di stringhe con f-string
nome = "Anna"
eta = 28
saluto = f"Ciao {nome}, hai {eta} anni!"
print(saluto)
print()

# -----------------------------------------------------
# SEZIONE B: OPERAZIONI BASILARI (SUI NUMERI)
# -----------------------------------------------------
a = 7
b = 3

print(f"a = {a}, b = {b}")
print("Somma (a + b) =", a + b)          # 10
print("Differenza (a - b) =", a - b)     # 4
print("Prodotto (a * b) =", a * b)       # 21
print("Divisione (a / b) =", a / b)      # 2.3333...
print("Divisione intera (a // b) =", a // b)  # 2
print("Resto (a % b) =", a % b)          # 1
print("Potenza (a ** b) =", a ** b)      # 7^3 = 343
print()

# -----------------------------------------------------
# SEZIONE C: SCOPE DELLE VARIABILI (GLOBALE VS LOCALE)
# -----------------------------------------------------

# Variabile GLOBALE
messaggio_globale = "Sono definita nel corpo principale del codice."

def dimostra_scope():
    """
    Questa funzione definisce una variabile LOCALE (visibile solo all'interno della funzione).
    """
    messaggio_locale = "Sono una variabile locale, esisto solo qui dentro!"
    print("All'interno di dimostra_scope():")
    print("messaggio_globale:", messaggio_globale)  # Accessibile qui perché è globale
    print("messaggio_locale:", messaggio_locale)
    print()

# Chiamando la funzione si può usare la variabile globale, ma non viceversa.
dimostra_scope()

# Se provassimo a stampare messaggio_locale fuori dalla funzione, otterremmo un NameError
# print(messaggio_locale)  # <-- Questo genererebbe un errore, perché messaggio_locale è LOCALE

print("All'esterno della funzione dimostra_scope():")
print("messaggio_globale è ancora accessibile:", messaggio_globale)
print("--- FINE DEMO ---")

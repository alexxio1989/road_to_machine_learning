"""
SCOPO DEL CODICE:
Questo script illustra come funzionano le strutture di controllo condizionali in Python, in particolare if, elif, ed else.
Mostra esempi di base, annidamento (nested if) e un cenno allo scope delle variabili (anche se in Python i blocchi
if/else non creano scope separati come succede in altri linguaggi: le variabili definite in un blocco if restano
visibili nel medesimo contesto di funzione o globale).

ARGOMENTO:
- Sintassi if, elif, else
- Flussi condizionali multipli
- Esempi di condizioni e azioni diverse
- Scope: in Python, blocchi if/else non introducono un nuovo scope (le variabili sono ancora accessibili nello stesso contesto)
"""

# -----------------------------------------------------
# ESEMPIO 1: if - else di base
# -----------------------------------------------------
valore = 5

if valore > 0:
    print("ESEMPIO 1: 'valore' è positivo.")
else:
    print("ESEMPIO 1: 'valore' NON è positivo (quindi è zero o negativo).")

print()

# -----------------------------------------------------
# ESEMPIO 2: if - elif - else
# -----------------------------------------------------
# Permette di gestire più casi in cascata.
# Esempio: verifichiamo lo stato di un numero (negativo, zero, positivo).

numero = 0

if numero < 0:
    print("ESEMPIO 2: 'numero' è negativo.")
elif numero == 0:
    print("ESEMPIO 2: 'numero' è zero.")
else:
    print("ESEMPIO 2: 'numero' è positivo.")

print()

# -----------------------------------------------------
# ESEMPIO 3: Nested if (if annidati)
# -----------------------------------------------------
# Possiamo annidare i blocchi di if per creare logiche più complesse.
# Per esempio, creiamo un mini-simulatore di età e patente di guida.

eta = 20
ha_patente = True

if eta >= 18:
    print("ESEMPIO 3: Sei maggiorenne.")

    if ha_patente:
        print("Puoi guidare un'auto!")
    else:
        print("Hai l'età giusta ma non la patente.")
else:
    print("Sei ancora minorenne, niente patente!")

print()

# -----------------------------------------------------
# ESEMPIO 4: Uso di una variabile definita all'interno di un if
# -----------------------------------------------------
# In Python NON esiste lo scope di blocco come in C/C++/Java.
# Le variabili create all'interno di un if (ma non all'interno di una funzione)
# rimangono nello scope corrente, cioè globale (in questo script) o della funzione in cui ci si trova.

condizione = True

if condizione:
    variabile_in_if = "Creo questa variabile dentro l'if"
    print("ESEMPIO 4: condizione è True, variabile_in_if creata.")
else:
    # Se la condizione fosse False, potremmo definire la variabile qui.
    # In un contesto reale, se non la definissimo altrove, darebbe errore di NameError se provassimo ad usarla fuori.
    variabile_in_if = "Creo questa variabile dentro l'else"

# Qui fuori dall'if, la variabile_in_if è comunque accessibile!
print("variabile_in_if =", variabile_in_if)
print()

# -----------------------------------------------------
# ESEMPIO 5: if con più condizioni (e operatori logici)
# -----------------------------------------------------
# Controlliamo se un numero è compreso in un range.
# e.g. se "x" è tra 10 e 20, e se è pure dispari.

x = 15
if x >= 10 and x <= 20:
    if x % 2 != 0:
        print(f"ESEMPIO 5: {x} è compreso tra 10 e 20 ed è dispari.")
    else:
        print(f"ESEMPIO 5: {x} è compreso tra 10 e 20 ed è pari.")
else:
    print(f"ESEMPIO 5: {x} non è compreso tra 10 e 20.")

print()

# -----------------------------------------------------
# NOTE SU SCOPE IN PYTHON
# -----------------------------------------------------
# - Le variabili definite nel corpo principale del file appartengono allo scope globale del modulo.
# - Le variabili definite dentro una funzione sono locali a quella funzione, a meno che non vengano
#   dichiarate global tramite la keyword 'global' (pratica sconsigliata).
# - I blocchi if/else/for/while NON creano scope a sé stante: se definisci una variabile dentro un if
#   (sempre all'interno della stessa funzione o del modulo), rimane visibile dopo la chiusura del blocco.
# - Esempio:

variabile_globale = "Sono globale"

def funzione_demo():
    # Scope locale della funzione
    var_locale = "Sono dentro funzione_demo()"
    if True:
        var_in_if = "Definita in un blocco if, ma sempre nel contesto funzione_demo()"
        print(var_in_if)

    # Fuori dall'if ma dentro la funzione, var_in_if è ancora accessibile
    print(var_in_if)
    print(var_locale)

funzione_demo()
# print(var_locale)    # -> darebbe errore NameError, perché var_locale è locale a funzione_demo()

print("\n--- FINE DEMO ---")

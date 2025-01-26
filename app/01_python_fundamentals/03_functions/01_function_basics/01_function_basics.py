"""
SCOPO DEL CODICE:
Questo script spiega i concetti fondamentali delle funzioni in Python (function_basics).
Vengono illustrati:
- Come definire una funzione
- Come utilizzare parametri e valori di ritorno
- Differenza tra funzioni senza e con parametri
- Esempi di funzioni semplici e complesse
- Scope delle variabili all'interno delle funzioni (locale vs globale)

ARGOMENTO:
- Cos'è una funzione e perché usarla
- Funzioni senza parametri
- Funzioni con parametri (posizionali e opzionali)
- Funzioni con valori di ritorno (`return`)
- Scope delle variabili nelle funzioni
"""

# -----------------------------------------------------
# SEZIONE A: DEFINIZIONE DI FUNZIONI
# -----------------------------------------------------

# 1. Funzione senza parametri e senza valore di ritorno
def saluta():
    """
    Stampa un messaggio di saluto.
    """
    print("Ciao! Benvenuto al corso di Python.")

# Chiamata della funzione
print("ESEMPIO 1: Funzione senza parametri")
saluta()
print()

# 2. Funzione con parametri
def saluta_persona(nome):
    """
    Stampa un saluto personalizzato con il nome fornito.
    :param nome: Il nome della persona da salutare
    """
    print(f"Ciao, {nome}! Piacere di conoscerti.")

# Chiamata della funzione con diversi parametri
print("ESEMPIO 2: Funzione con parametri")
saluta_persona("Anna")
saluta_persona("Marco")
print()

# 3. Funzione con parametri opzionali (valori di default)
def saluta_con_ruolo(nome, ruolo="studente"):
    """
    Stampa un messaggio di saluto includendo il ruolo, con valore predefinito 'studente'.
    :param nome: Il nome della persona
    :param ruolo: Il ruolo della persona (opzionale)
    """
    print(f"Ciao, {nome}! Sei un {ruolo}.")

print("ESEMPIO 3: Funzione con parametri opzionali")
saluta_con_ruolo("Luca")  # Usa il valore di default per 'ruolo'
saluta_con_ruolo("Marta", "insegnante")  # Sovrascrive il valore di default
print()

# -----------------------------------------------------
# SEZIONE B: VALORI DI RITORNO
# -----------------------------------------------------

# 4. Funzione che restituisce un valore
def somma(a, b):
    """
    Calcola la somma di due numeri e restituisce il risultato.
    :param a: Primo numero
    :param b: Secondo numero
    :return: Somma di a e b
    """
    return a + b

# Utilizzo del valore restituito
print("ESEMPIO 4: Funzione con valore di ritorno")
risultato = somma(3, 5)
print(f"La somma di 3 e 5 è: {risultato}")
print()

# -----------------------------------------------------
# SEZIONE C: FUNZIONI COMPLESSE
# -----------------------------------------------------

# 5. Funzione complessa con controllo dei parametri
def calcola_media(*numeri):
    """
    Calcola la media di un numero arbitrario di valori.
    :param numeri: Una lista di numeri
    :return: La media aritmetica dei numeri
    """
    if len(numeri) == 0:
        return None  # Nessun numero fornito
    somma_totale = sum(numeri)
    return somma_totale / len(numeri)

print("ESEMPIO 5: Funzione complessa (calcolo media)")
media = calcola_media(5, 10, 15)
print(f"La media di 5, 10 e 15 è: {media}")
media_vuota = calcola_media()
print(f"Media con lista vuota: {media_vuota}")
print()

# -----------------------------------------------------
# SEZIONE D: SCOPE DELLE VARIABILI
# -----------------------------------------------------

# 6. Scope delle variabili (locale vs globale)
variabile_globale = "Sono globale"

def dimostra_scope():
    """
    Dimostra la differenza tra variabili locali e globali.
    """
    variabile_locale = "Sono locale"  # Definita solo dentro questa funzione
    print("Dentro la funzione:")
    print("Variabile locale:", variabile_locale)
    print("Variabile globale:", variabile_globale)

dimostra_scope()

# Qui, la variabile_locale non è più accessibile:
# print(variabile_locale)  # Questo genererebbe un NameError

print("\nFuori dalla funzione:")
print("Variabile globale:", variabile_globale)
print()

# -----------------------------------------------------
# SEZIONE E: ESEMPI COMPLESSI CON COMBINAZIONI
# -----------------------------------------------------

# 7. Funzione con parametri obbligatori, opzionali e restituzione di un dizionario
def descrivi_persona(nome, età, città="non specificata"):
    """
    Crea una descrizione di una persona in formato dizionario.
    :param nome: Nome della persona
    :param età: Età della persona
    :param città: Città della persona (opzionale)
    :return: Dizionario contenente i dettagli
    """
    return {
        "nome": nome,
        "età": età,
        "città": città
    }

print("ESEMPIO 7: Funzione avanzata con restituzione di dizionario")
persona = descrivi_persona("Alice", 30, "Roma")
print("Dati persona:", persona)
persona_default = descrivi_persona("Giovanni", 25)
print("Dati persona con valore di default:", persona_default)
print()

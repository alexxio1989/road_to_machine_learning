"""
SCOPO DEL CODICE:
Questo script esplora il concetto di parametri (arguments) e valori di ritorno (return) nelle funzioni Python.
Vengono illustrati:
- Tipi di parametri (posizionali, opzionali, arbitrari e keyword arguments)
- Valori di ritorno (semplici e complessi)
- Esempi avanzati con funzioni di ordine superiore e combinazioni di parametri
- Scope delle variabili nei parametri e nei valori di ritorno

ARGOMENTO:
- Tipi di argomenti: posizionali, con valori di default, arbitrari (`*args`, `**kwargs`)
- Come restituire valori dalle funzioni con `return`
- Restituire più valori (tuple, liste, dizionari)
"""

# -----------------------------------------------------
# SEZIONE A: ARGOMENTI POSIZIONALI E DI DEFAULT
# -----------------------------------------------------

# 1. Funzione con argomenti posizionali
def somma(a, b):
    """
    Restituisce la somma di due numeri.
    :param a: Primo numero
    :param b: Secondo numero
    :return: Somma di a e b
    """
    return a + b

print("ESEMPIO 1: Argomenti posizionali")
print(f"Somma di 3 e 5: {somma(3, 5)}")
print()

# 2. Funzione con argomenti opzionali (default)
def saluta(nome, messaggio="Ciao"):
    """
    Stampa un messaggio personalizzato, con un valore di default per il messaggio.
    :param nome: Nome della persona da salutare
    :param messaggio: Messaggio di saluto (opzionale)
    """
    print(f"{messaggio}, {nome}!")

print("ESEMPIO 2: Argomenti con valori di default")
saluta("Anna")
saluta("Marco", "Benvenuto")
print()

# -----------------------------------------------------
# SEZIONE B: ARGOMENTI ARBITRARI (`*args`, `**kwargs`)
# -----------------------------------------------------

# 3. Funzione con un numero arbitrario di argomenti (`*args`)
def somma_arbitraria(*numeri):
    """
    Somma un numero arbitrario di valori.
    :param numeri: Un elenco di numeri
    :return: La somma dei numeri forniti
    """
    return sum(numeri)

print("ESEMPIO 3: Argomenti arbitrari (*args)")
print(f"Somma di 1, 2, 3: {somma_arbitraria(1, 2, 3)}")
print(f"Somma di 4, 5, 6, 7: {somma_arbitraria(4, 5, 6, 7)}")
print()

# 4. Funzione con keyword arguments arbitrari (`**kwargs`)
def descrivi_persona(**dati):
    """
    Stampa i dettagli di una persona utilizzando keyword arguments.
    :param dati: Dettagli forniti come chiave-valore
    """
    for chiave, valore in dati.items():
        print(f"{chiave}: {valore}")

print("ESEMPIO 4: Keyword arguments arbitrari (**kwargs)")
descrivi_persona(nome="Luca", età=30, città="Roma")
print()

# -----------------------------------------------------
# SEZIONE C: VALORI DI RITORNO
# -----------------------------------------------------

# 5. Funzione che restituisce un solo valore
def quadrato(n):
    """
    Restituisce il quadrato di un numero.
    :param n: Numero da elevare al quadrato
    :return: Quadrato di n
    """
    return n**2

print("ESEMPIO 5: Valore di ritorno singolo")
risultato = quadrato(4)
print(f"Quadrato di 4: {risultato}")
print()

# 6. Funzione che restituisce più valori (tuple)
def operazioni_base(a, b):
    """
    Restituisce somma, differenza e prodotto di due numeri.
    :param a: Primo numero
    :param b: Secondo numero
    :return: Tuple (somma, differenza, prodotto)
    """
    somma = a + b
    differenza = a - b
    prodotto = a * b
    return somma, differenza, prodotto

print("ESEMPIO 6: Valori multipli (tuple)")
s, d, p = operazioni_base(7, 3)
print(f"Somma: {s}, Differenza: {d}, Prodotto: {p}")
print()

# 7. Funzione che restituisce un dizionario
def analizza_lista(lista):
    """
    Analizza una lista e restituisce un dizionario con statistiche.
    :param lista: Lista di numeri
    :return: Dizionario con somma, lunghezza e media
    """
    somma = sum(lista)
    lunghezza = len(lista)
    media = somma / lunghezza if lunghezza > 0 else 0
    return {"somma": somma, "lunghezza": lunghezza, "media": media}

print("ESEMPIO 7: Valore complesso (dizionario)")
statistiche = analizza_lista([1, 2, 3, 4, 5])
print("Statistiche:", statistiche)
print()

# -----------------------------------------------------
# SEZIONE D: COMBINAZIONI COMPLESSIVE
# -----------------------------------------------------

# 8. Funzione complessa con combinazione di parametri
def calcola_prezzo_totale(prezzo, *quantità, sconto=0, **dettagli):
    """
    Calcola il prezzo totale basato sul prezzo unitario, quantità e sconto.
    :param prezzo: Prezzo unitario
    :param quantità: Quantità multipla (arbitraria)
    :param sconto: Percentuale di sconto (default: 0)
    :param dettagli: Dettagli extra (ad esempio, nome prodotto)
    :return: Prezzo totale dopo lo sconto
    """
    totale_quantità = sum(quantità)
    totale = prezzo * totale_quantità
    totale_scontato = totale * (1 - sconto / 100)
    print("Dettagli:", dettagli)
    return totale_scontato

print("ESEMPIO 8: Funzione complessa con combinazione di parametri")
totale = calcola_prezzo_totale(10, 2, 3, sconto=10, prodotto="T-shirt")
print(f"Prezzo totale scontato: {totale}")
print()

# -----------------------------------------------------
# NOTE FINALI
# -----------------------------------------------------
"""
- Argomenti posizionali vengono passati nella posizione definita.
- Argomenti opzionali usano valori di default quando non specificati.
- `*args` consente di passare un numero arbitrario di argomenti come tuple.
- `**kwargs` consente di passare argomenti arbitrari come coppie chiave-valore.
- Valori di ritorno possono essere semplici o complessi (tuple, dizionari).
"""

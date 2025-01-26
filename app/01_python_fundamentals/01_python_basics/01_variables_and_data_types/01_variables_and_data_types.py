"""
SCOPO DEL CODICE:
Questo script illustra i concetti fondamentali relativi alle variabili e ai tipi di dato (data types) in Python.
Mostra come creare e usare variabili di diversi tipi (int, float, bool, string, None), come funziona la tipizzazione dinamica
e fornisce esempi pratici di conversione dei tipi (casting). Inoltre, include best practice per la scelta dei nomi delle variabili.
"""

# -------------------------------------------------
# ESEMPIO: Variabili e Tipi di Dato in Python
# -------------------------------------------------

# 1. Assegnazione di una variabile intera (int)
numero_intero = 10
print("numero_intero =", numero_intero, "->", type(numero_intero))

# 2. Assegnazione di una variabile a virgola mobile (float)
valore_decimale = 3.14
print("valore_decimale =", valore_decimale, "->", type(valore_decimale))

# 3. Variabili booleane (bool)
condizione_vera = True
condizione_falsa = False
print("condizione_vera =", condizione_vera, "->", type(condizione_vera))
print("condizione_falsa =", condizione_falsa, "->", type(condizione_falsa))

# 4. Stringhe (str)
#    In Python si possono usare sia le virgolette singole che doppie
testo_singolo = 'Ciao'
testo_doppio = "Mondo"
print("testo_singolo =", testo_singolo, "->", type(testo_singolo))
print("testo_doppio =", testo_doppio, "->", type(testo_doppio))

# Concatenazione di stringhe
testo_concatenato = testo_singolo + " " + testo_doppio + "!"
print("testo_concatenato =", testo_concatenato)

# 5. Valore speciale None (assenza di valore)
nessun_valore = None
print("nessun_valore =", nessun_valore, "->", type(nessun_valore))

# 6. Tipizzazione dinamica
#    In Python, una variabile può cambiare tipo durante l'esecuzione
variabile_dinamica = 100
print("variabile_dinamica =", variabile_dinamica, "->", type(variabile_dinamica))
variabile_dinamica = "Ora sono una stringa!"
print("variabile_dinamica =", variabile_dinamica, "->", type(variabile_dinamica))

# 7. Casting (conversione di tipo)
numero_testo = "42"
numero_int = int(numero_testo)       # Converte "42" in 42 (int)
print("numero_int =", numero_int, "->", type(numero_int))

float_testo = "3.99"
numero_float = float(float_testo)    # Converte "3.99" in 3.99 (float)
print("numero_float =", numero_float, "->", type(numero_float))

bool_testo = "True"
valore_bool = bool(bool_testo)       # Converte la stringa "True" in True (bool)
print("valore_bool =", valore_bool, "->", type(valore_bool))

# 8. Best practice: Naming delle variabili
#    In Python si usa lo stile snake_case (lettere minuscole e underscore)
numero_di_studenti = 30
media_punteggi = 87.5
print("numero_di_studenti =", numero_di_studenti)
print("media_punteggi =", media_punteggi)

# 9. Spiegazione di scope (concetto base)
#    - Lo "scope" di una variabile indica l'ambito in cui è visibile/utilizzabile.
#    - In uno script semplice come questo, tutte le variabili sono nello scope globale del file.
#    - All'interno di funzioni, le variabili create sarebbero locali alla funzione.
#    - Esempio rapido:

def esempio_scope():
    variabile_locale = "Sono visibile solo qui dentro."
    print("Dentro la funzione:", variabile_locale)

esempio_scope()
# print(variabile_locale)  # Se provi a scommentare, darà errore NameError

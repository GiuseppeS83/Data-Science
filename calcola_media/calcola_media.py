def calcola_media(lista_numeri):
    """
    Calcola la media di una lista di numeri.
    
    Parametri:
    lista_numeri (list): Lista di numeri (interi o float)
    
    Ritorna:
    float: La media dei numeri, oppure None se la lista è vuota
    """
    if not lista_numeri:  # Controlla se la lista è vuota
        return None
    somma = sum(lista_numeri)
    quantita = len(lista_numeri)
    media = somma / quantita
    return media

# Esempio di utilizzo
numeri = [10, 20, 30, 40, 50]
print("La media è:", calcola_media(numeri))
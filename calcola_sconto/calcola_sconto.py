def calcola_sconto(prezzo, percentuale_sconto):
    sconto = prezzo * percentuale_sconto / 100
    prezzo_finale = prezzo - sconto
    return prezzo_finale
print(calcola_sconto(100, 15))
# Calcolatore Media Numerica (Python)

Questo script Python fornisce una funzione semplice e riutilizzabile per calcolare la media aritmetica di una lista di numeri.

## 📋 Descrizione

Il file `calcola_media.py` contiene la funzione `calcola_media()`, progettata per:
* Ricevere una lista di numeri (interi o float).
* Verificare se la lista è vuota per evitare errori di runtime.
* Restituire la media calcolata o `None` in caso di lista priva di elementi.

## ⚙️ Funzionamento Tecnico

La media viene calcolata seguendo la logica:
1. **Somma**: Si ottiene il totale degli elementi con `sum(lista_numeri)`.
2. **Conteggio**: Si determina il numero di elementi con `len(lista_numeri)`.
3. **Divisione**: Si divide la somma per la quantità.

## 🚀 Guida all'uso

### Prerequisiti
* Python 3.x installato.

### Esempio Rapido
Nello script è già presente un esempio di utilizzo predefinito:
```python
numeri = [10, 20, 30, 40, 50]
print("La media è:", calcola_media(numeri))
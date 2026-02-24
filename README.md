# 🛍️ Gestione Prodotto in Python

Un semplice script Python che crea e gestisce un **prodotto**
utilizzando un dizionario (`dict`).\
Il programma memorizza le informazioni principali di un prodotto e le
stampa a schermo.

------------------------------------------------------------------------

## 📌 Descrizione

Il file `dizionario.py` definisce un prodotto con le seguenti
caratteristiche:

-   🏷️ **Nome**
-   💰 **Prezzo**
-   🗂️ **Categoria**

Successivamente, il programma stampa i valori associati a ciascuna
chiave del dizionario.

------------------------------------------------------------------------

## 🧠 Codice

``` python
prodotto = {
    "nome": "Laptop",
    "prezzo": 800,
    "categoria": "lettronica"
}

print(prodotto["nome"])
print(prodotto["prezzo"])
print(prodotto["categoria"])
```

------------------------------------------------------------------------

## 🚀 Come eseguire il programma

1.  Assicurati di avere Python 3 installato.
2.  Salva il file come `dizionario.py`
3.  Esegui il comando:

``` bash
python dizionario.py
```

Oppure:

``` bash
python3 dizionario.py
```

------------------------------------------------------------------------

## 🖥️ Output atteso

    Laptop
    800
    lettronica

------------------------------------------------------------------------

## 📂 Struttura del progetto

    📁 progetto
     ├── dizionario.py
     └── README.md

------------------------------------------------------------------------

## 📚 Concetti utilizzati

-   Dizionari (`dict`) in Python
-   Accesso ai valori tramite chiave
-   Stampa a schermo con `print()`

------------------------------------------------------------------------

## 🔮 Possibili miglioramenti

-   Aggiungere input da utente
-   Gestire più prodotti in una lista
-   Calcolare sconti
-   Salvare i dati su file JSON
-   Creare un piccolo gestionale prodotti

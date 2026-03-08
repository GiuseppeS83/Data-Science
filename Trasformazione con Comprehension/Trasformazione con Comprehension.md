# Esercizio Python – List Comprehension

## Obiettivo
Dato un elenco di numeri, creare una nuova lista che contenga il **quadrato di ogni numero** utilizzando una **list comprehension**.

## Dati di partenza
Lista originale:

numeri = [1, 2, 3, 4, 5]

## Soluzione

quadrati = [n * n for n in numeri]

## Spiegazione

- `for n in numeri` scorre ogni elemento della lista `numeri`
- `n * n` calcola il quadrato di ogni numero
- la list comprehension crea automaticamente una nuova lista chiamata `quadrati`

## Risultato atteso

[1, 4, 9, 16, 25]

## Concetti utilizzati

- Liste in Python
- List Comprehension
- Operatore di moltiplicazione

## Autore

Esercizio svolto come pratica di Python.
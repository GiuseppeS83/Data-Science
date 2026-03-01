# String Normalizer Tool

Un semplice script Python per la **pulizia e la formattazione dei nomi**. Il tool si occupa di rimuovere gli spazi superflui e di uniformare l'uso delle maiuscole, rendendo i dati leggibili e pronti per database o interfacce utente.

---

## 🚀 Funzionalità
* **Rimozione Spazi:** Elimina gli spazi bianchi all'inizio e alla fine della stringa tramite `strip()`.
* **Formattazione Case:** Converte le stringhe in *Title Case* (es. "mario rossi" diventa "Mario Rossi").
* **Gestione Simboli:** Supporta nomi composti o con trattini.

## 🛠️ Requisiti
* **Python 3.x**: Non sono richieste librerie esterne (standard library).

## 📦 Installazione
1. Scarica o clona il file `normalizza_nome.py`.
2. Posizionati nella directory del file tramite terminale.

## 💻 Utilizzo
Puoi utilizzare la funzione importandola nel tuo progetto:

```python
from normalizza_nome import normalizza_nome

# Esempio di utilizzo
risultato = normalizza_nome("  marco rossi  ")
print(risultato) # Output: "Marco Rossi"
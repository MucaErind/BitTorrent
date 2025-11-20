#  Torrent - Verifica 5E

Piattaforma web modulare per la condivisione e la ricerca di file torrent, sviluppata con architettura **Client-Server** e database **NoSQL**.

##  Struttura del Progetto

Il progetto è suddiviso in tre moduli logici:

* **`/backend`**: Contiene il server API REST sviluppato in Python con Flask. Gestisce la logica di business, la connessione al database e le validazioni.
    * `app.py`: Entry point del server API (Porta 5000).
* **`/frontend`**: Contiene la Single Page Application (SPA).
    * `web_server.py`: Server web Python leggero per servire i file statici (Porta 8080).
    * `index.html`: L'interfaccia utente in HTML5/JS che comunica con le API.
* **`/database`**: Contiene la documentazione del modello dati.
    * `schema_*.json`: I JSON Schema per le collezioni (Utenti, Torrent, Commenti).

---

##  Prerequisiti e Configurazione

Per eseguire il progetto in locale è necessario avere installato:

1.  **Python 3.x**
2.  **MongoDB Community Server** (e MongoDB Compass per la visualizzazione dati)

### Installazione Dipendenze
Apri il terminale nella cartella del progetto ed esegui:

```bash
pip install flask flask-cors pymongo

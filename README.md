# BitTorrent
# Piattaforma TorrentShare - Verifica 5E

Piattaforma web modulare per la condivisione di file torrent sviluppata in Python e Flask.

## 🛠️ Architettura
* **Backend:** Python Flask con PyMongo. Espone API REST sulla porta 5000.
* **Database:** MongoDB (Database a documenti).
* **Frontend:** SPA (HTML/JS) servita da un web server Python dedicato sulla porta 8080.

## ⚙️ Configurazione
### Prerequisiti
Eseguire: `pip install flask pymongo flask-cors`

### Avvio
1. **Avviare MongoDB** (assicurarsi che il servizio sia attivo).
2. **Avviare Backend:**
   ```bash
   python backend/app.py
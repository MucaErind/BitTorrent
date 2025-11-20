# backend/init_db.py
from pymongo import MongoClient
from datetime import datetime

# 1. Connessione a MongoDB (Localhost porta standard)
client = MongoClient('mongodb://localhost:27017/')

# 2. Definizione del Database e delle Collezioni
db = client['torrent_db']  # Il DB si chiamerà 'torrent_db'
users_col = db['users']
torrents_col = db['torrents']
comments_col = db['comments']

# 3. Pulizia (Opzionale: cancella i dati vecchi per ripartire da zero)
users_col.delete_many({})
torrents_col.delete_many({})
comments_col.delete_many({})
print("🗑️  Vecchio database pulito.")

# 4. Creazione Dati Fake (Seguendo il tuo JSON Schema)

# --- UTENTE ---
admin_user = {
    "username": "AdminSystem",
    "email": "admin@torrentshare.it",
    "passwordHash": "hash_segreto_simulato",
    "ruolo": "amministratore",
    "isBanned": False,
    "dataRegistrazione": datetime.now().isoformat()
}
user_id = users_col.insert_one(admin_user).inserted_id
print("👤 Utente Admin creato.")

# --- TORRENTS ---
sample_torrents = [
    {
        "titolo": "Ubuntu 24.04 LTS",
        "descrizione": "L'ultima versione del sistema operativo Linux Ubuntu. Stabile e veloce.",
        "dimensioneByte": 4500000000,
        "categorie": ["Software", "Open Source"],
        "immaginiUrl": ["https://assets.ubuntu.com/v1/82818827-CoF_white_orange_hex_su.svg"],
        "autoreId": user_id, # Riferimento all'utente creato sopra
        "dataCaricamento": datetime.now().isoformat(),
        "statistiche": { # Pattern Computed
            "numeroDownload": 1540,
            "mediaVoti": 4.8,
            "conteggioVoti": 120
        }
    },
    {
        "titolo": "Big Buck Bunny 4K",
        "descrizione": "Film open source creato con Blender. Risoluzione 4K nativa.",
        "dimensioneByte": 800000000,
        "categorie": ["Film", "Animazione"],
        "immaginiUrl": [],
        "autoreId": user_id,
        "dataCaricamento": datetime.now().isoformat(),
        "statistiche": {
            "numeroDownload": 3400,
            "mediaVoti": 5.0,
            "conteggioVoti": 200
        }
    },
    {
        "titolo": "Corso Python Completo 2025",
        "descrizione": "Video corso per imparare Python da zero a esperto.",
        "dimensioneByte": 1200000000,
        "categorie": ["Documentari", "Software"], # Più categorie per testare i filtri
        "immaginiUrl": [],
        "autoreId": user_id,
        "dataCaricamento": datetime.now().isoformat(),
        "statistiche": {
            "numeroDownload": 50,
            "mediaVoti": 3.5,
            "conteggioVoti": 10
        }
    }
]

torrents_col.insert_many(sample_torrents)
print(f"💾 {len(sample_torrents)} Torrent inseriti nel database.")

print("✅ Database creato e popolato con successo!")
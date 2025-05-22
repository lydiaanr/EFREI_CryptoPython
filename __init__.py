from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

# Générer une clé de chiffrement une seule fois (et la sauvegarder)
# Remarque : N'exécutez cette ligne qu'une seule fois pour générer la clé, puis copiez-la dans le code
# key = Fernet.generate_key()
# print(key)  # Copiez la clé affichée et remplacez la ligne ci-dessous

# Remplacez cette clé par celle générée une fois
key = Fernet.generate(key)#b'votre_clé_fixe'  # Remplacez par la clé générée une seule fois
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')  # commentaire22

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        # Décryptage du token reçu
        valeur_decryptee = f.decrypt(token.encode())  # Conversion du token en bytes et décryptage
        return f"Valeur décryptée : {valeur_decryptee.decode()}"  # Retourne la valeur décryptée
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"  # Gestion des erreurs si le token est invalide

if __name__ == "__main__":
    app.run(debug=True)

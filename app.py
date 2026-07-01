import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'cle_secrete_super_secure_a_changer'

# Fonction de connexion à la base de données avec reconnexion automatique
def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'localhost'),
                user=os.environ.get('DB_USER', 'root'),
                password=os.environ.get('DB_PASSWORD', 'root_secure_password'),
                database=os.environ.get('DB_NAME', 'techsecure_db'),
                charset='utf8mb4'
            )
            return connection
        except mysql.connector.Error:
            retries -= 1
            time.sleep(2)
    raise Exception("Impossible de se connecter à la base de données MySQL.")

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/filiales')
def filiales():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM filiales")
    liste_filiales = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('filiales.html', filiales=liste_filiales)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_filiale():
    if request.method == 'POST':
        ville = request.form['ville']
        adresse = request.form['adresse']
        responsable = request.form['responsable']
        employes = request.form['employes']
        ip = request.form['ip']
        
        # SÉCURITÉ : Requête paramétrée contre les Injections SQL
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO filiales (ville, adresse, responsable, employes, ip) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (ville, adresse, responsable, employes, ip))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('filiales'))
    return render_template('ajouter.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        telephone = request.form['telephone']
        message = request.form['message']
        
        # SÉCURITÉ : Requête paramétrée contre les Injections SQL
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO contacts (nom, prenom, email, telephone, message) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nom, prenom, email, telephone, message))
        conn.commit()
        cursor.close()
        conn.close()
        
        flash("Votre message a été envoyé avec succès !", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/apropos')
def apropos():
    return render_template('apropos.html')

if __name__ == '__main__':
    # Écoute sur toutes les interfaces réseau du conteneur
    app.run(host='0.0.0.0', port=5000, debug=True)
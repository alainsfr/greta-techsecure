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

@app.route('/filiales/supprimer/<int:id>')
def supprimer_filiale(id):
    # SÉCURITÉ : Requête paramétrée pour éviter les injections SQL
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM filiales WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash("L'agence a été supprimée avec succès.", "success")
    return redirect(url_for('filiales'))

@app.route('/filiales/voir/<int:id>')
def voir_filiale(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM filiales WHERE id = %s", (id,))
    filiale = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not filiale:
        flash("Agence introuvable.", "error")
        return redirect(url_for('filiales'))
        
    return render_template('voir.html', filiale=filiale)

# 📝 NOUVELLE ROUTE : MODIFICATION FONCTIONNELLE ET SÉCURISÉE D'UNE FILIALE
@app.route('/filiales/modifier/<int:id>', methods=['GET', 'POST'])
def modifier_filiale(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        ville = request.form['ville']
        adresse = request.form['adresse']
        responsable = request.form['responsable']
        employes = request.form['employes']
        ip = request.form['ip']
        
        # SÉCURITÉ AUDIT : Requête paramétrée contre les injections SQL
        query = """
            UPDATE filiales 
            SET ville = %s, adresse = %s, responsable = %s, employes = %s, ip = %s 
            WHERE id = %s
        """
        cursor.execute(query, (ville, adresse, responsable, employes, ip, id))
        conn.commit()
        cursor.close()
        conn.close()
        
        flash("La filiale a été mise à jour avec succès !", "success")
        return redirect(url_for('filiales'))
        
    # GET : Récupération des données actuelles pour pré-remplir le formulaire
    cursor.execute("SELECT * FROM filiales WHERE id = %s", (id,))
    filiale = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not filiale:
        flash("Filiale introuvable pour modification.", "error")
        return redirect(url_for('filiales'))
        
    return render_template('modifier.html', filiale=filiale)

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
        
        flash("La filiale a été ajoutée avec succès !", "success")
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
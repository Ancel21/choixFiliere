"""
Created on Sun Nov  5 01:12:28 2023

@author: ancel
"""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Charger les données depuis le fichier CSV
data = pd.read_csv('fichier.csv')

# ...Création des dictionnaires de mots-clés et poids pour IPS et ASTRE
mots_cles_ips = {
    "Java": 5,
    "Python": 4,
    "C++": 2,
    "C#": 3,
    "JavaScript": 3,
    "UX/UI": 4,
    "Frontend / Backend": 5,
    "VR/AR": 4,
    "VSCode": 4,
    "Freelance": 4,
    "Résoudre des problèmes avec du code": 3,
    "Créer du contenu": 4,
    "L'esthétique": 4,
    "La sécurité": 2,
    "PME/Startups": 4,
    "Mathématiques": 4,
    "Jupyter": 4,
    "Intelligence Artificielle": 4,
    "Kotlin/Dart": 4,
    "Robotique": -2,
    "Arduino": -2,
    "Domotique": -2,
    "PC": 2,
    "Téléphone": 2,
    "Numérique et sciences informatiques": 4,
    "Linux": 2,
    "Windows": 4,
    "ENSIMERSION": 4,
    "ENSIM'ELEC": -2
    # Autres mots-clés pour IPS
}

mots_cles_astre = {
    "Java": 1,
    "C++": 4,
    "Python": 4,
    "C#": 3,
    "JavaScript": -1,
    "UX/UI": -2,
    "Frontend / Backend": -1,
    "VR/AR": -1,
    "Robotique": 4,
    "Domotique": 4,
    "Arduino": 4,
    "Linux": 4,
    "Windows": 3,
    "PC": 4,
    "Téléphone": 4,
    "ENSIMERSION": -2,
    "ENSIM'ELEC": 4,
    "Code::Blocks": 3,
    "Grande entreprise, grand groupe": 4,
    "PME/Startups": 1,
    "Le fonctionnel":4,
    "L'esthétique": 1,
    "La sécurité": 4,
    "Je ne prends pas de sac à dos": 3,
    "Cameroun": -1,
    "Côte d'ivoire": -1
    # Autres mots-clés pour ASTRE
}

# Initialisation d'un dictionnaire pour stocker les choix de filière pour chaque étudiant
choices = {}

# Paramètres par défaut des poids des critères
weights = {
    "Techno & outils": 1.0,
    "Passe temps et passion": 1.0,
    "Ambitions & objectifs professionnels": 1.0
}

# Itération à travers les lignes du DataFrame
for index, row in data.iterrows():
    student_id = row.iloc[0]  # Obtenez le numéro étudiant de la 1ère colonne

    # Initialisation des totaux de points pour IPS et ASTRE pour chaque étudiant
    total_ips = 0
    total_astre = 0

    # Colonnes pour le critère "Techno & outils"
    techno_columns = [1, 2, 3]  # Remplacez ces numéros par les indices corrects de vos colonnes

    # Calcul des scores en fonction des réponses de l'étudiant et des poids des critères
    for col_idx in techno_columns:
        response = row.iloc[col_idx]

        # Critère "Techno & outils"
        total_ips += mots_cles_ips.get(response, 0) * weights.get("Techno & outils", 1.0)
        total_astre += mots_cles_astre.get(response, 0) * weights.get("Techno & outils", 1.0)

    # Ajoutez d'autres conditions pour les autres critères

    # Vérification du choix en fonction des totaux de points
    if total_ips > total_astre:
        choix_filiere = "IPS"
    elif total_astre > total_ips:
        choix_filiere = "ASTRE"
    else:
        choix_filiere = "Indécis"

    # Stockez le choix de filière dans le dictionnaire
    choices[student_id] = choix_filiere

# Comptez le nombre d'étudiants pour chaque filière
count_ips = sum(1 for choix in choices.values() if choix == "IPS")
count_astre = sum(1 for choix in choices.values() if choix == "ASTRE")
count_indecis = sum(1 for choix in choices.values() if choix == "Indécis")

@app.route('/')
def index():
    return render_template('index.html', weights=weights)

@app.route('/result', methods=['POST'])
def result():
    global weights
    # Récupérer les poids des critères depuis le formulaire
    weights = {
        "Techno & outils": float(request.form.get('weight_techno')),
        "Passe temps et passion": float(request.form.get('weight_passion')),
        "Ambitions & objectifs professionnels": float(request.form.get('weight_ambitions'))
    }

    # Itération à travers les lignes du DataFrame
    for index, row in data.iterrows():
        student_id = row.iloc[0]  # Obtenez le numéro étudiant de la 1ère colonne

        # Initialisation des totaux de points pour IPS et ASTRE pour chaque étudiant
        total_ips = 0
        total_astre = 0

        # Colonnes pour le critère "Techno & outils"
        techno_columns = [2, 3, 4]  # Remplacez ces numéros par les indices corrects de vos colonnes
        passion_columns = [5, 6, 7,17]
        objectifs_columns = [12, 13, 14, 15]

        # Calcul des scores en fonction des réponses de l'étudiant et des poids des critères
        for col_idx in techno_columns:
            response = row.iloc[col_idx]

            # Critère "Techno & outils"
            total_ips += mots_cles_ips.get(response, 0) * weights.get("Techno & outils", 1.0)
            total_astre += mots_cles_astre.get(response, 0) * weights.get("Techno & outils", 1.0)

        for col_idx in passion_columns:
            response = row.iloc[col_idx]

            # Critère "Passions & passe temps"
            total_ips += mots_cles_ips.get(response, 0) * weights.get("Passe temps et passion", 1.0)
            total_astre += mots_cles_astre.get(response, 0) * weights.get("Passe temps et passion", 1.0)

        for col_idx in objectifs_columns:
            response = row.iloc[col_idx]

            # Critère "Objectifs & Projet pro"
            total_ips += mots_cles_ips.get(response, 0) * weights.get("Ambitions & objectifs professionnels", 1.0)
            total_astre += mots_cles_astre.get(response, 0) * weights.get("Ambitions & objectifs professionnels", 1.0)

        # Ajoutez d'autres conditions pour les autres critères

        # Vérification du choix en fonction des totaux de points
        if total_ips > total_astre:
            choix_filiere = "IPS"
        elif total_astre > total_ips:
            choix_filiere = "ASTRE"
        else:
            choix_filiere = "Indécis"

        # Stockez le choix de filière dans le dictionnaire
        choices[student_id] = choix_filiere

    # Comptez le nombre d'étudiants pour chaque filière
    count_ips = sum(1 for choix in choices.values() if choix == "IPS")
    count_astre = sum(1 for choix in choices.values() if choix == "ASTRE")
    count_indecis = sum(1 for choix in choices.values() if choix == "Indécis")

    return render_template('result.html', count_ips=count_ips, count_astre=count_astre, count_indecis=count_indecis, weights=weights)

if __name__ == '__main__':
    app.run(debug=True)
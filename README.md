# choixFiliere

Introduction:
Le projet avait pour objectif de créer un système d'aide à la décision pour aider les étudiants à choisir entre deux filières, IPS (Informatique et Pédagogie Spécialisée) et ASTRE (Analyse des Systèmes de Traitement et de Recherche d'Informations). Le système attribue un score basé sur les réponses des étudiants à un questionnaire, avec des poids différents pour chaque critère.

Technologies Utilisées:

Python pour le backend avec Flask comme framework web.
Pandas pour le traitement des données.
HTML/CSS pour les pages web.
Bootstrap pour la mise en page.
Chart.js pour la visualisation des données.
Fonctionnalités Clés:

Formulaire de Questionnaire: Les étudiants remplissent un questionnaire en ligne.
Calcul des Scores: Les scores IPS et ASTRE sont calculés en fonction des réponses et des poids attribués à chaque critère (Techno & Outils, Passe Temps et Passion, Ambitions & Objectifs Professionnels).
Visualisation des Résultats: Les résultats sont présentés dans un tableau et un diagramme en donut sur la page principale.
Détails par Étudiant: Les utilisateurs peuvent afficher les détails spécifiques d'un étudiant, y compris ses réponses, les critères choisis et un diagramme comparatif des scores IPS et ASTRE.
Structure du Code:

Le backend est construit avec Flask, avec des routes pour l'accueil, les résultats généraux et les détails par étudiant.
Le calcul des scores est effectué à l'aide de Pandas, en parcourant le DataFrame des réponses.
Chart.js est utilisé pour créer des graphiques interactifs sur les pages web.
Améliorations Possibles:

Authentification: Ajouter un système d'authentification pour assurer la confidentialité des résultats.
Interface Utilisateur Améliorée: Affiner l'interface utilisateur pour une meilleure expérience utilisateur.
Base de Données: Stocker les réponses des étudiants dans une base de données pour une gestion plus efficace des données.
Conclusion:
Le projet a réussi à créer un système d'aide à la décision fonctionnel pour le choix de filière, en prenant en compte les critères spécifiques tels que Techno & Outils, Passe Temps et Passion, Ambitions & Objectifs Professionnels. Les étudiants peuvent accéder à des résultats généraux et obtenir des détails spécifiques. Des améliorations futures pourraient renforcer la sécurité et l'expérience utilisateur.

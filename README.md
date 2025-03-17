# SpamDetection

Le programme **SpamDetection.py** utilise un modèle d'apprentissage automatique pour détecter les messages de spam. Le modèle est formé à l'aide de l'algorithme **Naive Bayes** et d'un ensemble de données nommé **spam.csv**, trouvé sur Kaggle. Ce jeu de données contient des messages étiquetés comme **spam** ou **ham** (non-spam).

## Objectif du projet

L'objectif de ce projet est de développer un modèle capable de prédire si un message donné est un spam ou non. Cela peut être utile pour filtrer les messages indésirables dans des applications de messagerie.

## Fonctionnalités

- Chargement et prétraitement des données depuis le fichier **spam.csv**.
- Transformation des données textuelles en vecteurs numériques avec **CountVectorizer**.
- Formation d'un modèle de classification utilisant l'algorithme **Naive Bayes** (**MultinomialNB**).
### To do : 
- Évaluation de la performance du modèle avec des métriques comme la **précision**, le **rappel**, et la **F-mesure**.
- Affichage d'une **matrice de confusion** pour visualiser les erreurs du modèle.

## Prérequis

Avant d'exécuter ce projet, assurez-vous d'avoir installé les bibliothèques suivantes :

- `pandas` pour la gestion des données.
- `numpy` pour les calculs numériques.
- `matplotlib` pour la visualisation des résultats.
- `sklearn` pour l'implémentation de l'algorithme Naive Bayes et l'évaluation du modèle.

Vous pouvez installer les dépendances avec :

```bash
pip install pandas numpy matplotlib scikit-learn

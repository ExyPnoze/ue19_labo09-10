# Trivia Game with trivia.py

Un simple jeu de questions-réponses trivia basé sur Python. Ce programme interagit avec une API de trivia pour poser des questions à l'utilisateur.

## Fonctionnalités

- Choisissez parmi différentes catégories de questions trivia.
- Recevez des questions aléatoires de la catégorie sélectionnée.
- Répondez aux questions et obtenez un retour immédiat sur la justesse de votre réponse.
- Possibilité de jouer autant de fois que vous le souhaitez.

## Prérequis

- Python 3.x installé sur votre système.
- Bibliothèques Python : `requests` et `json` (elles sont généralement incluses dans l'installation standard de Python).

## Installation

1. Clonez le référentiel à partir de GitHub en utilisant la commande suivante :

   ```bash
   git clone https://github.com/ExyPnoze/ue19_labo09-10.git
   ```

2. Accédez au répertoire du projet :

   ```bash
   cd ue19_labo09-10
   ```

3. Exécutez le programme trivia.py :

   ```bash
   python trivia.py
   ```

## Utilisation

1. Au lancement du programme, vous serez invité à choisir une catégorie de questions trivia parmi les options suivantes :

   - Art et Littérature
   - Langue
   - Science et Nature
   - Général
   - Nourriture et Boissons
   - Géographie
   - Musique
   - Mathématiques
   - Religion et Mythologie
   - Sports et Loisirs

2. Sélectionnez la catégorie en entrant le numéro correspondant.

3. Le programme récupérera une question aléatoire de la catégorie choisie depuis une API de trivia.

4. Répondez à la question en entrant votre réponse. Le programme vous donnera immédiatement une réponse quant à la justesse de votre réponse.

5. Vous pouvez jouer autant de fois que vous le souhaitez en répondant à d'autres questions.

6. Pour quitter le jeu, répondez "no" lorsqu'on vous demande si vous souhaitez rejouer.

---

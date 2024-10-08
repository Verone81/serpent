# Jeu du Serpent

Ce projet est une implémentation classique du jeu du serpent utilisant la bibliothèque Pygame. Le but du jeu est de contrôler un serpent, de le faire grandir en mangeant des pommes, et d'éviter de se mordre la queue ou de heurter les murs.

## Fonctionnalités

- **Contrôle du serpent** : Utilisez les flèches du clavier pour changer la direction du serpent.
- **Grandir** : Chaque fois que le serpent mange une pomme, il grandit d'une unité et votre score augmente.
- **Game Over** : Le jeu se termine si le serpent heurte les bords de l'écran ou se mord la queue.
- **Affichage du score** : Le score actuel est affiché en haut de la fenêtre de jeu.

1. **Cloner le dépôt :**
   git clone https://github.com/votre-nom-utilisateur/jeu-du-serpent.git
   cd jeu-du-serpent

2. **Installer les dépendances** : Assurez-vous d'avoir Python et Pygame installés sur votre machine.

3. **Lancez le jeu :**
python  main.py

## Comment jouer
- Flèche gauche : Déplace le serpent vers la gauche.
- Flèche droite : Déplace le serpent vers la droite.
- Flèche haut : Déplace le serpent vers le haut.
- Flèche bas : Déplace le serpent vers le bas.

Appuyez sur "Entrée" après un Game Over pour recommencer une partie.

## Ressources
- **Pygame** : Site officiel de Pygame
- **Polices** : Ce projet utilise la police NerkoOne-Regular.ttf, qui doit être incluse dans le répertoire du projet.

## Personnalisation
- **Vitesse du jeu** : La vitesse du jeu est contrôlée par la fonction **clock.tick(10)**. Vous pouvez augmenter ou diminuer le nombre pour ajuster la difficulté.

- **Couleurs** : Vous pouvez changer les couleurs du serpent, des pommes, et de l'arrière-plan en modifiant les valeurs RGB dans le code.

- **Sons** : Vous pouvez remplacer le fichier son_manger.mp3 par n'importe quel autre fichier audio pour changer le son lorsque le serpent mange une pomme.

## Améliorations possibles
- **Ajout de niveaux** : Implémenter plusieurs niveaux avec une vitesse de jeu croissante.

- **Obstacles** : Ajouter des obstacles aléatoires sur le terrain pour rendre le jeu plus difficile.

- **Mode multijoueur** : Ajouter un mode multijoueur local où deux serpents sont contrôlés simultanément.

## Contribuer
Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations ou si vous trouvez des bugs, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.
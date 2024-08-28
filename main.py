import pygame
import random
import time

# Configurations
tuile = 10  # Taille d'une tuile (unité de mouvement du serpent)
tuile_nombre = 60  # Nombre de tuiles en largeur et hauteur
score_hauteur = 0  # Hauteur réservée pour afficher le score (inutilisée ici)
fenetre_largeur = tuile * tuile_nombre  # Largeur de la fenêtre de jeu
fenetre_hauteur = tuile * tuile_nombre + score_hauteur  # Hauteur de la fenêtre de jeu

class Serpent:
    """
    Classe représentant le serpent dans le jeu.
    
    Attributes:
        screen (pygame.Surface): Surface sur laquelle le serpent est dessiné.
        x (int): Position x du serpent.
        y (int): Position y du serpent.
        direction (str): Direction actuelle du serpent ("G", "D", "H", "B").
        corps (list of tuple): Liste des segments qui composent le serpent.
        score (int): Score actuel du joueur.
    """

    def __init__(self, screen, x, y):
        """
        Initialise un objet Serpent.
        
        Args:
            screen (pygame.Surface): Surface de dessin.
            x (int): Position x initiale du serpent.
            y (int): Position y initiale du serpent.
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = ""  # Direction par défaut, aucune direction au début
        self.corps = [(self.x, self.y)]  # Le corps du serpent commence avec un segment
        self.score = 0  # Score initial

    def update(self):
        """
        Met à jour la position du serpent en fonction de la direction.
        Gère les collisions avec les bords de la fenêtre et vérifie si le serpent se mord la queue.
        """
        if self.direction == "G":
            self.x -= tuile
            if self.x < 0:  # Collision avec le bord gauche
                game_over()
        elif self.direction == "D":
            self.x += tuile
            if self.x >= fenetre_largeur:  # Collision avec le bord droit
                game_over()
        elif self.direction == "B":
            self.y += tuile
            if self.y >= fenetre_hauteur:  # Collision avec le bord inférieur
                game_over()
        elif self.direction == "H":
            self.y -= tuile
            if self.y < 0:  # Collision avec le bord supérieur
                game_over()

        # Déplacer le serpent en ajoutant la nouvelle position en tête de la liste
        self.corps.insert(0, (self.x, self.y))
        self.corps.pop()  # Retirer le dernier segment pour garder la longueur constante

        # Vérifier si le serpent se mord la queue
        self.mord_la_queue()

    def grow(self):
        """
        Fait grandir le serpent en ajoutant un segment à son corps.
        Augmente également le score.
        """
        self.corps.append(self.corps[-1])  # Ajoute un segment à la fin du corps
        self.score += 1  # Incrémente le score

    def draw(self):
        """
        Dessine le serpent sur l'écran.
        """
        for segment in self.corps:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, tuile, tuile))

    def mord_la_queue(self):
        """
        Vérifie si la tête du serpent entre en collision avec son propre corps.
        Si oui, le serpent est réduit à sa tête et le score est réinitialisé.
        """
        tete = self.corps[0]
        if tete in self.corps[1:]:  # Si la tête touche une autre partie du corps
            self.corps = self.corps[:1]  # Réinitialise le corps à sa tête
            self.score = 0  # Réinitialise le score


def afficher_bienvenue():
    """
    Affiche un message de bienvenue au démarrage du jeu et attend que l'utilisateur appuie sur 'Entrer'.
    """
    font = pygame.font.Font("NerkoOne-Regular.ttf", 18)
    bienvenue = font.render('Bienvenue sur le jeu du serpent cliquez sur "Entrer" pour commencer', True, 'black')
    text_rect_bienvenue = bienvenue.get_rect(center=(300, 300))

    fenetre.fill('white')
    fenetre.blit(bienvenue, text_rect_bienvenue)
    pygame.display.flip()
    attendre()  # Attend l'action de l'utilisateur


def attendre():
    """
    Attend que l'utilisateur appuie sur une touche pour continuer ou quitter le jeu.
    """
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Appuyer sur Entrée pour continuer
                    waiting = False
                    return  # Reprend l'exécution du jeu


def pointage_afficher():
    """
    Affiche le score actuel du joueur en haut à gauche de l'écran.
    """
    font = pygame.font.Font("NerkoOne-Regular.ttf", 24)
    score_font = font.render(f'score: {serpent.score}', True, 'white')
    text_rect_score = score_font.get_rect(center=(50, 50))
    fenetre.blit(score_font, text_rect_score)


def pomme_hasard():
    """
    Génère une position aléatoire pour la pomme.

    Returns:
        tuple: Position x et y de la pomme.
    """
    return random.randint(0, tuile_nombre - 1) * tuile, random.randint(0, tuile_nombre - 1) * tuile


def game_over():
    """
    Affiche un message de fin de jeu et attend que l'utilisateur prenne une action.
    """
    fenetre.fill("white")
    
    # Configuration de la police
    my_font = pygame.font.SysFont('', 60)  # Police par défaut du système
    text_surface = my_font.render('Game Over', False, (0, 0, 0))
    
    # Calcul pour centrer le texte
    text_rect = text_surface.get_rect(center=(fenetre_largeur // 2, fenetre_hauteur // 2))
    fenetre.blit(text_surface, text_rect)
    
    pygame.display.flip()  # Mettre à jour l'affichage

    # Option pour attendre une action de l'utilisateur
    attendre()  # Attend une action après l'affichage de "Game Over"


# Initialisation de Pygame, de la police et du mixer
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Création de la fenêtre de jeu
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))
pygame.display.set_caption("Jeu du Serpent")

# Chargement du son à jouer lorsque le serpent mange une pomme
son_manger = pygame.mixer.Sound("son_manger.mp3")

clock = pygame.time.Clock()

# Affichage du message de bienvenue
afficher_bienvenue()

# Position initiale du serpent
serpent = Serpent(fenetre, tuile * tuile_nombre // 2, tuile * tuile_nombre // 2)

# Position initiale de la pomme
pomme_pos = pomme_hasard()

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Changer la direction du serpent en fonction de la touche pressée
            if event.key == pygame.K_LEFT and serpent.direction != "D":
                serpent.direction = "G"
            elif event.key == pygame.K_RIGHT and serpent.direction != "G":
                serpent.direction = "D"
            elif event.key == pygame.K_DOWN and serpent.direction != "H":
                serpent.direction = "B"
            elif event.key == pygame.K_UP and serpent.direction != "B":
                serpent.direction = "H"

    # Mettre à jour la position du serpent
    serpent.update()

    # Vérifier la collision avec la pomme
    if (serpent.x, serpent.y) == pomme_pos:
        son_manger.play()  # Jouer le son lorsque le serpent mange la pomme
        serpent.grow()  # Faire grandir le serpent
        pomme_pos = pomme_hasard()  # Générer une nouvelle position pour la pomme
    
    # Effacer l'écran
    fenetre.fill("black")

    # Dessiner le serpent
    serpent.draw()

    # Dessiner la pomme
    pygame.draw.rect(fenetre, "red", (*pomme_pos, tuile, tuile))

    # Afficher le pointage
    pointage_afficher()

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Réguler la vitesse du jeu
    clock.tick(10)

pygame.quit()

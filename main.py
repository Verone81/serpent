import pygame
import random

# Configurations
tuile = 40
tuile_nombre = 20
score_hauteur = 40
fenetre_largeur = tuile * tuile_nombre
fenetre_hauteur = tuile * tuile_nombre

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()

fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))
pygame.display.set_caption("Jeu du Serpent")

son_manger = pygame.mixer.Sound("son_manger.mp3")

clock = pygame.time.Clock()

class Serpent:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = ""
        self.corps = [(self.x, self.y)]

    def update(self):
        if self.direction == "G":
            self.x -= tuile
        elif self.direction == "D":
            self.x += tuile
        elif self.direction == "B":
            self.y += tuile
        elif self.direction == "H":
            self.y -= tuile

        self.corps.insert(0, (self.x, self.y))
        self.corps.pop()

    def grow(self):
        self.corps.append(self.corps[-1])

    def draw(self):
        for segment in self.corps:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, tuile, tuile))

def pomme_hasard():
    return random.randint(0, tuile_nombre - 1) * tuile, random.randint(0, tuile_nombre - 1) * tuile

# Position initiale du serpent
serpent = Serpent(fenetre, tuile * tuile_nombre // 2, tuile * tuile_nombre // 2)

# Position initiale de la pomme
pomme_pos = pomme_hasard()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
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
        son_manger.play()
        serpent.grow()
        pomme_pos = pomme_hasard()

    # Effacer l'écran
    fenetre.fill("black")

    # Dessiner le serpent
    serpent.draw()

    # Dessiner la pomme
    pygame.draw.rect(fenetre, "red", (*pomme_pos, tuile, tuile))

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Réguler la vitesse du jeu
    clock.tick(10)

pygame.quit()

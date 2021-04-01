import pygame
pygame.init()

#générer la fenetre de notre jeu
pygame.display.set_caption("Shadow fight")
screen = pygame.display.set_mode((1600,900))

#importer l'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, (1600, 900))

#importer l'icone de la fenêtre
icon = pygame.image.load('assets/icone_jeu.png')
icon = pygame.transform.scale(icon, (36, 36))

running = True

#boucle tant que cette condition est vrai
while running :

    #appliquer l'arrière plan de notre jeu
    screen.blit(background , (0,0))

    #appliquer l'icone de la fenêtre
    pygame.display.set_icon(icon)

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get() :
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("fermeture du jeu")

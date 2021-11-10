
import pygame
import sys


#SIZES
WIDTH = 800
HEIGHT = 1000

player_vel = 8
player_shoot_vel = 16
player_shot_delay = 7
player_width = 60
player_health = 3

count = 0
laser_delay = 0

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))




#Class player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('player_ship.png'), (player_width, player_width)).convert_alpha()
        self.rect = self.image.get_rect() #figures out rectangle based on image
        self.rect.center = (WIDTH/2, HEIGHT/1.1)
    
    def update(self):
        global player_health, count, player_shot_delay
        count += 1;
        keys = pygame.key.get_pressed()
        #movement
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - player_width:
            self.rect.x += player_vel
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= player_vel
        if keys[pygame.K_UP]  and self.rect.y > HEIGHT*0.1:
            self.rect.y -= player_vel
        if keys[pygame.K_DOWN]  and self.rect.y < HEIGHT*0.9:
            self.rect.y += player_vel

        if keys[pygame.K_SPACE] and count%player_shot_delay == 0:
            all_sprites.add(Player_Shot())




        
class Player_Shot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('player_shot.png'), (14,37)).convert_alpha()
        self.rect = self.image.get_rect() #figures out rectangle based on image
        self.rect.center = player.rect.center
    
    def update(self):
        self.rect.y -= player_shoot_vel

        if self.rect.y < 0:
            all_sprites.remove(self)




class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('Space Background.png'), (WIDTH, HEIGHT)).convert()
        self.rect = self.image.get_rect() #figures out rectangle based on image
        self.rect.center = (WIDTH/2, HEIGHT/2)
    

        





all_sprites = pygame.sprite.Group()
all_sprites.add(Background())
player = Player()
all_sprites.add(player)

def main():
    pygame.init()
    clock = pygame.time.Clock() 

    screen = pygame.display.set_mode((WIDTH,HEIGHT))  
    running = True  
    
    while running:  
        clock.tick(FPS)
        

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False

            
        #pygame.display.flip() 

        all_sprites.update()

        all_sprites.draw(screen)
        pygame.display.update()
         

    pygame.quit() 


main()
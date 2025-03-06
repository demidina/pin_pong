import pygame
import time
pygame.init()

FPS = 60
WINDOW_SIZE = 1000, 700
background_color = (255, 255, 242)

main_window = pygame.display.set_mode((WINDOW_SIZE))
pygame.display.set_caption("pin_pong")
main_window.fill(background_color)
clock = pygame.time.Clock()
 
pygame.mixer.music.load("slava-skripka-bobr.mp3")
pygame.mixer.music.play(-1)


class GameSprite (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, image_filename):
        super().__init__()
        self.image = pygame.image.load(image_filename)
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, x, y, width, height, speed, image_filename):
        super().__init__(x, y, width, height, speed, image_filename)
        self.keys = None
    def set_control (self, key_up, key_down):
        self.keys = {
        "UP": key_up,
        "DOWN": key_down,
        }
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys [self.keys["UP"]]: self.rect.y -= self.speed
        if pressed_keys [self.keys["DOWN"]]: self.rect.y += self.speed


player1 = Player(0, 0, 50, 80, 10, 'палка.png')
player1.set_control(pygame.K_UP, pygame.K_DOWN)    
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    main_window.fill(background_color)
    player1.update()
    player1.reset(main_window)
    pygame.display.update()
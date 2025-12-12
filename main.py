from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('bg-pingpong.jpg'), (win_width, win_height))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def motion_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket_l = Player('rakun.jpg', 5, 250, 65, 65, 4)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    racket_l.show()
    racket_l.motion_l()
    display.update()
    clock.tick(FPS)
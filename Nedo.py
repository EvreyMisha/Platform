import pygame
import random
clock = pygame.time.Clock()

pygame.init()
height = 300
width = 794
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крес")

all_sprites = pygame.sprite.Group()
mountain = pygame.sprite.Group()
pt = pygame.sprite.Group()


class Mountain(pygame.sprite.Sprite):
    image = pygame.Surface([50, 10])

    def __init__(self,pos):
        super().__init__(mountain)
        self.image.fill((70,70,70))
        self.rect = pygame.Rect(pos[0],pos[1],50,10)
        self.add(mountain)

class Landing(pygame.sprite.Sprite):
    image = pygame.Surface([20, 20])

    def __init__(self, pos):
        super().__init__(pt)
        self.image.fill((0,0,255))
        self.rect = pygame.Rect(pos[0],pos[1],20,20)
        self.add(pt)

    def update(self):
        if not pygame.sprite.spritecollideany(self, mountain):
            self.rect = self.rect.move(0, 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect = self.rect.move(-10, 0)
        if keys[pygame.K_d]:
            self.rect = self.rect.move(10, 0)


run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
    if pygame.mouse.get_pressed()[0]:
        Mountain(pygame.mouse.get_pos())
    if pygame.mouse.get_pressed()[2]:
        pt.empty()
        Landing(pygame.mouse.get_pos())
    win.fill((0, 0, 0))
    pt.update()
    mountain.draw(win)
    pt.draw(win)
    clock.tick(10)
    pygame.display.flip()

pygame.quit()

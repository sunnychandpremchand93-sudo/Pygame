import pygame
import random
class Car(pygame.sprite.Sprite):
    def __init__(self,speedX,positionX,positionY):
        super().__init__()
        self.speedX = speedX
        self.image = pygame.image.load('source_images/car.png')
        self.rect = self.image.get_rect()
        self.rect.center = (positionX,positionY)
        
class EnemyCar(pygame.sprite.Sprite):
     def __init__(self,speedX,speedY,positionX,positionY):
        super().__init__()
        self.speedX = speedX
        self.speedY = speedY
        self.image = pygame.image.load('source_images/enemy_car_'+str(random.randint(1,3))+'.png')
        self.rect = self.image.get_rect()
        self.rect.center = (positionX,positionY)


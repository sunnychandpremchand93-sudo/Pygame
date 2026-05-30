import pygame
import sys
import car_class
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Manoj and Sunny First Game')

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

#creating my car class object
my_car = car_class.Car(1,400,500)
all_sprites.add(my_car)


road = pygame.image.load('source_images/road.png')


MENU_MUSIC='source_music/menu_music.mp3'
GAME_MUSIC='source_music/game_music.mp3'

def play_music(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)

LANE_WIDTH = 600 // 3
LINE_WIDTH = 10
LINE_HEIGHT = 40
LINE_GAP = 30
SPEED = 2
LINE_COLOR = (255,255,255)

divider_xs =[
    LANE_WIDTH - LINE_WIDTH // 2,
    2 * LANE_WIDTH - LINE_WIDTH // 2
]

lane_lines = []
for x in divider_xs:
    col = []
    for y in range(0,600,LINE_HEIGHT+LINE_GAP):
        col.append(pygame.Rect(x+100,y,LINE_WIDTH,LINE_HEIGHT))
    lane_lines.append(col)


SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1000)  # every 5 seconds


enemy_cars = []
#creating enemy car class object
#enemy_car = car_class.EnemyCar(1,1,400,-100)
#all_sprites.add(enemy_car)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

width = 800
height = 600
# Fonts
font = pygame.font.SysFont(None, 72)
score_font = pygame.font.SysFont(None, 100)
small_font = pygame.font.SysFont(None, 36)

# Restart button
button_rect = pygame.Rect(width//2 - 100, height//2 + 50, 200, 50)
menu_rect = pygame.Rect(width//2 - 100, height//2 + 200, 200, 50)


Score = 0
HighScore = 0


Running = True
GameOver = True
MainMenu = True

if not GameOver:
    play_music(GAME_MUSIC)
else:
    play_music(MENU_MUSIC)

while Running:
    if not GameOver:
        
        if pygame.sprite.spritecollideany(my_car, enemy_sprites):
            print("collided macha")
            GameOver = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == SPAWN_EVENT:    
                new_enemy_car = car_class.EnemyCar(0,1,(200 * random.randint(1,3)+random.randint(-50,50)),-100)
                enemy_cars.append(new_enemy_car)
                all_sprites.add(new_enemy_car)
                enemy_sprites.add(new_enemy_car)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            my_car.rect.x -= my_car.speedX
            if my_car.rect.x < 100:
                my_car.rect.x = 100
        if keys[pygame.K_RIGHT]:
            my_car.rect.x += my_car.speedX
            if my_car.rect.x > 550:
                my_car.rect.x = 550       

        for enemy_car in enemy_cars:
            enemy_car.rect.y += enemy_car.speedY
            if enemy_car.rect.y > 700:
                Score+=1
                HighScore = max(HighScore,Score)
                enemy_car.kill()
                enemy_cars.remove(enemy_car)
        
        screen.blit(road, (0, 0))

        for col in lane_lines:
            for rect in col:
                rect.y += SPEED
                if rect.y > 600:
                    rect.y = -LINE_HEIGHT
                pygame.draw.rect(screen,LINE_COLOR,rect)
            
        all_sprites.draw(screen)
        Score_text = small_font.render("SCORE: "+str(Score), True, WHITE)
        HighScore_text = small_font.render("HIGH SCORE: "+str(HighScore), True, WHITE)
        screen.blit(Score_text,(20,20) )
        screen.blit(HighScore_text,(20,50))
        pygame.display.flip()

    else:
        if MainMenu:
            for enemy_car in enemy_cars:
                enemy_car.kill()
                enemy_cars.remove(enemy_car)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            HighScore = max(HighScore,Score)
            Score=0
            for enemy_car in enemy_cars:
                enemy_car.kill()
                enemy_cars.remove(enemy_car)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            screen.fill((0,0,0))
            car_game_text = font.render("THE CAR GAME", True, RED)
            text_rect = car_game_text.get_rect(center=(width // 2, height // 2 - 50))
            screen.blit(car_game_text, text_rect)

            pygame.draw.rect(screen, GRAY, button_rect)
            button_text = small_font.render("START", True, RED)
            button_text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, button_text_rect)

            HighScore_text = font.render("HIGHSCORE: "+str(HighScore), True, RED)
            text_rect = HighScore_text.get_rect(center=(width // 2, height // 2 + 200))
            screen.blit(HighScore_text, text_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
            
                if button_rect.collidepoint(event.pos):
                    GameOver = False
                    MainMenu = False
                    if GameOver:
                        play_music(MENU_MUSIC)
                    else:
                        play_music(GAME_MUSIC)

            pygame.display.flip()

        else:
            for enemy_car in enemy_cars:
                enemy_car.kill()
                enemy_cars.remove(enemy_car)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            HighScore = max(HighScore,Score)
            Score=0
            for enemy_car in enemy_cars:
                enemy_car.kill()
                enemy_cars.remove(enemy_car)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.draw.rect(screen, GRAY, menu_rect)
            button_text = small_font.render("MENU", True, BLACK)
            button_text_rect = button_text.get_rect(center=menu_rect.center)
            screen.blit(button_text, button_text_rect)
            
            #screen.fill((0,0,0))
            game_over_text = font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(width // 2, height // 2 - 50))
            screen.blit(game_over_text, text_rect)

            # Draw button
            pygame.draw.rect(screen, GRAY, button_rect)
            button_text = small_font.render("Restart", True, BLACK)
            button_text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, button_text_rect)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    GameOver = False
                    MainMenu = False
                    if MainMenu:
                        play_music(MENU_MUSIC)
                    else:
                        play_music(GAME_MUSIC)

                if menu_rect.collidepoint(event.pos):
                    MainMenu = True
                    if MainMenu:
                        play_music(MENU_MUSIC)
                    else:
                        play_music(GAME_MUSIC)

            pygame.display.flip()


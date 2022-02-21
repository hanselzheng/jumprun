import pygame
from sys import exit, get_coroutine_origin_tracking_depth
from random import randint, choice

def display_score():
    score = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = font2.render(f'{score}', True, 'Black')
    score_rect = score_surf.get_rect(topleft = (40,10))
    screen.blit(score_surf,score_rect)
    return score

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Jump Run')
icon = pygame.image.load('img/snail.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fps = 60
game_active = False
start_time = 0
high_score = 0


# font sizes
font1 = pygame.font.Font('ArcadeClassic.ttf', 100)
font2 = pygame.font.Font('ArcadeClassic.ttf', 50)
font3 = pygame.font.Font('ArcadeClassic.ttf', 30)


# background
bg_img = pygame.image.load('img/background.png').convert()
bg_img = pygame.transform.scale(bg_img,(800,400))
bg_img_x_pos = 0


# hero
hero = pygame.image.load('img/hero2.png').convert_alpha()
hero = pygame.transform.scale(hero,(20,30))
hero_rect = hero.get_rect(midbottom = (80,330))
hero_gravity = 0



# enemies
snail = pygame.image.load('img/snail.png').convert_alpha()
snail = pygame.transform.scale(snail,(55,40))
snail_rect = snail.get_rect(bottomleft = (830,330))

blob = pygame.image.load('img/blob.png').convert_alpha()
blob = pygame.transform.scale(blob,(40,25))
blob_rect = blob.get_rect(bottomleft =(1800,285))

obstacle_group = []



# game over menu
game_over = pygame.image.load('img/gameover.png').convert_alpha()
game_over_rect = game_over.get_rect(center = (400,100))

# snail menu
snail_menu = pygame.image.load('img/snail.png').convert_alpha()
snail_menu = pygame.transform.rotozoom(snail_menu,0,0.25)
snail_menu_rect = snail_menu.get_rect(center = (400,250))

#game name menu
game_name = font1.render('Jump Run',False,('#4E9F3D'))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = font3.render('Press  space  to  start',False,('#4E9F3D'))
game_message_rect = game_message.get_rect(center = (400,350))



# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)




# game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and hero_rect.bottom == 330:
                        hero_gravity -= 18
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.x = (randint(830,1000))
                blob_rect.x = (randint(1100,1700))
                start_time = int(pygame.time.get_ticks()/1000)



    if game_active:        
        # load images
        screen.blit(bg_img,(bg_img_x_pos,0))
        screen.blit(hero,hero_rect)
        high_score = display_score()

        snail_rect.x -= 4
        if snail_rect.x < -100:
            snail_rect.x = (randint(830,1000))
        screen.blit(snail,snail_rect)

        blob_rect.x -= 4
        if blob_rect.x < -100:
            blob_rect.x = (randint(1100,1700))
        screen.blit(blob,blob_rect)
        
        # player gravity
        hero_gravity += 1
        hero_rect.y += hero_gravity
        if hero_rect.bottom >= 330:
            hero_gravity = 0
            hero_rect.bottom = 330


    else:
        screen.fill("#125C13")
        screen.blit(snail_menu,snail_menu_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)
        hero_rect.midbottom = (80,330)
        hero_gravity = 0

        if high_score != 0:
            score_menu = font3.render(f'Your Score is  {high_score}',True,('#4E9F3D'))
            score_menu_rect = score_menu.get_rect(center = (400,120))

            screen.blit(score_menu,score_menu_rect)


    if hero_rect.colliderect(snail_rect):
        game_active = False
    elif hero_rect.colliderect(blob_rect):
        game_active = False



    


    
    



    pygame.display.update()
    clock.tick(fps)


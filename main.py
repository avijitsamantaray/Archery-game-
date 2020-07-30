import pygame
from pygame import mixer

import  screeninfo
from screeninfo import get_monitors

pygame.init()
mixer.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

for m in get_monitors():
    
    screen_width = m.width
    screen_height = m.height
block_width = 8
block_height = 130
arrow_width = 95
arrow_height = 5



display = pygame.display.set_mode((screen_width, screen_height),pygame.FULLSCREEN)
BG=pygame.image.load("background.png")
BG=pygame.transform.scale(BG,(screen_width, screen_height))
ar_img=pygame.image.load("bow.png")
ar_img=pygame.transform.scale(ar_img,(100, 100))
ar_img=pygame.transform.rotate(ar_img,-90)
ar_small=pygame.image.load("bow.png")
ar_small=pygame.transform.scale(ar_img,(40, 40))
ar_small=pygame.transform.rotate(ar_small,90)
BG_MUSIC=mixer.music.load("BG.mp3")
hit=pygame.mixer.Sound("hit.wav")

pygame.display.set_caption("ARCHERY MASTER 5000")

clock = pygame.time.Clock()




font = pygame.font.SysFont(None, 40)


def message_to_screen(msg, color,place):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, place)


def gameLoop():
    
    BG_MUSIC = mixer.music.play(-1)
    block_x = screen_width-30
    block_y = 25
    block_speed = 13

    arrow_x = 1
    arrow_y = screen_height//2
    arrow_speed = 0

    count=10
    score=0
    gameExit = False
  

    while not  gameExit:

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and arrow_x==1:
                  
                    count-=1
                    arrow_speed = 28
                   
                if event.key == pygame.K_q:
                    gameExit = True

        display.blit(BG,(0,0))
        display.blit(ar_img,(arrow_x, arrow_y))

      
        if arrow_x> screen_width+300:
            arrow_x=1
            arrow_speed = 0
        if (arrow_x+ar_img.get_width())in range(block_x-(3*block_width),block_x-(2*block_width)+4)and ((arrow_y) in range(rect3.top,rect3.bottom)):
            pygame.mixer.Sound.play(hit)
            arrow_x = 1
            arrow_speed = 0
            score+=30
        elif  (arrow_x+ar_img.get_width())in range(block_x-(2*block_width),block_x-block_width+4) and (arrow_y) in range(rect2.top,rect2.bottom):
            pygame.mixer.Sound.play(hit)
            arrow_x = 1
            arrow_speed=0
            score+=20
        elif  (arrow_x+ar_img.get_width())in range(block_x-block_width,block_x+4) and (arrow_y) in range(block_y,block_y+block_height+2):
            pygame.mixer.Sound.play(hit)
            arrow_x = 1
            arrow_speed=0
            score+=10





        if block_y < 5 or block_y > screen_height - block_height + 5:
            block_speed *= -1

        block_y += block_speed
        arrow_x+= arrow_speed

        # position set - > debug
        if count==-1 :
            gameExit=True

        message_to_screen("score:" +str(score), white,(30,30))
        message_to_screen(str(count), white,(screen_width-150,30))
        display.blit(ar_small,(screen_width-120,27))
        message_to_screen("press q for exit", white,(30,screen_height-40))
        message_to_screen("press space for fire", white,(screen_width-300,screen_height-40))
        rect1=pygame.draw.rect(display, (255, 0, 0), [block_x, block_y, block_width, block_height])
        rect2=pygame.draw.rect(display, (100, 10, 5), [block_x-block_width, block_y+30, block_width,
                                                block_height-60])
        rect3=pygame.draw.rect(display, (black), [block_x-(2*block_width), block_y+45, block_width, block_height-90])
        display.blit(ar_img, (arrow_x, arrow_y))
        
            
        pygame.display.update()

        clock.tick(80)


    pygame.quit()
    quit()


gameLoop()

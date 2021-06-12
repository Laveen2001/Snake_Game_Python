import time
import random
import pygame
Display_size=(800,800)
Dot_size=10
Snake_size=25
Green=(0,222,0)
Red=(222,0,0)
Blue=(0,0,222)
Mix=(222,4,88)
small_size_of_font=22
large_size_of_font=112
pygame.init()
Disp=pygame.display.set_mode(Display_size)
pygame.display.set_caption('SnakeGame')
#Font function
def text_objects(text,font): 
    textSurface=font.render(text,True,Mix)# text,True,colour rgb
    return (textSurface, textSurface.get_rect())
#Score Display function
def ScoreDisp(text):
    largeText = pygame.font.Font('freesansbold.ttf',small_size_of_font)# type of font::
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (Display_size[0]//2,10)
    Disp.blit(TextSurf, TextRect)
    pygame.display.update()
    #time.sleep(1)
#Crash Message display function
def msgdisp(text):
    largeText = pygame.font.Font('freesansbold.ttf',large_size_of_font)# type of font::
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (Display_size[0]//2,Display_size[1]//2)
    Disp.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
#To generate random food
def GenerateFood(a,b):
    pygame.draw.rect(Disp,Red,[a,b,Dot_size,Dot_size])
def snakebase(snake_list):
  #  print(snake_list)
    for i in snake_list:
        pygame.draw.rect(Disp,Blue,[i[0],i[1],Snake_size,Snake_size])
#Main function of game
def game():
    s=0 #Increment in x due to pressing of down arrow key
    t=0 #Increment in y due to pressing of upper arrow key 
    game_over=False
    x=100 # position of snake
    y=44 #positoin of snake
    a=random.randint(0,Display_size[0])# Generating random for food
    b=random.randint(0,Display_size[1])
    score=0
    snake_list=[]
    snake_len=1
    while not game_over:
        # Quit function
        if x<0 or x>Display_size[0]-Snake_size or y<0 or y>Display_size[1]-Snake_size:
            msgdisp('CRASH')
            game_over=True
            pygame.quit()
            quit()
        while a<10 or a>Display_size[0]-100 or b<10 or b>Display_size[1]-100:# If by chance the food is generated at ends then regenerate it so that its visible 
            a=random.randint(0,Display_size[0])
            b=random.randint(0,Display_size[1])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    s-=1
                    t=0        
                if event.key==pygame.K_RIGHT:
                    s+=1
                    t=0                    
                if event.key==pygame.K_UP:
                    t-=1
                    s=0
                if event.key==pygame.K_DOWN:
                    t+=1
                    s=0
        
        Disp.fill(Green)        
        x=x+s # updating the values of x,y after pressing of keys
        y=y+t
        head=[] # the head or inintial box of snake 
        head.append(x)
        head.append(y)
        snake_list.append(head)
        if len(snake_list)>snake_len:
            del snake_list[0]# snakelist contains all x,y values but we only want acc to snake length so we delete remaining ones    
        if head in snake_list[:-1]:# Exit if head touches the another any box of its body;; -1 is used to exclude the head if not done it will always exit as snake_list always contains head
            game_over=True
            msgdisp('CRASH')
        snakebase(snake_list)
        GenerateFood(a,b)
        if a>=x and a+Dot_size<=x+Snake_size and b>=y and b+Dot_size<=y+Snake_size:# if snake touches the food then increase length and also increment the score
            score+=1
            snake_len+=20 # Increment of snake length
            a=random.randint(0,Display_size[0])
            b=random.randint(0,Display_size[1])
            GenerateFood(a,b)
        ScoreDisp('Score:'+str(score))
        pygame.display.flip()
game()

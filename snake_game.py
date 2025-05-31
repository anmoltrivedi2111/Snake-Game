import pygame
import random
import os 

pygame.init()
pygame.mixer.init()

# functions for game audio

def bgmusic():
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play()
    
def gameover_music():
    pygame.mixer.music.load('over.mp3')
    pygame.mixer.music.play()
    
def food_music():
    pygame.mixer.music.load('food.mp3')
    pygame.mixer.music.play()
    

def menushift_music():
    pygame.mixer.music.load('move.mp3')
    pygame.mixer.music.play()
    
# setting display and basic configs

screen_width = 900
screen_height = 600

# images

bg  = pygame.image.load('bg_image.jpg')
bg1 = pygame.image.load('bg_ingame.jpg')




gamewindow = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont(None, 30)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock() 

bg = pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()
bg1 = pygame.transform.scale(bg1,(screen_width,screen_height)).convert_alpha()

pygame.display.update()

# colors 

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

if (not os.path.exists("highscore.txt")):
            with open('highscore.txt','w') as f:
                f.write("0")


# creating functions
# text
def text_screen(text, color, x, y):
    screen_text = font.render(text , True, color)
    gamewindow.blit(screen_text, [x,y])
# snake plotting
def plot_snake(gamewindow,color , snake_list, snake_size,):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x, y, snake_size, snake_size])

def main_window():
    game_exit = False
    bgmusic()
    while not game_exit:
        
        gamewindow.fill(white)
        gamewindow.blit(bg, (0, 0))
        text_screen("Welcome To Snakes ",black, 290,230)
        text_screen("Press Space To Start",black,290,280)   
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gamewindow.fill(white)
                    gamewindow.blit(bg1,(0,0))
                    menushift_music()
                    game_loop()    
        pygame.display.update()     
        clock.tick(30)
            
# game loop

def game_loop():
    #game variables
    
    game_over = False
    game_exit = False

    # Creating snake variables (Main character)
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    fps = 30
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    score = 0
    vel_x = 1
    vel_y = 1
    snake_list = []
    snake_length = 1
    # highscore file reader
    
    with open('highscore.txt','r') as f:
                high_score =f.read()
    

    # main loop by which game runs
    
    while not game_exit:
        
        if snake_x < 0 or snake_x >screen_width or snake_y < 0 or snake_y > screen_height:
            gameover_music()
            game_over = True
            
        if game_over:
            
            
                    
                    
            with open('highscore.txt','w') as f:
                f.write(str(high_score))
                
            gamewindow.fill(white)
            
            
            
            text_screen("Game Over! Press Enter To Continue ", red, 250, 280)      
            text_screen(" Or Press M for Main Menu ", red, 300, 320)
                
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    game_exit =True
                if event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_RETURN:
                        menushift_music()
                        game_loop()     
                    if event.key ==pygame.K_m:
                        main_window()    
                        menushift_music()
            
        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        velocity_x = vel_x
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - vel_x    
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - vel_y
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = vel_y       
                        velocity_x = 0

            
            if abs(snake_x - food_x) <6 and abs(snake_y - food_y) <6:
                food_music()
                score+=1*10
                vel_x+=0.1
                vel_y+=0.1
                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snake_length +=2
                
            #highscore updating
            
                if score>int(high_score):
                    high_score = score
                    
            snake_x+=velocity_x
            snake_y+=velocity_y    
                            
            gamewindow.fill(white)
            text_screen("score : " + str(score) + "  HighScore : " + str(high_score), red, 5,5)
            pygame.draw.rect(gamewindow,red,[food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            
            if len(snake_list) > snake_length:
                del snake_list[0]
                
            if head in snake_list[:-1]:
                game_over = True                
            


            plot_snake(gamewindow,black, snake_list, snake_size)
            
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()    
    quit()    



# function calling
main_window()
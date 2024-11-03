import pygame
import random

# initialize the pygame
pygame.init()

# define the color
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# window size setting
dis_width = 800
dis_height = 600

# define snake size and speed
snake_block = 10
snake_speed = 10

#define the clock and font size
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

#define the snake color
def our_snake(dis, snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def message(dis, msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
#main game definition
def gameLoop(growth):
    game_over = False
    game_close = False

    #initialize basic settings
    snake_length = 1
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = snake_block
    y1_change = 0
    snake_list = [[x1, y1]]
    #define the food location
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # create the game winodw
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Greedy Snake')


    while not game_over:
        #use esc to quit the game
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    game_close = False
            if event.type == pygame.QUIT:
                game_over = True
            #use arrow keys to control the movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
        # define the gameover scene
        while game_close:
            dis.fill(black)
            message(dis, "You Lost! Press Esc-Quit or Space-Play Again", red)
            pygame.display.update()
            #Press Esc to quit or Space to play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop(growth)

        #when game is not over

        #when snake reach the edge, gameover
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        #if snake head touch the snake body, gameover
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(dis, snake_block, snake_list)

        pygame.display.update()
        #eat apple and become longer
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length += growth

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# get the user input number
while True:
    try:
        growth = int(input("Please Enter a random number"))
        if growth < 1:
            raise ValueError("Number must be greater than 0")
        break
    except ValueError as e:
        print(f"Invalid Number: {e}")

gameLoop(growth)
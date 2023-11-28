import pygame
import imageio


# import character / enemy class
from characters.player import *
from characters.enemy import *

# initialize the pygame window
pygame.init()

# set the window size to open to
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = (SCREEN_WIDTH * 0.6)

# window and title for window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Run Tony Run')

# sets game framerate
clock = pygame.time.Clock()
FPS = 60

background_gif_path = 'Jungle.gif'
background_gif = imageio.get_reader(background_gif_path)
# background_gif_frames = [pygame.transform.scale(pygame.surfarray.make_surface(frame), (SCREEN_WIDTH, SCREEN_HEIGHT)) for frame in background_gif]
background_gif_frames = [
    pygame.transform.flip(pygame.transform.scale(pygame.transform.rotate(pygame.surfarray.make_surface(frame), 90), (SCREEN_WIDTH, SCREEN_HEIGHT)), False, True)
    for frame in background_gif
]

frame_index = 0

# player action variables (how we move)
move_left = False
move_right = False
jump = False
move_down = False

# game variables
GRAVITY = 1

# define background as black
BACKGROUND = (0,0,0)
WHITE = (255, 255, 255)

# keep the background refreshing which hides/clears old sprite instances
def background():
    screen.fill(BACKGROUND)

    # makes a line for the floor!
    pygame.draw.line(screen, WHITE, (0, 750), (SCREEN_WIDTH, 750))

# instance of the player class to be used (test instance)
player = Player(200, 200, 0.125, 5)

# set the game with while loop
game_running = True
while game_running:

    clock.tick(FPS)
    background()

    screen.blit(background_gif_frames[frame_index], (0, 0))
    # pygame.draw.line(screen, WHITE, (0, 750), (SCREEN_WIDTH, 750))

    # adds the player sprite to the window (passes the screen to put the image on the screen)
    # player.draw(screen)
    player.move_character(move_left, move_right, jump, move_down)
    player.draw(screen)

    # adds the enemy sprite to the window (passes the screen to put the image on the screen)
        
    for event in pygame.event.get():
        # switches game_running to false and allow user to quit game on closing the window
        if event.type == pygame.QUIT:
            game_running = False

        # key presses by user to control sprite / exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                jump = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_ESCAPE:
                game_running = False

        #key release (aka stop character movement)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                jump = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False

    pygame.display.update()

    frame_index = (frame_index + 1) % len(background_gif_frames)


pygame.quit()
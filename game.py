import pygame
import random
#We initialize pygame, if we don't, we cannot access the methods in pygame
pygame.init()

# create a screen, make sure there are 2 parentheses in set_mode, it's because it requires tuples as arguments
screen = pygame.display.set_mode((800, 600)) # width and height values

#Add a background image
background = pygame.image.load('space.jpg')

#Title and Icon of game window
pygame.display.set_caption("Space Invaders")
'''We access the method set_caption() in the module display in the package pygame
The set_caption() method will set the title of the window as "Space Invaders" '''
icon=pygame.image.load('solar-system.png') #load the image to pygame
pygame.display.set_icon(icon) #set the loaded icon

#Create the player image
player_img=pygame.image.load('spaceship.png') #load the image

'''we create the global variables for the spaceship coordinates for later manipulation
for example, we will move the spaceship up/down/left/right by modifying the coordinates'''
player_x=370
player_y=480
def player(x,y):
    '''we define a function to place the image of the player on the game window
    blit stands for Block Transfer
    —and it's going to copy the contents of one Surface onto another Surface'''
    screen.blit(player_img,(x,y)) #arguments: the image and the tuple of coordinates

#Create the enemy image (similar to creating player)
enemy_img=pygame.image.load('ufo.png')
enemy_x=random.randint(0,736)
enemy_y=random.randint(50,150)
def enemy(x,y):
    screen.blit(enemy_img,(x,y))

#Create the bullet image
bullet_img=pygame.image.load('missile.png')
bullet_x=player_x
bullet_y=player_y

#Define moving variables:
left=0
right=0
up=0
down=0
enemy_vertical_move=0
enemy_horizontal_move=0.3
#Define bullet variables
bullet_move=3 #the pixels bullet moves each iteration
bullet_state="Off" #Initializing bullet state, bullet has on/off state
def bullet(x,y): #(x,y) is the coordinates of the spaceship
    global bullet_state #if we don't add keyword global, Python will create a local variable with the same name inside of this function
    bullet_state = "On"
    screen.blit(bullet_img,(x+16,y+10)) #we want the bullet to come out of the nose of the spaceship

def bullet_reload(x,y):
    global bullet_x,bullet_y,bullet_state
    bullet_x = x
    bullet_y = y
    bullet_state = "Off"

#Game loop
running=True
while running: #each iteration is a picture frame, changing picture frames give the animation
    screen.fill((50,0,100)) #fill the window with a RGB color
    screen.blit(background,(0,0)) #place background image on the window
    for event in pygame.event.get():
        '''Each "while iteration", the "for loop" will loop through all the events
        (which are the player interactions with the game windows)
        pygame.event.get() returns the list of all events
        happening inside the game window
        pygame.event.get() is translated as we access the module
        event, then access the function/method get()
        An event is anything that happens inside the game window, anykind of input control
        Event examples: when we move/click the mouse, type anything in the keyboard'''
        if event.type == pygame.QUIT: # the event that quit button is clicked
            '''learn the syntax here
            event.type means we access the attribute "type" in the object "event"
            pygame.QUIT means we access the attribute QUIT in the module pygame'''
            running = False
        if event.type == pygame.KEYDOWN: # the event of a keystroke (or pressing a key on keyboard, while KEYUP is releasing the key)
            if event.key == pygame.K_LEFT:
                left=0.5
            elif event.key == pygame.K_RIGHT:
                right=0.5
            elif event.key == pygame.K_UP:
                up=0.5
            elif event.key == pygame.K_DOWN:
                down=0.5
            elif event.key == pygame.K_SPACE:
                if bullet_state == "Off":
                    bullet_reload(player_x,player_y)
                bullet(player_x,player_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left=0
            elif event.key == pygame.K_RIGHT:
                right=0
            elif event.key == pygame.K_UP:
                up=0
            elif event.key == pygame.K_DOWN:
                down=0
    player_x = player_x + right - left
    player_y = player_y + down - up
    #adding boundaries to our spaceship
    if player_x<=0:
        player_x=0
    elif player_x>=736:
        player_x=736
    if player_y<=0: #be cafeful, do not use elif on this line or there'll be a bug
        player_y=0
    elif player_y>=536:
        player_y=536

    enemy_x = enemy_x + enemy_horizontal_move
    enemy_y = enemy_y + enemy_vertical_move
    if enemy_x<=0 or enemy_x>=736:
        enemy_horizontal_move=enemy_horizontal_move*-1
        enemy_vertical_move=random.randint(1,10)/100
    if enemy_y>=600:
        enemy_x=random.randint(0,736)
        enemy_y=random.randint(50,150)
    
    if bullet_state=="On":
        bullet(bullet_x,bullet_y)
        bullet_y-=bullet_move
        if bullet_y<=0:
            '''there's a bug when I set the condition at bullet_y==0, it's because the spaceship y-step is 0.5.
            So, there are cases that the bullet_y will not be 0, causing it not reload'''
            bullet_reload(player_x,player_y)
    
    enemy(enemy_x,enemy_y)
    player(player_x,player_y)

    pygame.display.update() #this makes sure the game window updates the changes we add at the end of each iteration



#1:27:00
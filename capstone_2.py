#This program is a simple game loop in pygame that includes:
#1. One player character that can move in all four directions.
#2. One weapon object.
#3. Four kinds of enemy objects attacking from different positions.
#4. Two kinds of reward objects.
#5. Score and life counters.
#6. Intro, directions, playing, win, and game-over screens that loop into each other.


#Note: all code used is based on "example.py" in Hyperiondev, 2021, Task 15, except where otherwise referenced.
#All images and fonts are my own work.




#First, "pygame", "random", and "time" modules are imported, and a number of variables defined.


import pygame
import random
import time

#The pygame module is initialized using "pygame.init()":
pygame.init()

#"screen_width" and "screen_height" will define the size of the pygame screen and help control player/enemy movement:
screen_width = 1366
screen_height = 768

#Using "pygame.display.set_mode((x,y))" (Pygame.org, 2021, pygame.display, t.ly/LWuy),
#a screen surface "screen" with dimensions "screen_width" x "screen_height" is created:
screen = pygame.display.set_mode((screen_width,screen_height))

#"color" is defined as white, using the pygame RGB color code "255",
#and "screen" is filled with white using "x.fill(y)"
#(Petercollingridge.co.uk, 2010, Creating a Pygame Window, t.ly/b22U):
color = (255,255,255)
screen.fill(color)

#We want the visible score and life amounts to change, and creating surfaces for each possible number is too much work,
#so a font is imported using "pygame.font.Font("x",y)" (Pygame.org, 2021,pygame.font, t.ly/ityA):
font = pygame.font.Font("game_font.ttf", 27)

#We don't want the mouse pointer to be visible on the game screen, so "pygame.mouse.set_visible()" is set to "False"
#(Pygame.org, 2021, pygame.mouse, t.ly/ZE6U):
pygame.mouse.set_visible(False)

#All images used in the game are uploaded as surfaces using "pygame.image.load("x")":
intro = pygame.image.load("intro.png")
direct = pygame.image.load("direct.png")
jones = pygame.image.load("jones_walk2.png")
bullet = pygame.image.load("bullet.png")
skull = pygame.image.load("skull.png")
bat = pygame.image.load("bat.png")
like = pygame.image.load("like.png")
knife = pygame.image.load("knife.png")
wine = pygame.image.load("wine.png")
jug = pygame.image.load("jug.png")
wall = pygame.image.load("wall.png")
lose = pygame.image.load("lose.png")
win = pygame.image.load("win.png")
life = pygame.image.load("life.png")
score_count = pygame.image.load("score_count.png")

#Using "x.get_height()" and "x.get_width()", height and width variables are declared for all images/surfaces.
#These will help control player and enemy position/movement:
jones_height = jones.get_height()
jones_width = jones.get_width()

bullet_height = bullet.get_height()
bullet_width = bullet.get_width()

skull_height = skull.get_height()
skull_width = skull.get_width()

knife_height = knife.get_height()
knife_width = knife.get_width()

bat_height = bat.get_height()
bat_width = bat.get_width()

like_height = like.get_height()
like_width = like.get_width()

life_height = life.get_height()
life_width = life.get_width()

wine_height = wine.get_height()
wine_width = wine.get_width()

jug_height = jug.get_height()
jug_width = jug.get_width()

wall_height = wall.get_height()
wall_width = wall.get_width()

score_count_height = score_count.get_height()
score_count_width = score_count.get_width()

#Three Boolean variables are declared "False".
#They will control the game state:
enter = False
playing = False
winning = False




#Next, the main game loop is started using a "while True".
#The main loop contains four game states, or smaller while loops, controlled by the three Boolean variables above.
#They are: introduction, playing, win, and game-over states.


while True:

        #A) While "enter", "playing", and "winning" are false, the game is in it's introduction state.        
        while (enter == False) and (playing == False) and (winning == False):


                #1. A number of variables are declared that will reset default player and enemy positions, scores, lives etc. when the game restarts. 

                #The default x and y positions (i.e. the left and top boundaries) of all the images/surfaces are declared
                #(x = 0 and y = 0 are respectively the left and top boundaries of the screen):                
                introXPosition = 0
                introYPosition = 0

                directXPosition = 0
                directYPosition = 0

                winXPosition = 0
                winYPosition = 0

                loseXPosition = 0
                loseYPosition = 0

                jonesXPosition = 100
                jonesYPosition = 50
                
                #Note: The bullet's position is set relative to Jones' position
                #(we want it to move with Jones and remain hidden while not shot):
                bulletXPosition = jonesXPosition + 100
                bulletYPosition = jonesYPosition + 84
                
                #Note: "random.randint(x,y)" is used so enemy and reward objects will appear from random y positions between "x" and "y"
                #(W3schools.com, 2021, Python Random randint() Method, t.ly/L1fR):               
                skullXPosition = screen_width
                skullYPosition = random.randint(0, screen_height - skull_height)
        
                knifeXPosition = screen_width
                knifeYPosition = random.randint(0, screen_height - knife_height)

                wineXPosition = screen_width
                wineYPosition = random.randint(0, screen_height - wine_height)

                batXPosition = screen_width 
                batYPosition = 350
                
                #Note: The like icon's position is set relative to the bat's position.
                #We want it to move with the bat and remain hidden:                
                likeXPosition = batXPosition + 50
                likeYPosition = batYPosition + 50

                wallXPosition = screen_width
                wallYPosition = 0

                jugXPosition = screen_width + 250
                jugYPosition = 300
                
                lifeXPosition = 1200
                lifeYPosition = 6

                score_countXPosition = 10
                score_countYPosition = 2

                #Life and score counter variables are set to default values:
                lives = 3
                score = 0

                #"batmove_y" and "hitcounter" are declared to respectively control the up and down movement of the bat boss,
                #and count how many times it has been hit by a bullet:
                batmove_y = 2
                hitcounter = 0

                #Key-command variables for arrow and spacebar keys are set to "False".
                #They will control player and weapon movement:
                keyUp = False
                keyDown = False
                keyRight = False
                keyLeft = False
                keySpace = False



                #2. "x.blit(y, (yx, yy))" is used to place the intro-screen image "intro" onto "screen" at its default x and y position.        
                #After blitting, the screen still needs to update using "pygame.display.flip()" (Pygame.org, 2021, pygame.display, t.ly/TkS9)
                #The name of the game is now displayed along with a message prompting the user to enter any key to start:
                screen.blit(intro, (introXPosition, introYPosition))
                pygame.display.flip()
                


                #3. A small event loop to control keyboard and mouse events is set up for the introduction state,
                #using "for event in pygame.event.get():",
                for event in pygame.event.get():

                        #If the event is "pygame.QUIT" (i.e. closing the pygame window - ninMonkey, 2012, Stackoverflow.com, t.ly/1zqX),
                        #the pygame module is closed ("pygame.quit()") and the program exited ("exit()"):
                        if event.type == pygame.QUIT:                                
                                pygame.quit()                                
                                exit()
                                
                        #If the event is a keyboard key that is pressed down ("pygame.KEYDOWN"),
                        if event.type == pygame.KEYDOWN:

                                #if the key pressed ("event.key") is escape ("pygame.K_ESCAPE") (Pygame.org, 2021, pygame.key, t.ly/Y2E6),
                                #the pygame module is closed, and the program exited:
                                if event.key == pygame.K_ESCAPE:                                        
                                        pygame.quit()                                        
                                        exit()
                                        
                                #if the key pressed is NOT escape, the game is started,
                                #and the directions-screen is displayed for three seconds using "time.sleep(x)" (Driscoll, 2021, Realpython.com, t.ly/P8ml).
                                #"enter" and "playing" are changed to "True", and the introduction state loop is terminated:
                                if event.key != pygame.K_ESCAPE:                                       
                                        screen.blit(direct, (directXPosition, directYPosition))                                      
                                        pygame.display.flip()                                       
                                        time.sleep(3) 
                                        enter = True 
                                        playing = True                                        
                                        


                        
        #B) While "enter" and "playing" are true, but "winning" is false, the game is now in its playing state.
        while (enter) and (playing) and (winning == False):

                #1. All images, players, enemies, and rewards are blitted to their default x and y positions.
                #As these positions change, they will be re-blitted to their new (current) positions every time the game loops.
                #Again "pygame.display.flip()" is included last to update the screen to all latest x and y positions:
                screen.fill(color)
                screen.blit(life, (lifeXPosition, lifeYPosition))
                screen.blit(score_count, (score_countXPosition, score_countYPosition))
                screen.blit(bullet, (bulletXPosition, bulletYPosition))
                screen.blit(jones, (jonesXPosition, jonesYPosition))
                screen.blit(wine, (wineXPosition, wineYPosition))
                screen.blit(skull, (skullXPosition, skullYPosition))
                screen.blit(knife, (knifeXPosition, knifeYPosition))
                screen.blit(jug, (jugXPosition, jugYPosition))
                screen.blit(wall, (wallXPosition, wallYPosition))
                screen.blit(like, (likeXPosition, likeYPosition))
                screen.blit(bat, (batXPosition, batYPosition))
                #Note: "x.render(z, b, c)" (Pygame.org, 2021, pygame.font, t.ly/gWop) is used to create "textsurface" and "textsurface2",
                #which will display the changing "score" and "lives" variables in the font uploaded earlier ("font")
                #(RGB color code "0,0,0" is used for black - Riptutuorial.com, Pygame The Complete Code, t.ly/n2T2):
                textsurface = font.render(str(score), False, (0,0,0,))
                screen.blit(textsurface, (170, 6))
                textsurface2 = font.render("X " + str(lives), False, (0,0,0,))
                screen.blit(textsurface2, (1250, 15))       
                pygame.display.flip()


        
                #2. The main event loop for the playing state is set up.
                for event in pygame.event.get():

                        #if the window is closed, pygame is closed and the program exited:     
                        if event.type == pygame.QUIT:                               
                                pygame.quit()                               
                                exit()
                                
                        #if a key is pressed down,       
                        if event.type == pygame.KEYDOWN:
                                
                                #if the key is escape, pygame is closed and the program exited: 
                                if event.key == pygame.K_ESCAPE:                                        
                                        pygame.quit()                                        
                                        exit()
                                        
                                #if the key is one of the arrow keys or spacebar,
                                #the key-command variables defined earlier are changed to "True":
                                if event.key == pygame.K_UP:
                                        keyUp = True                                        
                                if event.key == pygame.K_DOWN:
                                        keyDown = True                                       
                                if event.key == pygame.K_RIGHT:
                                        keyRight = True                                        
                                if event.key == pygame.K_LEFT:
                                        keyLeft = True                                       
                                if event.key == pygame.K_SPACE:
                                        keySpace = True
                                        
                        #if the event is a key being lifted ("pygame.KEYUP"),
                        if event.type == pygame.KEYUP:
                                
                                #if the key is one of the arrow keys, the key-command variables are changed back to "False"
                                #(Note: the same is not done for spacebar as we want the weapon to behave differently):
                                if event.key == pygame.K_UP:
                                        keyUp = False                                        
                                if event.key == pygame.K_DOWN:
                                        keyDown = False                                        
                                if event.key == pygame.K_RIGHT:
                                        keyRight = False                                        
                                if event.key == pygame.K_LEFT:
                                        keyLeft = False



                #3. Player and weapon movement are determined:
             
                #If the up-arrow key is pressed (i.e. if "keyUp" is True),
                #if the player's y position is lower than the screen top (i.e. > 0),
                #the the player will move up (y -=1.5) until it reaches the screen top
                #(Note, the bullet needs to move with the player to remain concealed):                
                if keyUp == True:
                        if  jonesYPosition > 0:
                                jonesYPosition -=1.5
                                bulletYPosition -=1.5
                                
                #The same statement is repeated for the other arrow keys,
                #using the player and screen height/width variables to keep the player from going off the screen:               
                if keyDown == True:
                        if  jonesYPosition < screen_height - jones_height:
                                jonesYPosition +=1.5
                                bulletYPosition +=1.5
                                
                if keyRight == True:
                        if  jonesXPosition < screen_width - jones_width:
                                jonesXPosition +=1.5
                                bulletXPosition +=1.5
                                
                if keyLeft == True:
                        if jonesXPosition > 0:
                                jonesXPosition -=1.5
                                bulletXPosition -=1.5

                #If spacebar is not being pressed ("keySpace" = False), the bullet remains hidden behind the player:
                if keySpace == False:
                        bulletXPosition = jonesXPosition + 100
                        bulletYPosition = jonesYPosition + 84
                        
                #If spacebar is pressed ("keySpace" = True), the bullet moves to the right of the screen:
                if keySpace == True:
                        bulletXPosition +=2.5

                #(Note: If the arrow keys are lifted, their key-command variables change back to "False" and the player stops moving.
                #If however, the space key is lifted the bullet continues moving.
                #The rest of the space key/bullet behavior will be determined later.)



                #4. To dictate collision behavior, rectangle surfaces are created around the player/weapon/enemy/reward surfaces,
                #using "x.get_rect()", which defines a rectangle the size of surface/image "x".
                #The rectangles' top and left hand sides are then assinged the values of the player's/weapon's/enemy's/reward's
                #y and x positions respectively, so the rectangle and character surfaces will move together:
                jonesBox = jones.get_rect()
                jonesBox.top = jonesYPosition
                jonesBox.left = jonesXPosition
        
                bulletBox = bullet.get_rect()
                bulletBox.top = bulletYPosition
                bulletBox.left = bulletXPosition

                wineBox = wine.get_rect()
                wineBox.top = wineYPosition
                wineBox.left = wineXPosition
                
                skullBox = skull.get_rect()
                skullBox.top = skullYPosition
                skullBox.left = skullXPosition

                knifeBox = knife.get_rect()
                knifeBox.top = knifeYPosition
                knifeBox.left = knifeXPosition
                
                batBox = bat.get_rect()
                batBox.top = batYPosition
                batBox.left = batXPosition

                likeBox = like.get_rect()
                likeBox.top = likeYPosition
                likeBox.left = likeXPosition

                wallBox = like.get_rect()
                wallBox.top = wallYPosition
                wallBox.left = wallXPosition
                
                jugBox = jug.get_rect()
                jugBox.top = jugYPosition
                jugBox.left = jugXPosition



                #5. Then, collision behavior is set up.
                
                #5.1 First, for collision betweeen the player and enemy boxes:
                
                #If the player's x position is greater than minus one (to prevent life loss while the player has just lost a life and is still off screen),
                if jonesXPosition > -1:

                        #if the skull, knife, or like-icon boxes collide with the player box,
                        #the player disappears off the screen to the left, and one is subtracted from "lives" (displayed in the chosen font via "textsurface2"):
                        if (skullBox.colliderect(jonesBox) or knifeBox.colliderect(jonesBox) or likeBox.colliderect(jonesBox)):
                                jonesXPosition = 0 - 200
                                jonesYPosition = 50
                                lives -= 1
                             
                        #if the wine box collides with the player box,
                        #the wine is sent back off the screen to the right, and one is added to "lives":
                        if wineBox.colliderect(jonesBox):
                                wineXPosition = (0 - wine_width)
                                lives += 1

                #If the bat or wall box collide with the player box, all lives are lost (game over):                                
                if batBox.colliderect(jonesBox) or wallBox.colliderect(jonesBox):
                        lives -= lives

                #If the player box collides with the wine jug box, the jug disappears off screen to the right,
                #"playing" changes to false, "winning" changes to true, and the playing-state loop is discontinued:
                if jonesBox.colliderect(jugBox):
                        jugXPosition = screen_width
                        playing = False
                        winning = True
                        
                                  
                #5.2 Second, for collision between the bullet and enemy boxes:

                #If the player is on screen (x > -1), and the bullet is between the player's right side and the right of the screen, 
                #(done to keep the bullet "active" only when fired and still on the screen),
                if jonesXPosition > -1 and (bulletXPosition > (jonesXPosition + jones_width)) and bulletXPosition < screen_width:

                        #if the bullet box collides with the skull box,
                        #the bullet resets to its default position behind the player ("keySpace" = False),
                        #the skull resets to its default position off the screen to the right,
                        #and "score" increases by one (displayed on screen in the chosen font using "textsurface"):
                        if bulletBox.colliderect(skullBox):                  
                                keySpace = False
                                skullXPosition = screen_width
                                skullYPosition = random.randint(0, screen_height - skull_height)
                                score += 1
                                
                        #if the bullet box collides with the like-icon box,
                        #the bullet resets to its default position behind the player ("keySpace" = False),
                        #the like icon disappears to its default position behind the bat,
                        #and "score" is increase by ten:
                        if bulletBox.colliderect(likeBox):
                                keySpace = False
                                likeXPosition = batXPosition + 50
                                likeYPosition = batYPosition + 50
                                score += 10
                                
                        #if the bullet box collides with the bat box,
                        #the bullet resets to its default position, the score is increased by two,
                        #and "hitcounter" is increased by one (when it reaches five, the bat is defeated):
                        if bulletBox.colliderect(batBox):
                                keySpace = False
                                score += 2
                                hitcounter += 1

                #If the bullet is off the screen to the right, it resets to its default position ("keySpace" = False):
                if bulletXPosition > screen_width:
                        keySpace = False



                #6. Enemy movement is determined.

                #Enemy and reward movements change during the course of the game, 
                #so three substates within the playing state are created to control these movements.
                               
                #6.1 If "score" and "hitcounter" are under five (normal substate),
                if score < 5 and hitcounter < 5:
                        
                        #If the wine's x position is greater than -5000 (-5000 to delay how frequently it appears),
                        #the wine moves to the left. Else, it resets to its default position off screen to the right:
                        if wineXPosition > (0 - 5000):
                                wineXPosition -= 1
                        else:
                                wineXPosition = screen_width
                                wineYPosition = random.randint(0, screen_height - wine_height)

                        #The same method is repeated for the for the skull and knife
                        #(their minimum x positions set to zero minus their width, so they appear to slide off the screen):
                        if skullXPosition > (0 - skull_width):
                                skullXPosition -= 1.5
                        else:
                                skullXPosition = screen_width
                                skullYPosition = random.randint(0, screen_height - skull_height)

                        if knifeXPosition > (0 - knife_width):
                                knifeXPosition -= 2
                        else:
                                knifeXPosition = screen_width
                                knifeYPosition = random.randint(0, screen_height - knife_height)


                #6.2 If "score" is five and above, and "hitcounter" is under five (boss-stage substate),
                if score >= 5 and hitcounter < 5:

                        #To make the bat move up and down within the boundaries of the screen,
                        #its y position is increased by "batmove_y" (set earlier to "2").
                        #If the bat goes off the screen (y < 0 or y > screen height minus bat height),
                        #"batmove_y" is multiplied by minus one, thus changing the direction of the movement
                        #(Rabbid76, 2020, Stackoverflow.com, t.ly/uVB7): 
                        batYPosition += batmove_y
                        if batYPosition < 0 or batYPosition > screen_height - bat_height:
                                batmove_y *= -1

                        #To make the bat, wall, and wine jug slide onto the screen from the right, their final x-positions are used as limiters
                        #(if they are right of their final x positions, they keep moving left): 
                        if batXPosition > 600:
                                batXPosition -= 3
                                                    
                        if wallXPosition > 1000:
                                wallXPosition -= 1
                                
                        if jugXPosition > 1250:
                                jugXPosition -= 1

                        #Because the enemies and rewards from the previous sub-state might still be on screen,
                        #they continue to move left until they are off screen:
                        if wineXPosition > 0 - wine_width:
                                wineXPosition -= 1

                        if skullXPosition > 0 - skull_width:
                                skullXPosition -= 1.5
                        
                        if knifeXPosition > 0 - knife_width:
                                knifeXPosition -= 2

                        #We want bonus points and lives awarded if the bat boss is defeated.
                        #"bonus" and "bonus_lives" are thus assigend values equal to the currect score and lives,
                        #plus 500 and two respectively:
                        bonus = score + 500
                        bonus_lives = lives + 2
                        
                #If the like-icon's x position is smaller than 750 (which it is by default), but larger than zero minus its width, 
                #it continues moving left. Else, it is set back to its default position behind the bat.
                #(Note: the like-icon's movement is defined outside the boss-stage substate's if statements above,
                #to make it continue moving even after the boss is defeated.)
                if likeXPosition < 750 and likeXPosition > 0 - like_width:
                        likeXPosition -= 4
                else:
                        likeXPosition = batXPosition + 50
                        likeYPosition = batYPosition + 50


                #6.3 If "score" and "hitcounter" are five and greater (boss-defeated substate)
                #(i.e. as soon as the bat boss is shot five times),
                if score >= 5 and hitcounter >= 5:

                        #If "score" is smaller than "bonus" (which it will be), "score" is increased by one,
                        #until it reaches "bonus" (i.e. the user's score plus 500)
                        #(Note: increase can be seen on screen via "textsurface"):
                        if score < bonus:
                                score += 1
                                
                        #Similarly, if "lives" is smaller than "bonus_lives", "lives" is increased by one,
                        #until it reaches "bonus_lives" (i.e. the user's lives plus two):
                        if lives < bonus_lives:
                                lives += 1
                                
                        #Sometimes the skull is still present at even after the boss is defeated,
                        #so it is guided to the left until off screen (zero minus the skull width):
                        if skullXPosition > 0 - skull_width:
                                skullXPosition -= 1.5
                                                
                        #The wall is moved up to make the final reward item (the wine jug) accessible,
                        #and the bat is moved off screen to the right:
                        wallYPosition -= 1
                        batXPosition = screen_width


                        
                #7. For the entire playing state, if the lives are less than one, 
                #"playing" and "winning" are set to "False", but "enter" is still true, and the game switches to its game-over state:
                if lives < 1:
                        playing = False
                        winning = False
                       


                
        #C) If the player won the game, "enter" and "winning" are true, but "playing" is false.
        #The game is in its winning state.

        #While in the winning state,
        while (enter) and (playing == False) and (winning):
                
                #The winning screen image is blitted into place and the display updated (the player is asked if they would like to play again):        
                screen.blit(win, (winXPosition, winYPosition))
                pygame.display.flip()
                
                #A small event loop is created,               
                for event in pygame.event.get():
                        
                        #if user clicks close, pygame is closed and the program is quit.               
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()

                        #if the event is a keyboard key being pressed,
                        if event.type == pygame.KEYDOWN:
                                
                                #if the key is escape, pygame is closed and the program is quit:                               
                                if event.key == pygame.K_ESCAPE:
                                        pygame.quit()
                                        exit()
                                        
                                #if the key is "y" ("pygame.K_y" - Pygame.org, 2021, pygame.key, t.ly/SlCd),
                                #(i.e. the player wants to play again), "winning" and "enter" are set to "False",
                                #and the game thus looped back to the introduction state:
                                if event.key == pygame.K_y:
                                        winning = False
                                        enter = False
                                        
                                #if the key is "n" ("pygame.K_n" - Pygame.org, 2021, pygame.key, t.ly/SlCd),
                                #(i.e. the player wants to quit), pygame is closed and the program is quit:
                                if event.key == pygame.K_n:
                                        pygame.quit()
                                        exit()




        #D) If the player lost all their lives, "playing" and "winning" change to "False",
        #but "enter" is still true, so the game is in its game-over state.

        #While in the game-over state:
        while (enter) and (playing == False) and (winning == False):
                
                #The game-over screen is blitted into position and the display flipped (the player is asked if they would like to play again):        
                screen.blit(lose, (loseXPosition, loseYPosition))
                pygame.display.flip()

                #Another event loop is created exactly as above in the winning state,
                #taking the user back to the introduction state ("enter = False") if they choose "y":                
                for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                                
                        if event.type == pygame.KEYDOWN:

                                if event.key == pygame.K_ESCAPE:
                                        pygame.quit()
                                        exit()

                                if event.key == pygame.K_y:
                                        enter = False

                                if event.key == pygame.K_n:
                                        pygame.quit()
                                        exit()

        


                                                        
######################### THE END ##############################

                
        

    
    
            
        


    

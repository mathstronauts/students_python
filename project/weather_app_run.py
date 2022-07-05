# import libraries
import pygame
import mathstropy

# import files
import app_data
import app_screen
import app_text

#--------------------------------------------------------
# initialize pygame
pygame.init()

# define screen WIDTH and HEIGHT
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(BLACK)  # start with a black screen

# call API data functions
weather_data = app_data.getWeather()

# initialize display text
text = mathstropy.TextDisplay(screen)
textinput = app_data.textinput

# APP LOOP
running = True
while running:
    # detecting events
    events = pygame.event.get()
    for event in events:
        # close pygame window
        if event.type == pygame.QUIT:
            running = False
            
        # check if ENTER key pressed and refresh city data
        keypressed = pygame.key.get_pressed()  # returns key pressed
        if keypressed[pygame.K_RETURN]:  # if enter key pressed
            weather_data = app_data.getWeather()

    #----------------------------------------
    # draw screen
    # app_screen.screen_refresh(screen)
    app_screen.update_screen(screen, weather_data)

    #-----------------------------------------
    # display text
    app_text.update_weather_data(text, weather_data)

    #-----------------------------------------
    #draw textbox
    textinput.update(events)
    textbox = textinput.get_surface()
    textboxRect = (25, 20) 
    screen.blit(textbox, textboxRect)
    
    #------------------------------------------
    # update screen
    pygame.display.flip()

# close app window
pygame.quit()
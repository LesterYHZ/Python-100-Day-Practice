import pygame as pg

def main():
    # Initialization
    pg.init()
    # Set the window geometry
    screen = pg.display.set_mode((800,600))
    # Title
    pg.display.set_caption('Big eats Small')
    """
    We can directly draw a circuit on the screen

    # Draw a circle
    pg.draw.circle(screen,(255,0,0),(100,100),30,0)

    or we can add images onto the screen
    
    # Load image
    ball_image = pg.image.load('./res/wrecking-ball.jpg')
    # Put image on the screen
    screen.blit(ball_image,(0,0))
    
    # Refresh the window to show the circle
    pg.display.flip()
    """
    x,y = 50,50
    running = True
    # Start a loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # Color
        screen.fill((255,255,255))
        pg.draw.circle(screen,(255,0,0),(x,y),30,0)
        # Refresh window
        pg.display.flip()
        # Alter the ball position and then refresh window every 50 ms
        pg.time.delay(50)
        x,y=x+5,y+5

if __name__ == '__main__':
    main()
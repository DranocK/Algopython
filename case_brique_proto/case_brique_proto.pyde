ballX = 0
ballY = 0

ballspeedX = 2
ballspeedY = 4
ballRadius = 8
racketWidht= 50
racketX= 0
racketY= 0



def setup():
    #on dit qu'on va faire appel à la variable ballX et ballY
    global ballX, ballY, ballspeedX, ballspeedY, ballRadius, racketX, racketY, racketWidht
    
    size(800, 500)
    
    
    ballX = width/2
    ballY = height/2
    
    racketY= height - 20
    racketX= mouseX - (racketWidht/2)
    
def draw() :
    clear()
    fill(255)
    
    drawRacket()
    drawBall()
    
    
def drawRacket():
    global racketX ,racketY ,racketWidht
    #draw a rectangle in coords
    #x : mouseX minus half of width
    #y : height of the windows minus 20
    # width : 50
    # height : 10
    racketX = mouseX - (racketWidht/2)
    rect(racketX ,racketY ,racketWidht ,10)
    
    
def drawBall():
    global ballX, ballY, ballspeedX, ballspeedY, ballRadius, racketX ,racketY ,racketWidht
    #draw circel centered on window
    #fill to color the next thing
    fill(255, 0, 0)
    circle(ballX ,ballY ,ballRadius*2);
    #ballX = ballX + speedX
    #ballY = ballY + speedX
    # idem a ce qu'il ya au dessus
    ballX+= ballspeedX
    ballY+= ballspeedY
    
    #gauche
    if(ballX - ballRadius < 0):
        ballspeedX *= -1
        ballX = ballRadius
    #droite
    elif(ballX + ballRadius > width):
        ballspeedX *= -1
        ballX = width-ballRadius
    #haut
    if(ballY - ballRadius < 0):
        ballspeedY *= -1
        ballY = ballRadius
    #bas
    elif(ballY + ballRadius > height):
        print("game over")
        
    #rebon racket
    if(ballY >= racketY-8):
        if(racketX<=ballX<=racketX+racketWidht):
            ballspeedY *= -1
    

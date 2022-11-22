#globale variabler 

#liste over alle punkter vores slange optager
longSnake = []

#bestemmer hvor lang vores slange skal være,
#før vi sletter den ældste del af slangen.
snakeSize = 0

#bestemmer hvilken retning slangen bevæger sig
dir = PVector(0, 0)

#slange mad
food = PVector(0, 0)

def setup():
    global longSnake, food, snakeSize
    size(190, 190)
    
    #bestemmer hvor lang vores slange skal være,
    #før vi sletter den ældste del af slangen.
    snakeSize = 3
    
    #Da vores logik er bundet til frameraten, kan vi
    #forøge hastigheden ved at hæve vores framerate.
    #prøv det
    frameRate(4)
    
    #vi tilføjer den første del af vores slange
    longSnake.append(PVector(9*10, 9*10))
    
    #vi finder et tilfældig sted at ligge noget
    #mad til vores slange
    #food = PVector(40,40)
    food = PVector(floor(random(0,18))*10, floor(random(0,18))*10)
    
    dir = PVector(0, 0)

def draw():
    global longSnake, food, snakeSize
    
    background(0)
    
    #tegner maden
    fill(255,0,0)
    rect(food.x, food.y, 10, 10)
    #rect(80, 80, 10, 10)
    
    #har tilføjer vi et extra segment af vores slange,
    #i den retning vi bevæger os i
    longSnake.append(PVector(
    longSnake[len(longSnake)-1].x + dir.x*10, 
    longSnake[len(longSnake)-1].y + dir.y*10))
    
    #går igennem vært segment af vores slange
    #og tegner den.
    fill(255)
    for i in range(len(longSnake)-1, 0, -1):
        rect(longSnake[i].x, longSnake[i].y,10,10)
        
        #kollision detection for vores slange,
        #her tjekker vi om hovedt at vores slange
        #rammer sig selv
        if longSnake[len(longSnake)-1].x == longSnake[i].x and longSnake[len(longSnake)-1].y == longSnake[i].y and i < len(longSnake)-1:
            
            #vi fjerner alle dele af vores slange,
            #og sætter den tilbage til sin start 
            #position
            longSnake = []
            longSnake.append(PVector(9*10, 9*10))
            snakeSize = 3
            #break kan vi bruge til at breake ud af
            #vores for-loop, uden at gøre det færdigt
            break
    
    #kollision detection for vores mad.
    #her tjekker vi om slangens hoved er det
    #samme sted som maden
    if food.x == longSnake[len(longSnake)-1].x and food.y == longSnake[len(longSnake)-1].y:
        
        #vi flytter vores med et nyt sted
        food = PVector(floor(random(0,18))*10, floor(random(0,18))*10)
        
        snakeSize += 1
    
    
    #vi fjerner den ældste del
    #af vores slange, så det ser ud som om
    #den bevægersig
    
    if len(longSnake) >= snakeSize:
        longSnake.pop(0)

#læser keyboarded, og sætter retningen for
#vores slange
def keyPressed():
    if key == CODED:
        #"dir.y != 1" vi forhinder slangen i at
        #gå bæglens
        if keyCode == UP and dir.y != 1:
            dir.y = -1
            dir.x = 0
        elif keyCode == DOWN and dir.y != -1:
            dir.y = 1
            dir.x = 0
        elif keyCode == LEFT and dir.x != 1:
            dir.x = -1
            dir.y = 0
        elif keyCode == RIGHT and dir.x != -1:
            dir.x = 1
            dir.y = 0

"""ideer til udfordringer:
//1. hæv hastigheden vær gang slangen finder mad
//2. styr slangen med musen
//3. hvis slangen rammer kanten af vinduet
//    reset spillet  
//4. SVÆR! forhindre maden af spawne et sted hvor slangen
//    allerede er
//5 SVÆR! hvis slangen rammer kanten af vinduet
//    skal den dukke op fra den anden side
"""

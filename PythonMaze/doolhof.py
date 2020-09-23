import turtle

# Constanten voor doolhof cellen voor te stellen
GANG=0
MUUR=1
DOEL=3
TOKEN=2

# class env to group static variables
class environment:
    blokskes=[]
    doolhof=[]
    start=(0,0)
    s=(0,0)
    e=(0,0)
    cv=None
    w=0
    h=0
    dh=0
    dw=0
    cw=0
    ch=0
    
env=environment()


 
def lees_doolhof(path):
    """
    Lees een doolhof in uit een bestand
    :param path: bestand dat het doolhof bevat
    :return: (doolhof,s,e): doolhof is een matrix, s en e zijn (rij,kolom) posities
    """
    f=open(path)

    doolhof=[]
    rijnr=0
    lengte=0
    for line in f:
        if lengte==0:
            lengte=len(line)-1
        elif lengte!=len(line)-1:   # negeer lijnen die niet dezelfde lengte hebben als de eerste lijn uit het bestand
            continue
        rij=[]
        kolomnr = 0
        for x in line[:-1]:  # Skip \n die elke lijn afsluit
            if x==' ':  # spaties, start en eind positie duiden een gangpositie aan
                rij.append(GANG)
            elif x=='S':
                s=(rijnr,kolomnr)
                rij.append(TOKEN)
            elif x=='E':
                e=(rijnr,kolomnr)
                rij.append(DOEL)
            else:
                rij.append(MUUR)
            kolomnr+=1
        doolhof.append(rij)
        rijnr+=1

    f.close() # sluit het bestand

    return (doolhof,s,e)

def draw_doolhof(cv,doolhof):
    global env
    for l in env.blokskes:
        cv.delete(l)
    env.blokskes=[]
    
    j = 0
    for row in doolhof:
        i = 0
        for cell in row:
            if cell == 1:
                color = 'black'
            elif cell == 2:
                color = 'red'
            elif cell == 3:
                color = 'green'
            elif cell == 4:
                color = 'blue'
            else:
                color = 'white'

            env.blokskes.append(cv.create_rectangle(i-env.w/2, j-env.h/2, i-env.w/2 + env.cw, j-env.h/2 + env.ch, fill=color))
            i += env.cw
        j += env.ch


def move_to(p):
    global env

    if (env.doolhof[p[0]][p[1]]==MUUR):
        print("AUW!")
        return
    turtle.goto((p[1]+0.5)*env.cw-env.w/2,env.h/2-(p[0]+0.5)*env.ch)
    env.s=p


def laad_doolhof(path="doolhof3.txt"):
    global env
    
    turtle.ht()
    (env.doolhof,env.s,env.e)=lees_doolhof(path)
    env.start=env.s
    env.cv=turtle.getcanvas()
    env.w=env.cv.winfo_width()
    env.h=env.cv.winfo_height()
    env.dh=len(env.doolhof)
    env.dw=len(env.doolhof[0])
    env.cw=env.w/env.dw
    env.ch=env.h/env.dh
    draw_doolhof(env.cv,env.doolhof)

    turtle.penup()
    turtle.speed(5)
    move_to(env.s)
    turtle.right(turtle.heading())
    turtle.st()

def reset():
    global env

    move_to(env.start)

def move_up():
    global env
    
    move_to((env.s[0]-1,env.s[1]))

def move_down():
    global env
    
    move_to((env.s[0]+1,env.s[1]))

def move_left():
    global env
    
    move_to((env.s[0],env.s[1]-1))


def move_right():
    global env
    move_to((env.s[0],env.s[1]+1))

def turn_right():
    turtle.right(90)

def turn_left():
    turtle.left(90)

def go_forward():
    if turtle.heading()==0:
        move_right()
    elif turtle.heading()==90:
        move_up()
    elif turtle.heading()==180:
        move_left()
    elif turtle.heading()==270:
        move_down()

def ahead():
    if turtle.heading()==0:
        return (0,1)
    elif turtle.heading()==90:
        return (-1,0)
    elif turtle.heading()==180:
        return (0,-1)
    elif turtle.heading()==270:
        return (1,0)

def dirright():
    if turtle.heading()==90:
        return (0,1)
    elif turtle.heading()==180:
        return (-1,0)
    elif turtle.heading()==270:
        return (0,-1)
    elif turtle.heading()==0:
        return (1,0)

def dirleft():
    if turtle.heading()==270:
        return (0,1)
    elif turtle.heading()==0:
        return (-1,0)
    elif turtle.heading()==90:
        return (0,-1)
    elif turtle.heading()==180:
        return (1,0)
    

def free_forward():
    global env
    delta=ahead()
    ns=(env.s[0]+delta[0],env.s[1]+delta[1])

    return (env.doolhof[ns[0]][ns[1]]!=MUUR)

def free_right():
    global env
    delta=dirright()
    ns=(env.s[0]+delta[0],env.s[1]+delta[1])

    return (env.doolhof[ns[0]][ns[1]]!=MUUR)

def free_left():
    global env
    delta=dirleft()
    ns=(env.s[0]+delta[0],env.s[1]+delta[1])

    return (env.doolhof[ns[0]][ns[1]]!=MUUR)

def found_exit():
    global env
    return env.doolhof[env.s[0]][env.s[1]]==DOEL

turtle.shapesize(3, 3, 8)


turnright=turnRight=Turnright=TurnRight=turn_Right=Turn_right=Turn_Right=turn_right
turnleft=turnLeft=Turnleft=TurnLeft=turn_Left=Turn_left=Turn_Left=turn_left
goforward=Goforward=goForward=GoForward=Go_forward=go_Forward=Go_Forward=go_forward
laaddoolhof=Laaddoolhof=laadDoolhof=LaadDoolhof=Laad_doolhof=laad_Doolhof=Laad_Doolhof=laad_doolhof
foundexit=Foundexit=FoundExit=foundExit=Found_exit=Found_Exit=found_Exit=found_exit
freeforward=freeForward=Freeforward=FreeForward=free_Forward=Free_forward=Free_Forward=free_forward
Freeright=freeRight=FreeRight=freeright=Free_right=free_Right=Free_Right=free_right
FreeLeft=freeLeft=Freeleft=freeleft=Free_left=free_Left=Free_Left=free_left
turtle.ht()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        laad_doolhof("doolhof.txt")
    else:
        program = sys.argv[1]
        if program == "1":
            laad_doolhof("doolhof.txt")
        elif program == "2a":
            laad_doolhof("doolhof2a.txt")
        elif program == "2b":
            laad_doolhof("doolhof2b.txt")
        elif program == "3":
            laad_doolhof("doolhof3.txt")
        else:
            laad_doolhof("doolhof.txt")



    


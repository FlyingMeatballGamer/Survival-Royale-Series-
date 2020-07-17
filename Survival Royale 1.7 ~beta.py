import turtle
import time
import math
import os
import random
from tkinter import *
turtle.title("Survival Royale")
turtle.tracer(2)
player = turtle.Turtle()
turtle.bgcolor("black")
choice = random.randint(1,2)

earn1 = 4
earn2 = 2
earn3 = 15
earn4 = 3
earn5 = 9
earn6 = 6
earn7 = 6
op = 1

#Quest Number
QuestNum = 1

#These are to prevent beta mode
AlreadyHitBear = False
AlreadyHitOgre = False
AlreadyHitGoblin = False
AlreadyHitHunter = False
AlreadyHitFireMonster = False
AlreadyHitWitherGhoul = False
AlreadyHitGhost = False

alreadydead = False

AlreadyClicked = False

#If Bullet is already fired
BulletFired = False
BULLETS = 0

#Quests
RandomNumber1 = 5
RandomNumber2 = 10
GlobalRandomNumber = 0
GlobalRandomNumber2 = 0
reward = 30
XPReward = 10
#These numbers will be changed throught out the program

playerheading = 90

bro = 1
seeable = 1
math4 = 1
purcase = 1
used = 1
timer = 500
firemonsterlives = 2
change = 0
on = 0
healing = 1
ghostlives = 1
xp = 0
level = 1
caught = False
coin = 0
speed2 = 2
scoreboard = 0
ogrelives = 1
bearlives = 1
hunterlives = 14
witherghoullives = 1
goblinlives = 2
bulletnum = 0
bulletfunc = True
xpt = turtle.Turtle()
xpt.color("white")
xpt.penup()
xpt.setpos(200, 320)
xpt.pendown()
xpt.hideturtle()
xpt.write(" | XP:", False, align="right", font=("Arial",40, "bold"))
xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
anotherrealm = turtle.Turtle()
anotherrealm.speed(0)
anotherrealm.color("purple")
anotherrealm.shape("square")
anotherrealm.shapesize(1,1,1)
anotherrealm.penup()
anotherrealm.setpos(-500,0)
anotherrealm.pendown()
earth = turtle.Turtle()
earth.speed(0)
earth.color("purple")
earth.shape("square")
earth.shapesize(1,1,1)
earth.penup()
earth.setpos(11111,0)
gem = coin * 2
gem1 = turtle.Turtle()
gem1.hideturtle()
gem1.color("yellow")
gem1.penup()
gem1.setpos(350,-290)
gem1.pendown()
player.shape("circle")
player.color("yellow")
error = turtle.Turtle()
error.speed(0)
error.hideturtle()
error.color("red")
error.penup()
error.setpos(0,20)
error.pendown()
switch = turtle.Turtle()
switch.color("blue")
switch.shape("square")
switch.shapesize(2,2)
switch.penup()
switch.speed(0)
switch.setpos(-350,350)
switch2 = turtle.Turtle()
switch2.color("red")
switch2.shape("square")
switch2.shapesize(2,2)
switch2.speed(0)
switch2.penup()
switch2.setpos(-300,350)
portalinfo = turtle.Turtle()
portalinfo.speed(0)
portalinfo.penup()
portalinfo.setpos(-500,10)
portalinfo.pendown()
portalinfo.color("white")
portalinfo.hideturtle()
portalinfo.write("PORTAL", False, align="center", font=("Comic Sans MS",7, "bold"))
message = turtle.Turtle()
message.color("white")
message.hideturtle()
message.penup()
message.setpos(0,-300)
message.pendown()
healthbooster = turtle.Turtle()
healthbooster.speed(0)
healthbooster.color("pink")
healthbooster.shape("circle")
healthbooster.penup()
healthbooster.setpos(300,0)
version = turtle.Turtle()
version.hideturtle()
version.color("white")
version.speed(0)
version.penup()
version.setpos(400,350)
version.pendown()
version.write("Version 1.7", False, align="center", font=("Arial",7, "bold"))
writer = turtle.Turtle()
writer.speed(0)
writer.hideturtle()
writer.color("white")
writer.penup()
writer.setpos(340,10)
writer.pendown()
Nruse = ("Nurse Level: ")
writer.write(Nruse, False, align="right", font=("Arial",10, "bold"))
writer.write(level, False, align="left", font=("Arial",10, "bold"))
player.penup()
player.speed(0)
coin1 = turtle.Turtle()
coin1.speed(0)
coin1.color("red")
coin1.hideturtle()
coin1.penup()
coin1.setpos(350,-330)
coin1.pendown()

bullet = turtle.Turtle()
bullet.shapesize(1,1,1)
bullet.penup()
bullet.color("blue")
bullet.setpos(12039847,10239847)
bullet.setheading(90)
obstacle = turtle.Turtle()
obstacle.penup()
obstacle.shape("circle")
obstacle.color("green")
obstacle.setpos(0,280)
obstacle2 = turtle.Turtle()
obstacle2.penup()
obstacle2.setpos(-300,0)
obstacle2.shape("circle")
obstacle2.color("brown")
obstacle2.shapesize(2,2)
obstacle3 = turtle.Turtle()
obstacle3.speed(0)
obstacle3.penup()
obstacle3.shape("circle")
obstacle3.color("red")
obstacle3.shapesize(0.9,0.9)
obstacle3.setpos(-300,300)
obstacle4 = turtle.Turtle()
obstacle4.speed(0)
obstacle4.penup()
obstacle4.shape("circle")
obstacle4.color("red")
obstacle4.shapesize(3,3)
obstacle4.setpos(300,-200)
obstacle5 = turtle.Turtle()
obstacle5.speed(0)
obstacle5.penup()
obstacle5.shape("circle")
obstacle5.color("black")
obstacle5.shapesize(1.7,1.7,1.7)
obstacle5.setpos(13204987,10239847)
obstacle6 = turtle.Turtle()
obstacle6.speed(0)
obstacle6.penup()
obstacle6.shape("circle")
obstacle6.color("red")
obstacle6.shapesize(2,2,2)
obstacle6.setpos(10293847,10293847)
obstacle7 = turtle.Turtle()
obstacle7.speed(1)
obstacle7.penup()
obstacle7.color("white")
obstacle7.shape("circle")
obstacle7.setpos(10239847,92384765)
obstacle7.forward(100)
player.setheading(90)
obstacle.setheading(270)
def ChangeValues(Gem,Coin,XP):
    global coin
    global gem
    global xp
    
    gem = gem + Gem
    coin = coin + Coin
    xp = xp + XP
    gem1.undo()
    gem1.write("coins: ", False, align="right", font=("Arial",30, "bold"))
    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
    coin1.undo()
    coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
    coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
    xpt.undo()
    xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
def listen(self, xdummy=None, ydummy=None):
        self._listen()

def onclick2(xdummy,ydummy):
    global lives
    question = input("Enter Confirmation code: ")
    if question == 'chicken':
        lives = lives - lives
        wn.undo()
        wn.write(lives, False, align="left", font=("Arial",40, "bold"))
        dead()
    else:
        print("INCORRECT!")
def onclick3(xdummy,ydummy):
    global coin
    global gem
    global xp
    question = input("Enter Confirmation code: ")
    if question == 'chicken':
        coin = coin + 100000000
        gem = gem + 100000000
        xp = xp + 100000000
        gem1.undo()
        gem1.write("coins: ", False, align="right", font=("Arial",30, "bold"))
        gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
        coin1.undo()
        coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
        coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
        xpt.undo()
        xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
    else:
        print("INCORRECT!")
def REALquest():
    global gem
    global coin
    global xp
    global RandomNumber1
    global RandomNumber2
    global GlobalRandomNumber
    global GlobalRandomNumber2
    global AlreadyClicked
    global QuestNum

    print("Quest:",QuestNum)
    def exit2():
        root.destroy()
        player.setposition(0,0)
        player.setheading(90)
        time.sleep(2)
    def ClaimReward():
        global reward
        global XPReward
        global GlobalRandomNumber
        global GlobalRandomNumber2
        global QuestNum
        QuestNum = QuestNum + 1
        ChangeValues(reward,0,XPReward)
        error.write("You have Recieved your reward!", False, align="center", font=("Arial",20, "bold"))
        time.sleep(2)
        error.undo()
        reward = reward * 2
        XPReward = XPReward * 2
        GlobalRandomNumber = GlobalRandomNumber * 2
        GlobalRandomNumber2 = GlobalRandomNumber * 2
        exit2()
    if AlreadyClicked == False:
        AlreadyClicked = True
        GlobalRandomNumber = random.randint(RandomNumber1,RandomNumber2)
        GlobalRandomNumber2 = random.randint(RandomNumber1,RandomNumber2)
        print(GlobalRandomNumber)
        print(GlobalRandomNumber2)
        #end
    root = Tk()
    root.focus_set()
    root.geometry('500x600')
    root.title("QUESTS")

    #first quest is simple: Just Coins and gems!
    
    l = Label(root, font = ("arial",30,"bold"),text="QUESTS")
    l.pack(side=TOP)

    colo = "white"
    colo2 = "white"
    if gem >= GlobalRandomNumber:
        colo = "green"
    else:
        colo = "white"
    if coin >= GlobalRandomNumber2:
        colo2 = "green"
    else:
        colo2 = "white"
    dabel = Label(root, font = ("arial",20,"bold"),text=("Coins:",gem,"/",GlobalRandomNumber),bg=colo)
    dabel.pack()
        
    dabel2 = Label(root, font = ("arial",20,"bold"),text=("Gems:",coin,"/",GlobalRandomNumber2),bg=colo2)
    dabel2.pack()

    if colo == "green" and colo2 == "green":
        ClaimReward = Button(root, text="Claim Reward",font = ("arial",30,"bold"), command=ClaimReward,bg="white")
        ClaimReward.pack()
    
    rp = Button(root, text="Exit out of Quests",font = ("arial",30,"bold"), command=exit2,bg="white")
    rp.pack(side=BOTTOM)


    
    
def REALshop():
    global healing
    global lives
    global used
    global level
    global purcase
    global bro
    global alreadydead
    
    if lives <= 0:
        if alreadydead == True:
            print("Dead Function is already running")
        else:
            dead()
    else:
        player.setposition(0,100000000)
        global gem
        global coin
        global level
        root = Tk()
        root.focus_set()
        root.geometry('500x600')
        root.title("SHOP")

        l = Label(root, font = ("arial",30,"bold"),text="SHOP")
        l.pack(side=TOP)
        
        dabel = Label(root, font = ("arial",10,"bold"),text="GOLD")
        dabel.pack(side=BOTTOM)
        
        dabel2 = Label(root, font = ("arial",10,"bold"),text=gem,bg="yellow")
        dabel2.pack(side=BOTTOM)        
        

        
        
            
            
        def buttonextrahealth():
            def yes():
                    global gem
                    global lives
                    global coin
                    error.undo()
                    gem = gem - 20
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    lives = lives + 12
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
                    wn.undo()
                    wn.color("blue")
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    for x in range(3):
                        wn.undo()
                        wn.color("white")
                        wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                        time.sleep(1)
                        wn.undo()
                        wn.color("blue")
                        wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                        time.sleep(1)
                    wn.undo()
                    wn.color("white")
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            def no():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            global gem
            global lives
            global coin
            if gem >= 20:
                    root.destroy()
                    poop = Tk()
                    poop.focus_set()
                    poop.geometry('270x120')
                    poop.title("| Confirmation |")
                    b = Button(poop, text="NO",font = "arial",command=no,bg = "red")
                    b.pack()
                    b = Button(poop, text="YES",font = "arial",command=yes,bg = "green")
                    b.pack()
                    pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                    pppp.pack(side=BOTTOM)
                    error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                    error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    pass
                    root.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
        def fhealing():
            global speed2
            global gem
            global level
            def yes2():
                    global speed2
                    global gem
                    global level
                    error.undo()
                    level = level + 1
                    gem = gem - 20
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    speed2 = speed2 - 0.5
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    writer.undo()
                    writer.write(level,False, align="left", font=("Arial",10, "bold"))
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            def no2():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 20:
                    if speed2 == 0.5:
                            error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                            time.sleep(2)
                            error.undo()
                    else:
                            root.destroy()
                            poop = Tk()
                            poop.focus_set()
                            poop.geometry('270x120')
                            poop.title("| Confirmation |")
                            b = Button(poop, text="NO",font = "arial",command=no2,bg = "red")
                            b.pack()
                            b = Button(poop, text="YES",font = "arial",command=yes2,bg = "green")
                            b.pack()
                            pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                            pppp.pack(side=BOTTOM)
                            error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                    error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    pass
                    root.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
        def respawn():
            global bro
            global gem
            def yes22222():
                    global bro
                    global gem
                    global xp
                    error.undo()
                    gem = gem - 200
                    xp = xp - 75
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    xpt.undo()
                    xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    bro = bro - bro
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            def no22222():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 200 and xp >= 75:
                    if bro == 0:
                            error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                            time.sleep(2)
                            error.undo()
                    else:
                            root.destroy()
                            poop = Tk()
                            poop.focus_set()
                            poop.geometry('270x120')
                            poop.title("| Confirmation |")
                            b = Button(poop, text="NO",font = "arial",command=no22222,bg = "red")
                            b.pack()
                            b = Button(poop, text="YES",font = "arial",command=yes22222,bg = "green")
                            b.pack()
                            pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure? ")
                            pppp.pack(side=BOTTOM)
                            error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                    error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    pass
                    root.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
        def double():
            global gem
            global op
            def yes22():
                    global gem
                    global level
                    global earn1
                    global earn2
                    global earn3
                    global earn4
                    global earn5
                    global earn6
                    global earn7
                    error.undo()
                    earn1 = earn1 * 2
                    earn2 = earn2 * 2
                    earn3 = earn3 * 2
                    earn4 = earn4 * 2
                    earn5 = earn5 * 2
                    earn6 = earn6 * 2
                    earn7 = earn7 * 2
                    gem = gem - 30
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            def no22():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 30:
                    if op != 1:
                            error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                            time.sleep(2)
                            error.undo()
                    else:
                            op = op - 1
                            root.destroy()
                            poop = Tk()
                            poop.focus_set()
                            poop.geometry('270x120')
                            poop.title("| Confirmation |")
                            b = Button(poop, text="NO",font = "arial",command=no22,bg = "red")
                            b.pack()
                            b = Button(poop, text="YES",font = "arial",command=yes22,bg = "green")
                            b.pack()
                            pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                            pppp.pack(side=BOTTOM)
                            error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                    error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    pass
                    root.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
        def sword():
            global used
            def yes7():
                    global gem
                    global level
                    global seeable
                    error.undo()
                    player.color("sky blue")
                    seeable = seeable - 1
                    gem = gem - 15
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            def no7():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 15:
                    if used == 0:
                        error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                        time.sleep(2)
                        error.undo()
                        root.destroy()
                        player.setposition(0,0)
                        player.setheading(90)
                    else:
                        used = 0
                        root.destroy()
                        poop = Tk()
                        poop.focus_set()
                        poop.geometry('270x120')
                        poop.title("| Confirmation |")
                        b = Button(poop, text="NO",font = "arial",command=no7,bg = "red")
                        b.pack()
                        b = Button(poop, text="YES",font = "arial",command=yes7,bg = "green")
                        b.pack()
                        pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                        pppp.pack(side=BOTTOM)
                        error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                time.sleep(2)
                error.undo()
                root.destroy()
                player.setposition(0,0)
                player.setheading(90)
            
            
        def toxicrealm():
            global purcase
            def yes4():
                    global xp
                    global speed2
                    global gem
                    global level
                    global purcase
                    purcase = purcase - 1
                    error.undo()
                    gem = gem - 50
                    xp = xp - 100
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    xpt.undo()
                    xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            def no4():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 50 and xp >= 100:
                    if purcase == 0:
                            error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                            time.sleep(2)
                            error.undo()
                    else:
                            root.destroy()
                            poop = Tk()
                            poop.focus_set()
                            poop.geometry('270x120')
                            poop.title("| Confirmation |")
                            b = Button(poop, text="NO",font = "arial",command=no4,bg = "red")
                            b.pack()
                            b = Button(poop, text="YES",font = "arial",command=yes4,bg = "green")
                            b.pack()
                            pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                            pppp.pack(side=BOTTOM)
                            error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                time.sleep(2)
                error.undo()
                root.destroy()
                player.setposition(0,0)
                player.setheading(90)
                
                
            
        def buttontrading():
            global gem
            global lives
            global coin
            if coin > 0 and gem == 0:
                gem = coin * 2
                gem1.undo()
                gem1.write("coins: ", False, align="right", font=("Arial",30, "bold"))
                gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                coin = 0
                coin1.undo()
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                time.sleep(2)
                error.undo()   
                pass
                root.destroy()
                player.setposition(0,0)
                player.setheading(90)
                time.sleep(2)
            elif coin > 0 and gem > 0:
                gem = coin * 2 + gem - 2 + 2
                gem1.undo()
                gem1.write("coins: ", False, align="right", font=("Arial",30, "bold"))
                gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                coin = 0
                coin1.undo()
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                time.sleep(2)
                error.undo()   
                pass
                root.destroy()
                player.setposition(0,0)
                player.setheading(90)
                time.sleep(2)
            else:
                error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                time.sleep(2)
                error.undo()
                pass
                root.destroy()
                player.setposition(0,0)
                player.setheading(90)
        def ihealing():
            global xp
            global speed2
            global gem
            global level
            def yes3():
                    global gem
                    global lives
                    global xp
                    error.undo()
                    gem = gem - 20
                    xp = xp - 20
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    xpt.undo()
                    xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                    beat = 24 - lives
                    lives = lives + beat
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            def no3():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 10 and xp >= 20:
                    if lives == 24:
                            error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                            time.sleep(2)
                            error.undo()
                            root.destroy()
                            player.setposition(0,0)
                            player.setheading(90)
                    else:
                            root.destroy()
                            poop = Tk()
                            poop.focus_set()
                            poop.geometry('270x120')
                            poop.title("| Confirmation |")
                            b = Button(poop, text="NO",font = "arial",command=no3,bg = "red")
                            b.pack()
                            b = Button(poop, text="YES",font = "arial",command=yes3,bg = "green")
                            b.pack()
                            pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                            pppp.pack(side=BOTTOM)
                            error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                    error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    pass
                    root.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
        def tp():
            def yes5():
                    global gem
                    global lives
                    global xp
                    error.undo()
                    gem = gem - 1
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    player.setposition(-500,10)
                    player.setheading(270)
            def no5():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 10 and xp >= 20:
                    if purcase == 1:
                            error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                            time.sleep(2)
                            error.undo()
                            root.destroy()
                            player.setposition(0,0)
                            player.setheading(90)
                    else:
                            root.destroy()
                            poop = Tk()
                            poop.focus_set()
                            poop.geometry('270x120')
                            poop.title("| Confirmation |")
                            b = Button(poop, text="NO",font = "arial",command=no5,bg = "red")
                            b.pack()
                            b = Button(poop, text="YES",font = "arial",command=yes5,bg = "green")
                            b.pack()
                            pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                            pppp.pack(side=BOTTOM)
                            error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                    error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    pass
                    root.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
        def bulletfire():
            def yes5():
                    global gem
                    global lives
                    global xp
                    global BULLETS
                    error.undo()
                    gem = gem - 20
                    gem1.undo()
                    gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    poop.destroy()
                    BULLETS = BULLETS + 3
                    player.setpos(0,0)
                    player.setheading(90)
            def no5():
                    error.undo()
                    poop.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
            if gem >= 20:
                    if 0 == 1:
                            error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                            time.sleep(2)
                            error.undo()
                            root.destroy()
                            player.setposition(0,0)
                            player.setheading(90)
                    else:
                            root.destroy()
                            poop = Tk()
                            poop.focus_set()
                            poop.geometry('270x120')
                            poop.title("| Confirmation |")
                            b = Button(poop, text="NO",font = "arial",command=no5,bg = "red")
                            b.pack()
                            b = Button(poop, text="YES",font = "arial",command=yes5,bg = "green")
                            b.pack()
                            pppp = Label(poop, font = ("arial",20,"bold"),text="Are you sure?")
                            pppp.pack(side=BOTTOM)
                            error.write("Confirm your Transaction. . .", False, align="center", font=("Arial",20, "bold"))
            else:
                    error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                    time.sleep(2)
                    error.undo()
                    pass
                    root.destroy()
                    player.setposition(0,0)
                    player.setheading(90)
        def exitoutofshop():
            root.destroy()
            player.setposition(0,0)
            player.setheading(90)
            time.sleep(2)
            
        b = Button(root, text="Sheild: 20 COINS",font = "arial",command=buttonextrahealth,bg = "lightblue")
        b.pack()

        c = Button(root, text="Trading: AT LEAST 1 GEM",font = "arial", command=buttontrading,bg = "blue")
        c.pack()

        REALTEXT = ""
        text2 = ("Healing: Level",level)
        text3 = ("Healing: MAXED OUT")
        if level == 1:
            REALTEXT = "Faster Healing: Level 2"
        elif level == 2:
            REALTEXT = "Faster Healing: Level 3"
        elif level == 3:
            REALTEXT = "Faster Healing: Level 4"
        else:
            REALTEXT = ("Faster Healing: MAXED OUT")
        tttt = Button(root, text = REALTEXT,font = "arial", command=fhealing,bg = "pink")
        tttt.pack()
        
        d = Button(root, text="Exit out of shop",font = ("arial", 20 ,"bold"), command=exitoutofshop,bg="white")
        d.pack(side=BOTTOM)

        lll = ""
        if lives >= 24:
            lll = "Instant Heal: FULL HEALTH"
        else:
            lll = "Instant Heal: 20 COINS AND 20 XP"
        ddl = Button(root, text=lll,font = "arial", command=ihealing,bg="red")
        ddl.pack()

        bulletoo = Button(root, text="Bullets: 20 COINS",font = "arial", command=bulletfire,bg="orange")
        bulletoo.pack()

        ee11 = ""
        if purcase == 0:
            ee11 = "Toxic Realm: OWNED"
        if purcase == 1:
            ee11 = "Toxic Realm: 50 COINS and 100 XP"
        Realm2 = Button(root, text=ee11,font = "arial", command=toxicrealm,bg="light green")
        Realm2.pack()


        ss = ""
        if earn1 == 8 and earn2 == 4 and earn3 == 30 and earn4 == 6 and earn5 == 18 and earn6 == 12 and earn7 == 12:
            ss = "Double Earnings: OWNED"
        else:
            ss = "Double Earnings: 30 COINS"
        cd = Button(root, text=ss,font = "arial", command=double,bg="yellow")
        cd.pack()
     
        tp = Button(root, text="Teleport to Portal: 10 COINS",font = "arial", command=tp,bg="purple")
        tp.pack()

        oo = ""
        if bro == 0:
            oo = "Respawn: OWNED"
        else:
            oo = "Respawn: 200 COINS AND 75 XP"
        rp = Button(root, text=oo,font = "arial", command=respawn,bg="white")
        rp.pack()

        if change == 1:
            sword2 = Button(root, text="Ghost Sword: 15 COINS",font = "arial", command=sword,bg="sky blue")
            sword2.pack()
        else:
            pass
        
def onclick(xdummy,ydummy):
    global healing
    global lives
    global used
    root = Tk()
    root.focus_set()
    root.geometry('300x300')
    root.title("Options")
    def SHop():
        REALshop()
        root.destroy()
    def QUeST():
        REALquest()
        root.destroy()
    def exit3():
        root.destroy()
        player.setposition(0,0)
        player.setheading(90)
        time.sleep(2)
    if lives <= 0:
        root.destroy()
        if alreadydead == True:
            print("Dead Function is already running")
        else:
            dead()
    if healing == 0:
        root.destroy()
        error.write("You Can't Access the Menu while Healing", False, align="center", font=("Arial",20, "bold"))
        time.sleep(2)
        error.undo()
    elif lives > 0 and healing != 0:
        player.setposition(0,100000000)
        global gem
        global coin
        global xp

        l = Label(root, font = ("arial",10,"bold"),text="OPTIONS")
        l.pack(side=TOP)
        
        #dabel = Label(root, font = ("arial",10,"bold"),text="QUESTS")
        #dabel.pack(side=BOTTOM)

        rp = Button(root, text="SHOP",font = ("arial",10,"bold"), command=SHop,bg="white")
        rp.pack()

        rp2 = Button(root, text="QUESTS",font = ("arial",10,"bold"), command=QUeST,bg="white")
        rp2.pack()

        value1 = "Coins:",gem,"Gems:",coin,"XP:",xp
        howmuch = Label(root, text=value1,font = ("arial",15,"bold"))
        howmuch.pack(side=BOTTOM)

        rp3 = Button(root, text="Cancel",font = ("arial",15,"bold"), command=exit3,bg="white")
        rp3.pack(side=BOTTOM)
    else:
        pass
shop = turtle.Turtle()
shop.speed(0)
shop.color("white")
shop.shapesize(5,5)
shop.penup()
shop.setpos(-250,-180)
shop.forward(100)
shop.pendown()
shop.begin_fill()
shop.left(90)
shop.forward(100)
shop.left(90)
shop.forward(100)
shop.left(90)
shop.forward(100)
shop.left(90)
shop.forward(100)
shop.end_fill()
shop.setpos(-200,-130)
shop.color("black")
shop.write("Menu", False, align="center", font=("Arial",20, "bold"))
shop.penup()
shop.setpos(-200,-150)
shop.color("white")
coinstash = turtle.Turtle()
coinstash.speed(0)
coinstash.color("brown")
coinstash.shapesize(1,3,3)
coinstash.shape("square")
coinstash.penup()
coinstash.setpos(90,200)
xp3 = turtle.Turtle()
xp3.speed(0)
xp3.color("blue")
xp3.shapesize(1,3,3)
xp3.shape("square")
xp3.penup()
xp3.setpos(0, -100)
wn = turtle.Turtle()
wn.speed(0)
wn.color("white")
wn.hideturtle()
wn.penup()
wn.setpos(-30,320)
wn.pendown()
lives = 24
#update in progress
wn.write("Health:", False, align="right", font=("Arial",40, "bold"))
wn.write(lives, False, align="left", font=("Arial",40, "bold"))
speed = 2
coinstash.setpos(90,200)
xp3.setpos(0,-100)
while True:
    gg = player.xcor()
    gg2 = player.ycor()
    shop.onclick(onclick, 1)
    switch.onclick(onclick2, 1)
    switch2.onclick(onclick3, 1)
    e = math.sqrt(math.pow(player.xcor()-healthbooster.xcor(),2)  + math.pow(player.ycor()-healthbooster.ycor(),2))
    c = math.sqrt(math.pow(player.xcor()-shop.xcor(),2)  + math.pow(player.ycor()-shop.ycor(),2))
    d = math.sqrt(math.pow(player.xcor()-obstacle.xcor(),2)  + math.pow(player.ycor()-obstacle.ycor(),2))
    f = math.sqrt(math.pow(player.xcor()-obstacle2.xcor(),2)  + math.pow(player.ycor()-obstacle2.ycor(),2))
    u = math.sqrt(math.pow(player.xcor()-obstacle3.xcor(),2)  + math.pow(player.ycor()-obstacle3.ycor(),2))
    s = math.sqrt(math.pow(player.xcor()-obstacle4.xcor(),2)  + math.pow(player.ycor()-obstacle4.ycor(),2))
    i = math.sqrt(math.pow(player.xcor()-obstacle5.xcor(),2) + math.pow(player.ycor()-obstacle5.ycor(),2))
    k = math.sqrt(math.pow(player.xcor()-obstacle6.xcor(),2) + math.pow(player.ycor()-obstacle6.ycor(),2))
    y = math.sqrt(math.pow(player.xcor()-obstacle7.xcor(),2) + math.pow(player.ycor()-obstacle7.ycor(),2))
    o = math.sqrt(math.pow(player.xcor()-coinstash.xcor(),2)  + math.pow(player.ycor()-coinstash.ycor(),2))
    lll = math.sqrt(math.pow(player.xcor()-anotherrealm.xcor(),2)  + math.pow(player.ycor()-anotherrealm.ycor(),2))
    p = math.sqrt(math.pow(player.xcor()-xp3.xcor(),2)  + math.pow(player.ycor()-xp3.ycor(),2))
    q = math.sqrt(math.pow(player.xcor()-earth.xcor(),2)  + math.pow(player.ycor()-earth.ycor(),2))
    ww = math.sqrt(math.pow(bullet.xcor()-obstacle.xcor(),2)  + math.pow(bullet.ycor()-obstacle.ycor(),2))
    ee = math.sqrt(math.pow(bullet.xcor()-obstacle2.xcor(),2)  + math.pow(bullet.ycor()-obstacle2.ycor(),2))
    rr = math.sqrt(math.pow(bullet.xcor()-obstacle3.xcor(),2)  + math.pow(bullet.ycor()-obstacle3.ycor(),2))
    tt = math.sqrt(math.pow(bullet.xcor()-obstacle4.xcor(),2)  + math.pow(bullet.ycor()-obstacle4.ycor(),2))
    if ee < 40:
            caught = True
            obstacle2.hideturtle()
            obstacle2.setpos(0,1000)    
            coin = 5 + coin
            coin1.undo()
            coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
            coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
            greatjob = turtle.Turtle()
            greatjob.color("white")
            greatjob.hideturtle()
            greatjob.penup()
            greatjob.setpos(0,-250)
            greatjob.pendown()
            greatjob.write("great Job!  You hit a bear", False, align="center", font=("Arial",36, "bold"))
            time.sleep(1)
            greatjob.undo()
            spawn_bear()
        
    elif ww < 15:
            caught = True
            coin = 2 + coin
            obstacle.hideturtle()
            obstacle.setpos(0,1000)        
            coin1.undo()
            coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
            coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
            greatjob = turtle.Turtle()
            greatjob.color("white")
            greatjob.hideturtle()
            greatjob.penup()
            greatjob.setpos(0,-250)
            greatjob.pendown()
            greatjob.write("great Job!  You hit an ogre", False, align="center", font=("Arial",36, "bold"))
            time.sleep(1)
            greatjob.undo()
            spawn_ogre()

    elif rr < 5:
            caught = True
            coin = 3 + coin
            obstacle3.hideturtle()
            obstacle3.setpos(0,1000)        
            coin1.undo()
            coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
            coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
            greatjob = turtle.Turtle()
            greatjob.color("white")
            greatjob.hideturtle()
            greatjob.penup()
            greatjob.setpos(0,-250)
            greatjob.pendown()
            greatjob.write("great Job!  You hit a goblin", False, align="center", font=("Arial",36, "bold"))
            time.sleep(1)
            greatjob.undo()
            spawn_goblin()

    elif tt < 15:
            caught = True
            coin = 3 + coin
            obstacle4.hideturtle()
            obstacle4.setpos(0,1000)        
            coin1.undo()
            coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
            coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
            greatjob = turtle.Turtle()
            greatjob.color("white")
            greatjob.hideturtle()
            greatjob.penup()
            greatjob.setpos(0,-250)
            greatjob.pendown()
            greatjob.write("great Job!  You hit a hunter", False, align="center", font=("Arial",36, "bold"))
            time.sleep(1)
            greatjob.undo()
            spawn_hunter()


    if player.xcor() > 480 or player.xcor() < -880:
        player.right(180)
        
    if player.ycor() > 350 or player.ycor() < -350:
        player.right(180)
        
    if bullet.xcor() > 480 or bullet.xcor() < -880:
        bullet.setpos(10000,10000)
        BulletFired = False
        
    if bullet.ycor() > 350 or bullet.ycor() < -350:
        bullet.setpos(10000,10000)
        BulletFired = False


    #SPACE    
    if d < 15:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            lives = lives - 4
            wn.undo()
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(0.5)
    if o < 30:
        gain = random.randint(3,6)
        gem = gem + gain
        time.sleep(0.5)
        gem1.undo()
        gem1.write("coins: ", False, align="right", font=("Arial",30, "bold"))
        gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
        coinstash.setpos(100000,0)
        pick = random.randint(1,3)
    if y < 15:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            lives = lives - 3
            wn.undo()
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(0.7)
    if q < 20:
        def yesyesyes():
            #toxic realm
            global speed
            global change
            hroot.destroy()
            error.undo()
            turtle.bgcolor("black")
            change = change - 1
            obstacle.setpos(0,280)
            obstacle2.setpos(-300,0)
            obstacle3.setpos(-300,300)
            obstacle4.setpos(300,-200)
            obstacle5.setpos(20398472,2039847)
            obstacle6.setpos(10293847,12039487)
            obstacle7.setpos(18763473,19283743)
            anotherrealm.penup()
            anotherrealm.setpos(-500,0)
            earth.penup()
            earth.setpos(0,111111)
            speed = speed + 2
                
            
            
        def nonono():
            global speed
            hroot.destroy()
            error.undo()
            speed = speed + 2
            player.forward(speed)
        if purcase == 0:
            speed = speed - speed
            player.forward(speed)
            player.setpos(0,0)
            error.write("Confirmation. . .", False, align="center", font=("Arial",40, "bold"))
            hroot = Tk()
            hroot.focus_set()
            hroot.geometry('300x300')
            hroot.title("|Confirm |")

            yy3 = Label(hroot,text="Are You Sure?",font = ("arial",20,"bold"))
            yy3.pack(side=TOP)

            nono2 = Button(hroot, text="NO",font = "arial", command=nonono,bg="red")
            nono2.pack()
            
            yesyes2 = Button(hroot, text="YES",font = "arial", command=yesyesyes,bg="green")
            yesyes2.pack()

        elif purcase == 1:
            error.write("You have not Purchased the Toxic Land Realm", False, align="center", font=("Arial",20, "bold"))
            player.forward(80)
            time.sleep(2)
            error.undo()
    if p < 30:
        gain2 = random.randint(3,6)
        xp = xp + gain2
        time.sleep(0.5)
        xpt.undo()
        xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
        xp3.setpos(100000,0)
        pick2 = random.randint(1,3)
    if lll < 20:
        def yesyes():
            #toxic realm
            global speed
            global change
            hroot.destroy()
            error.undo()
            turtle.bgcolor("green")
            change = change + 1
            obstacle.setpos(0,11111)
            obstacle2.setpos(0,111111)
            obstacle3.setpos(0,1111111)
            obstacle4.setpos(0,11111111)
            obstacle5.setpos(300,300)
            obstacle6.setpos(-100,200)
            obstacle7.setpos(0,-300)
            anotherrealm.penup()
            anotherrealm.setpos(0,1111111111)
            earth.penup()
            earth.setpos(-500,0)
            speed = speed + 2
            player.forward(speed)
            
        def nono():
            global speed
            hroot.destroy()
            error.undo()
            speed = speed + 2
            player.forward(speed)
        if purcase == 0:
            speed = speed - speed
            player.forward(speed)
            player.setpos(0,0)
            error.write("Confirmation. . .", False, align="center", font=("Arial",40, "bold"))
            hroot = Tk()
            hroot.focus_set()
            hroot.geometry('300x300')
            hroot.title("|Confirm |")

            yy3 = Label(hroot,text="Are You Sure?",font = ("arial",20,"bold"))
            yy3.pack(side=TOP)

            nono2 = Button(hroot, text="NO",font = "arial", command=nono,bg="red")
            nono2.pack()
            
            yesyes2 = Button(hroot, text="YES",font = "arial", command=yesyes,bg="green")
            yesyes2.pack()

        elif purcase == 1:
            error.write("You have not Purchased the Toxic Land Realm", False, align="center", font=("Arial",20, "bold"))
            player.forward(80)
            time.sleep(2)
            error.undo()
            
            
        
    if s < 15:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            lives = lives - 12
            wn.undo()
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(2)
    elif i < 30:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            for x in range(i<30):
                xx1 = obstacle5.xcor()
                xx2 = obstacle5.ycor()
                player.setpos(xx1,xx2)
                if i < 30:
                    if lives <= 0:
                        dead()
                    else:
                        player.forward(0.9)
                        lives = lives - 1
                        wn.undo()
                        wn.color("black")
                        wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                        time.sleep(0.1)                      
                elif lives <= 0:
                    dead()
                else:
                    time.sleep(3)
                    wn.undo()
                    wn.color("white")
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            
            if lives == 1 or lives == 3 or lives == 5 or lives == 7 or lives == 9:
                player.forward(0.9)
                lives = lives - 1
                wn.undo()
                wn.color("black")
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                time.sleep(0.1)  
            wn.undo()
            wn.penup()
            wn.setpos(-30,320)
            wn.pendown()
            wn.color("white")
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
    elif k < 10:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            for x in range(k<10):
                speed = speed - speed
                player.forward(speed)
                lives = lives - 3
                wn.undo()
                wn.color("red")
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                time.sleep(0.1)
                lives = lives - 3
                wn.undo()
                wn.color("white")
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                time.sleep(1.3)
            lives = lives - 3
            wn.undo()
            wn.color("red")
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(0.1)
            lives = lives - 3
            wn.undo()
            wn.color("white")
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(1.7)
            speed = speed + 2
            player.forward(speed)
    elif u < 5:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            for x in range(u<5):
                x1 = obstacle3.xcor()
                x2 = obstacle3.ycor()
                player.setpos(x1,x2)
                if u < 5:
                    if lives <= 0:
                        dead()
                    else:
                        player.forward(0.9)
                        lives = lives - 2
                        wn.undo()
                        wn.color("green")
                        wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                        time.sleep(0.5)                      
                elif lives <= 0:
                    dead()
                else:
                    time.sleep(3)
                    wn.undo()
                    wn.color("white")
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            
                    
            wn.undo()
            wn.penup()
            wn.setpos(-30,320)
            wn.pendown()
            wn.color("white")
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                
    elif f < 15:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            lives = lives - 6
            wn.undo()
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(0.5)
            
    elif e < 10:
        if lives >= 24:
            healing = 1
            message.hideturtle()
            message.setpos(0,-300)
            message.write("Your healed up!", False, align="right", font=("Arial",30, "bold"))
            time.sleep(0.1)
            message.undo()
            time.sleep(2)
            player.forward(50)
        elif lives < 24:
            healing = 0
            message.write("Let me heal you up!", False, align="right", font=("Arial",30, "bold"))
            time.sleep(1)
            message.undo()
            if lives < 10:
                while lives != 10 or on == 1:
                    lives = lives + 2
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    time.sleep(speed2)
                while lives != 24 or on == 1:
                    lives = lives + 1
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    time.sleep(speed2)
            else:   
                wn.undo()
                wn.penup()
                wn.setpos(-30,320)
                wn.pendown()
                while lives != 24 or on == 1:
                    lives = lives + 1
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    time.sleep(speed2)
                
    def dead():
        global xp
        global gem
        global coin
        global speed
        global lives
        global alreadydead
        alreadydead = True
        if bro != 1:
                lives = 0
                wn.undo()
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                player.forward(0)
                player.color("red")
                wn.penup()
                wn.setpos(0,100)
                wn.pendown()
                wn.color("red")
                wn.write("You are Dead!", False, align="center", font=("Arial",40, "bold"))
                wn.color("white")
                wn.penup()
                wn.setpos(0,50)
                wn.pendown()
                wn.write("Your Final Score was: ", False, align="center", font=("Arial",40, "bold"))
                wn.penup()
                wn.setpos(0,-10)
                wn.pendown()
                wn.color("blue")
                wn.write(xp, False, align="center", font=("Arial",40, "bold"))
                time.sleep(3)
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.write("Respawning in 5", False, align="center", font=("Arial",40, "bold"))
                time.sleep(1)
                wn.undo()
                wn.write("Respawning in 4", False, align="center", font=("Arial",40, "bold"))
                time.sleep(1)
                wn.undo()
                wn.write("Respawning in 3", False, align="center", font=("Arial",40, "bold"))
                time.sleep(1)
                wn.undo()
                wn.write("Respawning in 2", False, align="center", font=("Arial",40, "bold"))
                time.sleep(1)
                wn.undo()
                wn.write("Respawning in 1", False, align="center", font=("Arial",40, "bold"))
                time.sleep(1)
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()
                wn.undo()


                coin = coin - coin
                gem = gem - gem
                xp = xp - xp
                coin1.undo()
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                gem1.undo()
                gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                wn.penup()
                wn.setpos(-30,320)
                wn.pendown()
                lives = lives + 24
                wn.color("white")
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                player.color("yellow")
                player.setpos(0,0)
                speed = 2
                
        elif bro == 1:
                player.forward(0)
                player.color("red")
                wn.undo()
                lives = 0
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                wn.penup()
                wn.setpos(0,100)
                wn.pendown()
                wn.color("red")
                wn.write("You are Dead!", False, align="center", font=("Arial",40, "bold"))
                wn.color("white")
                wn.penup()
                wn.setpos(0,50)
                wn.pendown()
                wn.write("Your Final Score was: ", False, align="center", font=("Arial",40, "bold"))
                wn.penup()
                wn.setpos(0,-10)
                wn.pendown()
                wn.color("blue")
                wn.write(xp, False, align="center", font=("Arial",40, "bold"))
                time.sleep(3)
                turtle.exitonclick()
        alreadydead = False
    if lives <= 0:
        player.forward(0)
    else:
        player.forward(speed)
        bullet.forward(speed+1)
        time.sleep(0.01)
    
    def up():
        global speed
        global alreadydead
        global BulletFired
        global playerheading
        if lives <= 0:
            if alreadydead == True:
                print("Dead Function is already running")
            else:
                dead()
        else:
            playerheading = 90
            player.setheading(90)

            
        
    def down():
        global speed
        global alreadydead
        global BulletFired
        global playerheading
        if lives <= 0:
            if alreadydead == True:
                print("Dead Function is already running")
            else:
                dead()
        else:
            playerheading = 270
            player.setheading(270)

    def plus():
        global speed
        global alreadydead
        if lives <= 0:
            if alreadydead == True:
                print("Dead Function is already running")
            else:
                dead()
        else:
            speed += 1
    def minus():
        global speed
        global alreadydead
        if lives <= 0:
            if alreadydead == True:
                print("Dead Function is already running")
            else:
                dead()
        else:
            speed -= 1
        
    def hit():
        global alreadydead
        if lives <= 0:
            if alreadydead == True:
                print("Dead Function is already running")
                pass
            else:
                dead()
                pass
        global bearlives
        global ogrelives
        global goblinlives
        global hunterlives
        global witherghoullives
        global firemonsterlives
        global ghostlives
        global seeable
        global xp
        global coin
        global used
        global AlreadyHitBear
        global AlreadyHitOgre
        global AlreadyHitGhost
        global AlreadyHitGoblin
        global AlreadyHitHunter
        global AlreadyHitWitherGhoul
        global AlreadyHitFireMonster
        d = math.sqrt(math.pow(player.xcor()-obstacle.xcor(),2)  + math.pow(player.ycor()-obstacle.ycor(),2))
        if f < 30 and AlreadyHitBear == False:
            if bearlives == 5:
                AlreadyHitBear = True
                bearlives = 1
                coin = earn1 + coin
                obstacle2.hideturtle()
                obstacle2.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                xp = xp + 3
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.hideturtle()
                greatjob.penup()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit an bear", False, align="center", font=("Arial",36, "bold"))
                time.sleep(1)
                greatjob.undo()
                pick = random.randint(1,4)
                pick2 = random.randint(1,4)
                if pick2 == 4:
                    xp3.setpos(0,-100)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_bear()
                AlreadyHitBear = False
            else:
                bearlives = bearlives + 1
        
        elif d < 15 and AlreadyHitOgre == False:
            if ogrelives == 3:
                AlreadyHitOgre = True
                coin = earn2 + coin
                obstacle.hideturtle()
                obstacle.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                xp = xp + 1
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.hideturtle()
                greatjob.penup()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit an ogre", False, align="center", font=("Arial",36, "bold"))
                time.sleep(1)
                greatjob.undo()
                pick = random.randint(1,4)
                pick2 = random.randint(1,4)
                if pick2 == 4:
                    xp3.setpos(0,-100)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_ogre()
                AlreadyHitOgre = False
            else:
                ogrelives = ogrelives + 1
        elif y < 30 and AlreadyHitGhost == False:
            if ghostlives == 5:
                AlreadyHitGhost = True
                used = 1
                ghostlives = 1
                coin = coin + earn3
                obstacle7.hideturtle()
                obstacle7.setpos(0,192309)
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                xp = xp + 4
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.penup()
                greatjob.hideturtle()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit a Ghost", False, align="center", font=("Arial",36, "bold"))
                time.sleep(1)
                greatjob.undo()
                greatjob.hideturtle()
                player.color("yellow")
                seeable = seeable + 1
                pick = random.randint(1,4)
                pick2 = random.randint(1,4)
                if pick2 == 4:
                    xp3.setpos(0,-100)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_ghost()
                AlreadyHitGhost = False
            elif seeable == 1:
                 error.write("You can't hit the ghost!", False, align="center", font=("Arial",30, "bold"))
                 time.sleep(0.5)
                 error.undo()
            else:
                ghostlives = ghostlives + 1
                
        elif u < 5 and AlreadyHitGoblin == False:
            if goblinlives == 3:
                AlreadyHitGoblin = True
                goblinlives = goblinlives - goblinlives + 2
                coin = earn4 + coin
                obstacle3.hideturtle()
                obstacle3.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                xp = xp + 2
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.penup()
                greatjob.hideturtle()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit a goblin", False, align="center", font=("Arial",36, "bold"))
                time.sleep(1)
                greatjob.undo()
                pick = random.randint(1,4)
                pick2 = random.randint(1,4)
                if pick2 == 4:
                    xp3.setpos(0,-100)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_goblin()
                AlreadyHitGoblin = False
            else:
                goblinlives = goblinlives + 1
        elif s < 15 and AlreadyHitHunter == False:
            if hunterlives == 7:
                AlreadyHitHunter = True
                hunterlives = 14
                coin = earn5 + coin
                obstacle4.hideturtle()
                obstacle4.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                xp = xp + 12
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.hideturtle()
                greatjob.penup()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit a hunter", False, align="center", font=("Arial",36, "bold"))
                time.sleep(1)
                greatjob.undo()
                pick = random.randint(1,4)
                pick2 = random.randint(1,4)
                if pick2 == 4:
                    xp3.setpos(0,-100)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_hunter()
                AlreadyHitHunter = False
            else:
                hunterlives = hunterlives - 1
        elif i < 30 and AlreadyHitWitherGhoul == False:
            if witherghoullives == 6:
                AlreadyHitWitherGhoul = True
                witherghoullives = 1
                coin = earn6 + coin
                obstacle5.hideturtle()
                obstacle5.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                xp = xp + 5
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.hideturtle()
                greatjob.penup()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit a Wither Ghoul", False, align="center", font=("Arial",28, "bold"))
                time.sleep(1)
                greatjob.undo()
                pick = random.randint(1,4)
                pick2 = random.randint(1,4)
                if pick2 == 4:
                    xp3.setpos(0,-100)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_witherghoul()
                AlreadyhitWitherGhoul = False
            else:
                witherghoullives = witherghoullives + 1
        elif k < 10 and AlreadyHitFireMonster == False:
            if firemonsterlives == 6:
                AlreadyHitFireMonster = True
                firemonsterlives = 0
                coin = earn7 + coin
                obstacle6.hideturtle()
                obstacle6.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                xp = xp + 5
                xpt.undo()
                xpt.write(xp, False, align="left", font=("Arial",40, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.hideturtle()
                greatjob.penup()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit a Fire Monster", False, align="center", font=("Arial",28, "bold"))
                time.sleep(1)
                greatjob.undo()
                pick = random.randint(1,4)
                pick2 = random.randint(1,4)
                if pick2 == 4:
                    xp3.setpos(0,-100)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_firemonster()
                AlreadyHitFireMonster = False
            else:
                firemonsterlives = firemonsterlives + 1
        else:
            message.write("There's nothing to hit!", False, align="center", font=("Arial",40, "bold"))
            time.sleep(1)
            message.undo()
    def space():
        global BulletFired
        global playerheading
        global BULLETS
        if BULLETS > 0:
            if BulletFired == False:
                BulletFired = True
                BULLETS = BULLETS - 1
                #when the player presses the space key it will teleport the turtle to the player and shoot
                bullet.setpos(player.xcor(),player.ycor())
                bullet.setheading(playerheading)
        else:
            message.setpos(0,-300)
            message.write("You have no ammo", False, align="right", font=("Arial",30, "bold"))
            time.sleep(1)
            message.undo()

        
            
            
    def spawn_ogre():
        global ogrelives
        obstacle.penup()
        obstacle.setpos(random.randrange(200,300),random.randrange(200,300))
        obstacle.showturtle()
        ogrelives = 1
    def spawn_witherghoul():
        obstacle5.penup()
        obstacle5.setpos(random.randrange(200,300),random.randrange(200,300))
        obstacle5.showturtle()
        ogrelives = 1
    def spawn_firemonster():
        obstacle6.penup()
        obstacle6.setpos(random.randrange(-100,-50),random.randrange(100,200))
        obstacle6.showturtle()
    def spawn_goblin():
        global lives 
        for x in range(4):
                lives = lives - 1
                wn.undo()
                wn.color("green")
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                time.sleep(0.5)
        wn.undo()
        wn.color("white")
        wn.write(lives, False, align="left", font=("Arial",40, "bold"))
        if lives <= 0:
                obstacle3.penup()
                obstacle3.setpos(random.randrange(-200,-100),random.randrange(200,300))
                dead()
        else:
                obstacle3.penup()
                obstacle3.setpos(random.randrange(-200,-100),random.randrange(200,300))
        obstacle3.showturtle()
        wn.undo()
        wn.undo()
    def spawn_bear():
        obstacle2.penup()
        obstacle2.setpos(random.randrange(-200,-100),random.randrange(0,200))
        obstacle2.showturtle()
    def spawn_hunter():
        obstacle4.penup()
        obstacle4.setpos(random.randrange(-200,-100),random.randrange(-100,0))
        obstacle4.showturtle()
    def spawn_ghost():
        obstacle7.penup()
        obstacle7.setpos(random.randrange(-200,200),random.randrange(-200, -10))
        obstacle7.showturtle()
        
        
    def right():
        global lives
        global alreadydead
        global BulletFired
        global playerheading
        if lives <= 0:
            if alreadydead == True:
                print("Dead Function is already running")
            else:
                dead()
        else:
            player.setheading(0)
            playerheading = 0
    def left():
        global BulletFired
        global playerheading
        if lives <= 0:
            if alreadydead == True:
                print("Dead Function is already running")
            else:
                dead()
        else:
            playerheading = 180
            player.setheading(180)
        
    
    turtle.onkeypress(right, "Right")
    turtle.onkeypress(left, "Left")
    turtle.onkeypress(up, "Up")
    turtle.onkeypress(down ,"Down")
    turtle.onkeypress(plus, "]")
    turtle.onkeypress(minus, "[")
    turtle.onkeypress(hit, "e")
    turtle.onkeypress(space, "space")
    turtle.listen()

    




    

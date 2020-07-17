import turtle
import winsound
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
level = 1
caught = False
coin = 0
speed2 = 2
scoreboard = 0
ogrelives = 1
bearlives = 1
hunterlives = 5
goblinlives = 2
bulletnum = 0
bulletfunc = True
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
version.setpos(350,350)
version.pendown()
version.write("Version 1.4", False, align="center", font=("Arial",7, "bold"))
writer = turtle.Turtle()
writer.speed(0)
writer.hideturtle()
writer.color("white")
writer.penup()
writer.setpos(300,10)
writer.pendown()
textext = "Nurse Level: ",level
writer.write(textext, False, align="center", font=("Arial",10, "bold"))
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
bullet.setpos(11111111111110,0)
bullet.setheading(90)
obstacle = turtle.Turtle()
obstacle.penup()
obstacle.shape("circle")
obstacle.color("green")
obstacle.setpos(0,280)
obstacle2 = turtle.Turtle()
obstacle2.color("black")
obstacle2.width(50)
obstacle2.setpos(-300,0)
obstacle2.penup()
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
player.setheading(90)
obstacle.setheading(270)
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
    question = input("Enter Confirmation code: ")
    if question == 'chicken':
        coin = coin + 100000000
        gem = gem + 100000000
        gem1.undo()
        gem1.write("coins: ", False, align="right", font=("Arial",30, "bold"))
        gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
        coin1.undo()
        coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
        coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
    else:
        print("INCORRECT!")
def onclick(xdummy,ydummy):
    global lives
    if lives == 0:
        exit()
    player.setposition(0,100000000)
    global gem
    global coin
    global level
    root = Tk()
    root.geometry('350x350')
    root.title("SHOP")

    l = Label(root, font = ("arial",20,"bold"),text="SHOP")
    l.pack(side=TOP)
    
    dabel = Label(root, font = ("arial",10,"bold"),text="GOLD")
    dabel.pack(side=BOTTOM)
    
    dabel2 = Label(root, font = ("arial",10,"bold"),text=gem,bg="yellow")
    dabel2.pack(side=BOTTOM)        
    

    

    def buttonextrahealth():
        global gem
        global lives
        global coin
        if gem >= 20:
                gem = gem - 20
                gem1.undo()
                gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                lives = lives + 24
                wn.undo()
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                time.sleep(2)
                error.undo()
                pass
                root.destroy()
                player.setposition(0,0)
                player.setheading(90)

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
        if gem >= 20:
                if speed2 == 0.5:
                        error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                        time.sleep(2)
                        error.undo()
                else:
                        level = level + 1
                        gem = gem - 20
                        gem1.undo()
                        gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
                        speed2 = speed2 - 0.5
                        error.write("Your Transaction has been made!", False, align="center", font=("Arial",20, "bold"))
                        time.sleep(2)
                        error.undo()
                        writer.undo()
                        writer.write(["Nurse Level: ",level],False, align="center", font=("Arial",10, "bold"))
                pass
                root.destroy()
                player.setposition(0,0)
                player.setheading(90)

        else:
                error.write("An Error Occured while Processing your Transaction!", False, align="center", font=("Arial",20, "bold"))
                time.sleep(2)
                error.undo()
                pass
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
    def exitoutofshop():
        root.destroy()
        player.setposition(0,0)
        player.setheading(90)
        time.sleep(2)
        
    b = Button(root, text="Extra Health - 20 COINS",font = "arial",command=buttonextrahealth,bg = "red")
    b.pack()

    c = Button(root, text="Trading - AT LEAST 1 COIN",font = "arial", command=buttontrading,bg = "blue")
    c.pack()

    tttt = Button(root, text ="Faster Healing - 20 COINS",font = "arial", command=fhealing,bg = "pink")
    tttt.pack()
    
    d = Button(root, text="Exit out of shop",font = ("arial", 20 ,"bold"), command=exitoutofshop,bg="white")
    d.pack(side=BOTTOM)
        
        
shop = turtle.Turtle()
shop.speed(0)
shop.color("dark blue")
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
shop.color("white")
shop.write("shop", False, align="center", font=("Arial",20, "bold"))
shop.penup()
shop.setpos(-200,-150)
shop.color("dark blue")
coinstash = turtle.Turtle()
coinstash.speed(0)
coinstash.color("brown")
coinstash.shapesize(1,3,3)
coinstash.shape("square")
coinstash.penup()
coinstash.setpos(90,200)
wn = turtle.Turtle()
wn.speed(0)
wn.color("white")
wn.hideturtle()
wn.penup()
wn.setpos(0,320)
wn.pendown()
lives = 24
wn.write("Health:", False, align="right", font=("Arial",40, "bold"))
wn.write(lives, False, align="left", font=("Arial",40, "bold"))
speed = 2
coinstash.setpos(90,200)
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
    o = math.sqrt(math.pow(player.xcor()-coinstash.xcor(),2)  + math.pow(player.ycor()-coinstash.ycor(),2))
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
        bullet.right(180)
        
    if bullet.ycor() > 350 or bullet.ycor() < -350:
        bullet.right(180)


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
        gem = gem + 8
        time.sleep(0.5)
        gem1.undo()
        gem1.write("coins: ", False, align="right", font=("Arial",30, "bold"))
        gem1.write(gem, False, align="left", font=("Arial",30, "bold"))
        coinstash.setpos(100000,0)
        pick = random.randint(1,3)
        
    if s < 15:
        if lives <= 0:
            player.forward(0)
            dead()
        else:
            lives = lives - 24
            wn.undo()
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(1)   
    elif u < 5:
        if lives == 0:
            player.forward(0)
            dead()
        else:
            for x in range(u<5):
                x1 = obstacle3.xcor()
                x2 = obstacle3.ycor()
                player.setpos(x1,x2)
                if u < 5:
                    if lives == 0:
                        dead()
                    else:
                        player.forward(0.9)
                        lives = lives - 2
                        wn.undo()
                        wn.color("green")
                        wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                        time.sleep(0.5)                      
                elif lives == 0:
                    dead()
                else:
                    time.sleep(3)
                    wn.undo()
                    wn.color("white")
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            
                    
            wn.undo()
            wn.penup()
            wn.setpos(0,320)
            wn.pendown()
            wn.color("white")
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                
    elif f < 15:
        if lives == 0:
            player.forward(0)
            dead()
        else:
            lives = lives - 6
            wn.undo()
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(0.5)
            
    elif e < 20:
        if lives >= 24:
            message.setpos(0,-300)
            message.write("Your healed up!", False, align="right", font=("Arial",30, "bold"))
            time.sleep(0.1)
            message.undo()
            time.sleep(2)
            player.forward(50)
        elif lives < 20:
            message.write("Let me heal you up!", False, align="right", font=("Arial",30, "bold"))
            time.sleep(1)
            message.undo()
            if lives < 10:
                while lives != 10:
                    lives = lives + 2
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    time.sleep(speed2)
            else:
                health3 = 24 - lives
                wn.undo()
                wn.penup()
                wn.setpos(0,320)
                wn.pendown()
                for x in range(health3):
                    lives = lives + 1
                    wn.undo()
                    wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                    time.sleep(speed2)
    def dead():
        player.forward(0)
        player.color("red")
        wn.penup()
        wn.setpos(0,-100)
        wn.pendown()
        wn.color("red")
        wn.write("You are Dead!", False, align="center", font=("Arial",40, "bold"))
        time.sleep(3)
        turtle.exitonclick()
    if lives <= 0:
        player.forward(0)
    else:
        player.forward(speed)
        bullet.forward(speed)
        time.sleep(0.01)
    
    def up():
        global speed
        if lives == 0:
            print("You are Dead!")
            dead()
        else:
            player.setheading(90)
            
        
    def down():
        global speed
        if lives == 0:
            print("You are Dead!")
            dead()
        else:
            player.setheading(270)
    def plus():
        global speed
        if lives == 0:
            print("You are Dead!")
        else:
            speed += 1
    def minus():
        global speed
        if lives == 0:
            print("You are Dead!")
        else:
            speed -= 1
        
    def hit():
        if lives == 0:
            print("You are dead")
            exit()
        global bearlives
        global ogrelives
        global goblinlives
        global hunterlives
        global coin
        d = math.sqrt(math.pow(player.xcor()-obstacle.xcor(),2)  + math.pow(player.ycor()-obstacle.ycor(),2))
        if f < 30:
            if bearlives == 4:
                bearlives = bearlives - bearlives + 1
                coin = 2 + coin
                obstacle2.hideturtle()
                obstacle2.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
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
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_bear()
            else:
                bearlives = bearlives + 1
        
        elif d < 15:
            if ogrelives == 3:
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
                pick = random.randint(1,4)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_ogre()
            else:
                ogrelives = ogrelives + 1
        elif u < 5:
            if goblinlives == 3:
                goblinlives = goblinlives - goblinlives + 2
                winsound.PlaySound("Desktop/Pain.wav", winsound.SND_ASYNC)
                coin = 3 + coin
                obstacle3.setpos(0,1000)        
                coin1.undo()
                coin1.write("gems: ", False, align="right", font=("Arial",30, "bold"))
                coin1.write(coin, False, align="left", font=("Arial",30, "bold"))
                greatjob = turtle.Turtle()
                greatjob.color("white")
                greatjob.penup()
                greatjob.setpos(0,-250)
                greatjob.pendown()
                greatjob.write("great Job!  You hit a goblin", False, align="center", font=("Arial",36, "bold"))
                time.sleep(1)
                greatjob.undo()
                pick = random.randint(1,4)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_goblin()
            else:
                goblinlives = goblinlives + 1
        elif s < 15:
            if hunterlives == 3:
                hunterlives = 5
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
                pick = random.randint(1,4)
                if pick == 4:
                    coinstash.setpos(90,200)
                spawn_hunter()
            else:
                hunterlives = hunterlives - 1
        else:
            message.write("There's nothing to hit!", False, align="center", font=("Arial",40, "bold"))
            time.sleep(1)
            message.undo()
    def space():
        if bulletfunc == False:
            #bulletnum == bulletnum - 1
            for x in range(18):
                bullet.forward(4)
                player.forward(0.5)
                if ww < 40:  
                    print("hi")
                if ee < 40:  
                    print("hi")
                if rr < 40:  
                    print("hi")
                if tt < 40:  
                    print("hi")
        else:
            print("NOPE!")
            
            
            
    def spawn_ogre():
        global ogrelives
        obstacle.penup()
        obstacle.setpos(random.randrange(200,300),random.randrange(200,300))
        obstacle.showturtle()
        ogrelives = 1
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
        wn.undo()
        obstacle3.penup()
        obstacle3.setpos(random.randrange(-200,-100),random.randrange(200,300))
    def spawn_bear():
        obstacle2.penup()
        obstacle2.setpos(random.randrange(-200,-100),random.randrange(200,300))
        obstacle2.showturtle()
    def spawn_hunter():
        obstacle4.penup()
        obstacle4.setpos(random.randrange(-200,-100),random.randrange(200,209))
        obstacle4.showturtle()
        
        
    def right():
        if lives <= 0:
            print("You are Dead!")
            dead()
        else:
            player.setheading(0)
            bullet.right(30)
    def left():
        if lives <= 0:
            print("You are Dead!")
            dead()
        else:
            player.setheading(180)
            bullet.left(30)
        
    
    turtle.onkeypress(right, "Right")
    turtle.onkeypress(left, "Left")
    turtle.onkeypress(up, "Up")
    turtle.onkeypress(down ,"Down")
    turtle.onkeypress(plus, "]")
    turtle.onkeypress(minus, "[")
    turtle.onkeypress(hit, "e")
    turtle.onkeypress(space, "space")
    turtle.listen()

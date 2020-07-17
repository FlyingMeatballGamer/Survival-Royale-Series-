import turtle
import time
import math
import os
import random
turtle.title("Survival Royale")
player = turtle.Turtle()
choice = random.randint(1,2)
ogrelives = 3
coin = 0
scoreboard = 0
player.shape("circle")
player.color("yellow")
turtle.bgcolor("black")
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
version.write("Version 1.0", False, align="center", font=("Arial",7, "bold"))
writer = turtle.Turtle()
writer.speed(0)
writer.hideturtle()
writer.color("white")
writer.penup()
writer.setpos(300,10)
writer.pendown()
writer.write("Nurse", False, align="center", font=("Arial",10, "bold"))
player.penup()
player.speed(0)
coin1 = turtle.Turtle()
coin1.speed(0)
coin1.color("red")
coin1.hideturtle()
coin1.penup()
coin1.setpos(350,-330)
coin1.pendown()
obstacle = turtle.Turtle()
obstacle.penup()
obstacle.shape("circle")
obstacle.color("green")
obstacle.setpos(0,280)
player.setheading(90)
obstacle.setheading(270)
wn = turtle.Turtle()
wn.speed(0)
wn.color("white")
wn.hideturtle()
wn.penup()
wn.setpos(0,320)
wn.pendown()
lives = 20
wn.write("Health:", False, align="right", font=("Arial",40, "bold"))
wn.write(lives, False, align="left", font=("Arial",40, "bold"))
speed = 2
while True:
    if player.xcor() > 350 or player.xcor() < -350:
        player.right(180)
    if player.ycor() > 350 or player.ycor() < -350:
        player.right(180)
    e = math.sqrt(math.pow(player.xcor()-healthbooster.xcor(),2)  + math.pow(player.ycor()-healthbooster.ycor(),2))
    d = math.sqrt(math.pow(player.xcor()-obstacle.xcor(),2)  + math.pow(player.ycor()-obstacle.ycor(),2))
    ogrelives = 3
    if d < 15:
        if lives == 0:
            player.forward(0)
            dead()
        else:
            coin = 1 + coin
            lives = lives - 5
            wn.undo()
            wn.write(lives, False, align="left", font=("Arial",40, "bold"))
            time.sleep(1)
    elif e < 20:
        if lives == 20:
            message.setpos(0,-300)
            message.write("Your healed up!", False, align="center", font=("Arial",40, "bold"))
            time.sleep(0.1)
            message.undo()
            time.sleep(2)
            player.forward(20)
        else:
            message.write("Let me heal you up!", False, align="center", font=("Arial",40, "bold"))
            time.sleep(1)
            message.undo()
            health3 = 20 - lives
            wn.undo()
            wn.penup()
            wn.setpos(0,320)
            wn.pendown()
            for x in range(health3):
                lives = lives + 1
                wn.undo()
                wn.write(lives, False, align="left", font=("Arial",40, "bold"))
                time.sleep(1)
            
                
            
    def dead():
        player.forward(0)
        player.color("red")
        wn.penup()
        wn.setpos(0,-100)
        wn.pendown()
        wn.color("red")
        wn.write("You are Dead!", False, align="center", font=("Arial",40, "bold"))
    if lives == 0:
        player.forward(0)
    else:
        player.forward(speed)
        time.sleep(0.01)
    
    


    
    def up():
        global speed
        if lives == 0:
            print("You are Dead!")
        else:
            speed += 1
            
        
    def down():
        global speed
        if lives == 0:
            print("You are Dead!")
        else:
            speed -= 1
        
    def hit():
        d = math.sqrt(math.pow(player.xcor()-obstacle.xcor(),2)  + math.pow(player.ycor()-obstacle.ycor(),2))
        if d < 15:
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
                    
        
        else:
            message.write("There's nothing to hit!", False, align="center", font=("Arial",40, "bold"))
            time.sleep(1)
            message.undo()
    def spawn_ogre():
        obstacle.penup()
        obstacle.setpos(random.randint(200,300),random.randint(200,300))
        obstacle.showturtle()
            
    def right():
        if lives == 0:
            print("You are Dead!")
        else:
            player.right(30)
    def left():
        if lives == 0:
            print("You are Dead!")
        else:
            player.left(30)
        
    
    turtle.onkeypress(right, "Right")
    turtle.onkeypress(left, "Left")
    turtle.onkeypress(up, "Up")
    turtle.onkeypress(down ,"Down")
    turtle.onkeypress(hit, "e")
    turtle.listen()

from turtle import *

t = Turtle()
t.screen.setup(800, 800)
t.width(15)
t.speed(4)
t.ht()
t.color("blue")

t.up()
t.goto(-300, -350)
t.down()
t.forward(600)

t.up()
t.goto(-285, -335)
t.down()
t.forward(570)

t.up()
t.goto(-270, -320)
t.down()
t.forward(540)

t.color("orange")

t.up()
t.goto(-255, -305)
t.down()
t.forward(240)
t.up()
t.forward(30)
t.down()
t.forward(240)

t.up()
t.goto(-240, -290)
t.down()
t.forward(225)
t.color("black")
t.forward(30)
t.color("orange")
t.forward(225)

t.up()
t.goto(-225, -275)
t.down()
t.forward(195)
t.up()
t.forward(60)
t.down()
t.forward(195)

t.color("black")

t.up()
t.goto(-205, -260)
t.down()
t.goto(-225, -245)
t.setheading(90)
t.forward(300)
t.setheading(0)
t.forward(15)
t.goto(-225, 55)
t.setheading(90)
t.forward(150)

t.setheading(0)
t.forward(30)
t.setheading(90)
t.forward(30)
t.setheading(0)
t.forward(30)
t.setheading(90)
t.forward(30)
t.setheading(0)
t.forward(300)
t.setheading(270)
t.forward(30)
t.setheading(0)
t.forward(30)
t.setheading(270)
t.forward(30)
t.setheading(0)
t.forward(30)
t.setheading(270)
t.forward(150)
t.setheading(180)
t.forward(15)
t.goto(195, 55)
t.setheading(270)
t.forward(300)
t.goto(180, -260)

t.up()
t.goto(-225, 40)
t.down()
t.setheading(180)
t.forward(30)

t.up()
t.goto(-225, 25)
t.down()
t.setheading(180)
t.forward(60)

t.up()
t.goto(-225, 10)
t.down()
t.setheading(180)
t.forward(90)

t.up()
t.goto(-225, -5)
t.down()
t.setheading(180)
t.forward(120)

t.up()
t.goto(-225, -20)
t.down()
t.setheading(180)
t.forward(150)

t.up()
t.goto(-255, -35)
t.down()
t.setheading(180)
t.forward(75)



t.up()
t.goto(195, 40)
t.down()
t.setheading(0)
t.forward(30)

t.up()
t.goto(195, 25)
t.down()
t.setheading(0)
t.forward(60)

t.up()
t.goto(195, 10)
t.down()
t.setheading(0)
t.forward(90)

t.up()
t.goto(195, -5)
t.down()
t.setheading(0)
t.forward(120)

t.up()
t.goto(195, -20)
t.down()
t.setheading(0)
t.forward(150)

t.up()
t.goto(225, -35)
t.down()
t.setheading(0)
t.forward(75)


t.up()
t.goto(-105, 100)
t.down()
t.setheading(0)
t.forward(15)

t.up()
t.goto(-105, 85)
t.down()
t.setheading(0)
t.forward(15)


t.up()
t.goto(75, 100)
t.down()
t.setheading(0)
t.forward(15)

t.up()
t.goto(75, 85)
t.down()
t.setheading(0)
t.forward(15)

t.color("orange")
t.up()
t.goto(-15, 55)
t.down()
t.setheading(0)
t.forward(30)

t.up()
t.goto(-5, 40)
t.down()
t.setheading(0)
t.forward(15)

t.screen.exitonclick()
t.screen.mainloop()
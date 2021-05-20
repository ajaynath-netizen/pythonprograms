import turtle,math
tool=turtle.Turtle()
angel={i:math.sin(math.radians(i)*100) for i in range(-180,181)}


tool.backward(180)
tool.forward(360)
tool.stamp()
tool.backward(180)
tool.left(90)
tool.forward(100)
tool.stamp()
tool.backward(200)
tool.forward(100)
tool.right(90)
tool.backward(180)


for x,y in angel.items():
    
    tool.goto(x,y)


turtle.done()
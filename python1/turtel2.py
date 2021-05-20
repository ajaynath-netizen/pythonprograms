import turtle
wn=turtle.Screen()
wn.bgcolor('black')

tool=turtle.Turtle()
tool.color('white')

#rotate rectangle graphics

def rotate_rect(angle):
    if angle<=0:
     return

    else:
        for j in range(2):
            tool.speed(10)
            tool.color('red')
            tool.forward(100)
            tool.left(90)
            tool.forward(60)
            tool.left(90)
        tool.left(angle)
        return rotate_rect(angle-1)

angle=360
rotate_rect(angle)

# for i in range(1,10):
#    tool.pendown()
#    tool.forward(240)
#    tool.penup()
#    tool.goto(0,-30*i)
   
tool.speed(10)

#Chess Board
def box(l):
  
   for i in range(4):
      tool.forward(l)
      tool.left(90)
      




x=0
y=-80
z=30
count=0

while True:

   tool.goto(x,y)
   tool.pendown()
   
   
   
   x=x+z
   

   if count%2==0:
      tool.begin_fill()
      tool.fillcolor("white")
      box(z)
      tool.end_fill()
      

   else:
     tool.begin_fill()
     tool.fillcolor("black")
     box(z)
     tool.end_fill()

    

   if x>=z*8:
      x=0
      y+=z
      
      count+=1
      tool.penup()
   

   if y>=160:
       break

   count+=1
   
tool.hideturtle()
turtle.done()


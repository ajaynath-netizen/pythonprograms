import turtle 
tool=turtle.Turtle()

def rectangle(l,b):
    if b<=0:
        return

    else:
      for j in range(2):
        tool.forward(l)
        tool.left(90)
        tool.forward(b)
        tool.left(90)
      return rectangle(l-5,b-5)
rectangle(100,80)
  
    


def draw_circle(radius):
     if radius<=0:
         return

     else:
       
        tool.circle(radius)
        tool.goto(0,radius-5)
        return draw_circle(radius-5)



draw_circle(100)

turtle.done()
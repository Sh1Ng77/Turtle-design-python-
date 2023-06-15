import turtle

t = turtle.Turtle()
t.speed(9)
turtle.bgcolor('black')
t.pensize(1)
def func():
    for i in range(200):
        t.speed(77)
        t.right(1)
        t.forward(1)
t.color('darkblue','darkred')
t.begin_fill()
t.left(140)
t.forward(111.70)
func()
t.left(120)
func()
t.forward(111.60)
t.end_fill()
t.color('white')
style = ('Algerian',(20),'italic')
t.write('.......For you😘💖💖;___#___💖💖.',font=style,align='left')      # write name; [#]you want
t.hideturtle()
turtle.done()   
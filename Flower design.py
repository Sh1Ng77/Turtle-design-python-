from turtle import *

def flur():
    for i in range(300):
        speed(0)
        circle(190 - i, 90)
        left(90)
        circle(190-i, 90)
        left(18)
flur()
mainloop()
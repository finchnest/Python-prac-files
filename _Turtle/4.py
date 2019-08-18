import turtle as t
def reg_polygon(turt,n,l,x,y):
        s=1
        turt.penup()
        turt.goto(x,y)
        turt.pendown()
        while s<=n:
            turt.fd(l)
            turt.lt(360/n)
            s+=1

    

bob=t.Turtle()

reg_polygon(bob,6,100,12,100)

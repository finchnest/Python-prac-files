import turtle as t
def square(turt,x,y,leng):
    c=1
    while c<19:
        turt.penup()
        turt.goto(x,y)
        turt.lt(20)
       
        turt.pendown()
        s=1
        while s<=4:
            turt.fd(leng)
            turt.lt(90)
            s+=1
        c+=1

    

bob=t.Turtle()

square(bob,0,0,100)



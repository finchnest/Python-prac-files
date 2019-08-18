import turtle as t

def randColor():
    import random
    color='#'
    for a in range(0,6):
       r=random.randint(0,14)
       if r>=10:
            color+=chr(ord('a')+(r-10))
       else:
            color+=str(r)
    return color

def radius(turt,rad):
    c=1
    turt.speed(2000)
    while c<19:
        rand_color = randColor()
        turt.begin_fill()
        turt.fillcolor(rand_color)
        turt.lt(20)
        turt.circle(rad)
        turt.end_fill()
        c+=1

bob=t.Turtle()
radius(bob,100)


import math

def areaOfCircle(h,x1,k,y1):
     def distance(h,x1,k,y1):
        dist=math.sqrt((x1-h)**2+(y1-k)**2)
        return dist
     def cirArea(radius):
        area=math.pi*radius**2
        return area
     return cirArea(distance(h,x1,k,y1))

print(areaOfCircle(2,8,4,12)) 

###############################

def distance(h,x1,k,y1):
     dist=math.sqrt((x1-h)**2+(y1-k)**2)
     return dist
def cirArea(radius):
     area=math.pi*radius**2
     return area
     
print(cirArea(distance(2,8,4,12))) 

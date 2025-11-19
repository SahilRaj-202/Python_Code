#write a function to calculate the distance of two points.
import math
def calc_distance(x1,y1,x2,y2):
    print("X1=",x1)
    print("X2=",x2)
    print("Y1=",y1)
    print("Y2=",y2)
    dx=(x2-x1)
    dx=math.pow(dx,2)
    dy=(y2-y1)
    dy=math.pow(dy,2)
    distance=math.pow(dx+dy,0.5)
    return distance

print("Distance =",(format(calc_distance(4,4,2,2) ,".2f")))


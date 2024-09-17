import math

try:
    r=float(input("moi ban nhap ban kinh hinh tron:"))
    cv=2*math.pi*r
    dt=r**2
    print("cv=",cv)
    print("dt=",dt)
except:
    print("loi roi!")

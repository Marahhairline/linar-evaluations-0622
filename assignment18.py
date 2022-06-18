def distance (value):
    print("input the first value")
    xone = int(input())
    print (" input the second value")
    xtwo = int(input())
    x = (xtwo - xone)
    xsqu = x**2
    print(xsqu)
    print ("input the first value for y")
    yone = int(input())
    print("input the second value of y")
    ytwo = int(input())
    y = (ytwo - yone)
    ysqu = y**2
    print (ysqu)
    distance = (xsqu * ysqu)**0.5
    print (distance)
distance ("value")

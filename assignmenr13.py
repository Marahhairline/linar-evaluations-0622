def quadratic(a , b , c):
    print("input first value")
    a = float(input())
    print("input second value")
    b = float(input())
    print("input third value")
    c = float(input())
    determinant = (b**2) - (4*a*c)
    denorminator = 2*a
    mainformular = determinant**0.5
    firstroot = float(-b) + mainformular
    secondroot = float(+b) + mainformular
    finalresult = firstroot/denorminator
    secondfinalresult = secondroot/denorminator
    #print("the firstroot is", str(finalresult))
    #print("the second root is", str(secondfinalresult))
    #print("the first solution", a)
    #rint("the second solution", 
    #print("the third solution", c) 
    return finalresult , secondfinalresult
    #quadratic(1 , -4 , 4)
to_use = quadratic(a, b, c)

print (to_use)

                    

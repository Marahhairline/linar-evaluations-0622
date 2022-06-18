def percentageerror(actual , predicted):
    print(" input the actual value")
    actualvalue = int(input())
    print("input the predicted value")
    predictedvalue = int(input())
    percentageerror = (actualvalue - predictedvalue) / actualvalue 
    normalvalue = percentageerror * 100
    if actualvalue != 0 : 
        print(percentageerror)
    else :
        print(normalvalue)
percentageerror ("actual" , "predicted")           
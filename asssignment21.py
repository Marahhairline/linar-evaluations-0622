#for example 2
for p in range (40 , 100):
    print (p)


#for example 3
food = ["rice" ,"beans" ,"tomato" ,"bread" ,"stew" ,"akara"]
for q in food:
    if q == "stew":
        continue
    print(q)

    #for example 
food = ["rice" ,"beans" ,"tomato" ,"bread" ,"stew" ,"akara"]
for q in food:
    if q == "stew":
        break
    print(q)
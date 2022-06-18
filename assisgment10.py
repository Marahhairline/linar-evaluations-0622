#using if,else,elif the staff of linar are to be graded based on the years of experience from level 1 to level 11
print("WELCOME TO LINAR STAFF EXPERIRNCE")
print("THIS PROGRAM CALCULATES YOUR SALARY AND LEVEL BASED ON YOUR YEARS OF EXPERIENCE")
basicsalary = 20000
experience = int(input())
if  0<=experience<=2 :
    print("YOU ARE IN LEVEL 1")
    print ("YOUR SALARY IS ", + basicsalary)
elif 3<=experience<=5 :
    print("YOU ARE IN LEVEL 2")
    print("YOUR SALARY IS ", + basicsalary*1.25)
elif 6<=experience<=8 :
    print("YOU ARE IN LEVEL 3")
    print("YOUR SALARY IS ", + basicsalary*1.25**2)
elif 9<=experience<=11 :
    print("YOU ARE IN LEVEL 4") 
    print("YOUR SALARY IS ", + basicsalary*1.25**3)
elif 12<=experience<=14 :
    print("YOU ARE IN LEVEL 5")
    print("YOUR SALARY IS ", + basicsalary*1.25**4)
elif 15<=experience<=17 :
    print("YOU ARE IN LEVEL 6")
    print("YOUR SALARY IS ", + basicsalary*1.25**5)
elif 18<=experience<=20 :
    print("YOU ARE IN LEVEL 7")
    print("YOUR SALARY IS ", + basicsalary*1,25**6)
elif 21<=experience<=23 :
    print("YOU ARE IN LEVEL 8")
    print("YOUR SALARY IS ", + basicsalary*1.25**7)
elif 24<=experience<=26 :
    print("YOU ARE IN LEVEL 9")
    print("YOUR SALARY IS ", + basicsalary*1.25**8)
elif 27<=experience<=29 :
    print("YOUR ARE IN LEVEL 10")
    print("YOUR SALARY IS ", + basicsalary*1.25**9)
else :
    30<=experience 
    print("YOU ARE IN LEVEL 11")
    print("YOUR SALARY IS ", + basicsalary*1.25**10)
print("YOU ARE QUALIFIED TO BE A RETIREE")
print("THANKS FOR USING OUR AUTOMATIC GRADING SOFTWARE")


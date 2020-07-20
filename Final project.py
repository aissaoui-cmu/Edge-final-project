import math

print("")
print("WELCOME , to the TRIANGLE SOLVER created by Ahmed Issaoui . ")
print("")
print("This program will help you find the area , perimeter , sides and angles of a triangle . ")
print("")
print("You just have to provide it with some information .")
print("")
print("Stop waisting time using boring trigonometry calcuations and start using the TRIANGLE SOLVER  ")
print("")
print("press ENTER to strat .")
print("")
print("")
print("")

luncher = input()

if luncher == "" :

    A = B = C = a = b = c = "0"


    u1 = 3
    u2 = 3

    A = input("Enter the measure of angle A (type 0 if it is unknown) :")
    if A != "0" :
        u1 = u1 - 1
    print("")
    B = input("Enter the measure of angle B (type 0 if it is unknown) :")
    if B != "0" :
        u1 = u1 - 1
    print("")
    if u1 >= 2 :
      C = input("Enter the measure of angle C (type 0 if it is unknown) :")
      if C != "0" :
        u1 = u1 - 1
    print("")
    if u1 == 3 :
        print("ERROR : you should provide one angle measurement at least")

    else :
        a = input("Enter the length of side a (type 0 if it is unknown) :")
        if a != "0" :
            u2 = u2 - 1
        if u1 + u2 != 3 :
            b = input("Enter the length of side b (type 0 if it is unknown) :")
            if b != "0" :
               u2 = u2 - 1
        print("")
        if u1 + u2 != 3 :
           c = input("Enter the length of side c (type 0 if it is unknown) :")
           if c != "0" :
               u2 = u2 - 1



    if u1 + u2 == 3 :

        c = int(c)
        A = int(A)
        B = int(B)
        C = int(c)
        a = int(a)
        b = int(b)

        if (c != 0 and b != 0 and A != 0 ) :
          print(math.cos(A))
          a = math.sqrt(c*c + b*b - b*c*(math.acos(A)))











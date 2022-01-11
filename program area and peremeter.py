a=int(input("select the options to find area and perimeter \n 1. square \n 2. rectangle=   "))
if(a==1):
   s=int(input("enter the side of square="))
   ar=s*s
   ps=4*s
   print("the area and peremeter is=",ar,ps)
elif(a==2):
    l=int(input("enter the length of rectangle="))
    b=int(input("enter the breath of rectangle="))
    pr=2*l+2*b
    a=l*b
    print("the peremeter and area is=",pr,a)
else:
    print("wrong input")

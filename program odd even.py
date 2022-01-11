a=int(input('enter the lower limit'))
b=int(input('enter the upper limit'))
even=0
odd=0
for i in range(a,b+1):
     if (i%2==0):
         even+=i
     else:
         odd+=i
         print(even,"..                                            ..",odd)
else:
    print('loop terminated')
print(" sum of all even no is ",even)
print("sum of all odd no is",odd)

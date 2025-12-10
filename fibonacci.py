print("*"*10)
 #fibonacci series

number = input("Enter a number")
n = int(number)
a=0
b=1
while n>0 :
   print(a)
   next_term= a+b
   a=b
   b=next_term
   n = n-1

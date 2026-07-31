# wap to input two number and calculate the sum of these number
num1=int(input("Enter the IST  number "))
num2=float(input("Enter the 2nd number  "))
result=num1+num2
# # expilcit type casting 
print(float(result))
# # implicit type casting 
print(result)
# # try esception
try:
    num1=int(input("Enter the IST  number "))
    num2=float(input("Enter the 2nd number  "))
    result=num1+num2
    print(result)
except:
     print("Any error are occured ")
#wap to print the area of the square
try:
    side=float(input("Enter the one side of the square "))
    print("area =",side*side)
except:
    print("can't input the int value ")
# wap to input the two floating number and the calculate thier avarage
IStNum=float(input("Enter the IST number "))
secondNum=float(input("Enter the 2nd number "))
sum=IStNum+secondNum
avarage=sum/2
print("The avarage of the two floating number is =",avarage)
# wap to input two number nad the which is A and B and print true if A is greater then or equal to B.else if not equal
A=int(input("Enter the value for A  "))
B=int(input("Enter the value for B"))
print(A>=B)
if A>=B:
    print("true")
else:
    print("flase")
    # multi line commnet 
    print('''
          pakistan is power
           full country''')




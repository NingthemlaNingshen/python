# #vovels
# ch=input("alphabet=")
# if (ch=='A'or ch=='a') or (ch=='E'or ch=='e') or (ch=='I'or ch=='i') or (ch=='O'or ch=='o') or (ch=='U'or ch=='u'):
#     print("vowels")
# else:
#     print("try")


#even,odd,or zero
# num=int(input("enter the no="))
# if num%2==0:
#     print("even")
# elif num%2!=0:
#     print("odd")
# else:
#     print("zero")


#check vowel,consonent 
# ch=input("alphabet=")
# if (ch=="a" or ch=='A')or( ch=='I'or ch=="i")or(ch=='E'or ch=='e')or(ch=='O'or ch=='o')or(ch=='u'or ch=='U') :
#     print("vowel")
# else:
#     print("consonent")


#numbers of girls and bed
# girls=int(input("no. of girls="))
# bed=int(input("no. of bed="))
# if bed>girls:
#     print("add" ,bed-girls ,"more girls")
# elif bed<girls:
#     print("need",girls-bed," more bed")
# else:
#     print("equal")



#special charecter or alphabet
# ch=input("any=")
# if (ord(ch)>=65 and ord(ch)<=90)or(ord(ch)>=97 and ord(ch)<=122):
#     print(ch, "is an alphabet")
# else:
#     print(ch, "is not alphabet")



#triangle(valid or invalid)(equilateral,isoceles,or scalene)
# num1=int(input("any number="))
# num2=int(input("any number="))
# num3=int(input("any number="))
# if (num1+num2>num3 and num2+num3>num1 and num1+num3>num2):
#     print("triangle is valid")
# else:
#     print("invalid")


# num1=int(input("num="))
# num2=int(input("num="))
# num3=int(input("num="))
# if(num1==num2 and num2==num3 and num3==num1):
#     print("equilateral")
# elif(num1==num2 or num2==num3 or num3==num1):
#     print("isoceles")
# else:
#     print("scalene")


#attendence,percentage
# a=int(input("no. of calss held="))
# b=int(input("no. of class attended="))
# percentage=b/a*100
# if (percentage>=75):
#     print(percentage,"can attend exam")
# else: 
#     print(percentage,"can't attend exam ")

#oldest,youngest
# x=int(input("enter the age="))
# y=int(input("enter the age="))
# z=int(input("enter the age="))
# if(x>y and x>z):
#     print(x,"older")
# else:
#     print("younger")

#find out the youngest to oldest
# age1=int(input("enter the age="))
# age2=int(input("enter the age="))
# age3=int(input("enter the age="))
# if(age1>age2 and age1>age3):
#     print(age1,"older")
# if(age2>age3 and age2>age1):
#     print(age2,"older")
# if(age3>age1 and age3>age2):
#     print(age3,"older")
# if(age1<age2 and age1<age3):

#     print(age1,"younger")
# if(age2<age3 and age2<age1):
#     print(age2,"younger")
# if(age3<age1 and age3<age2):
#     print(age3,"younger")
# else:
#     print("equal age")


#greater between two number

# num1=int(input("enter the first number="))
# num2=int(input("enter thr second number="))
# if(num1>num2):
#     print(num1,"greater")
# if(num2>num1):
#     print(num2,"greater")
# else:
#     print(num1,num2,"lesser")



#upper case or lower case
# ch=input("any")
# if(ord(ch)>=65 and ord(ch)<=90):
#     print(ch,"upper case")
# elif(ord(ch)>=97 and ord(ch)<=122):
#     print(ch,"lower case")
# else:
#     print("not alphabet")



# salary=int(input("enter the amount="))
# year=int(input("enter the year="))
# if year>5:
#     print("add salary",5/100*salary)
# else:
#     print("no bonus",year,"need more year")


# length=int(input("enter the length="))
# breadth=int(input("enter the breadth="))
# if length==breadth:
#     print("square")
# else:
#     print("rectangle")


# num1=int(input("enter the number="))
# num2=int(input("enter the number="))
# if num1>num2:
#     print("greater",num1)
# elif num2>num1:
#     print("greater",num2)
# else:
#     print("smaller")

#leap year
# year=int(input("enter the year="))
# if year%4==0 and year%400==0:
#     print("leap year")
# elif year%100==0:
#     print("century")
# else:
#     print("normal year")

#or
# year=int(input("year="))
# if ((year%400==0)or (year%4==0)) and ((year%100!=0)):
#     print("leap year")
# else:
#     print("not leap year")


#positive or negative
# num1=int(input("enter the number="))
# if num1>0:
#     print("positive")
# else:
#     print("negative")

# purchase_quantity=int(input("enter the purchase_quantity= "))
# if purchase_quantity>1000:
#     print("there will be discount of 10%=",purchase_quantity-(10*100/1000))
# else:
#     print("no discount")
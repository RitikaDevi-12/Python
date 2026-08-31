# problem 1
"""a1 =int(input("Enter number 1 : "))
a2 =int(input("Enter number 2 : "))
a3 =int(input("Enter number 3 : "))
a4 =int(input("Enter number 4 : "))
if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greater number :" ,a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greater number :" ,a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("a3 is greater number :" ,a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("a4 is greater number :" ,a4)       

# problem 2
marks1 = int(input("Enter Marks 1 : "))
marks2 = int(input("Enter marks 2 : "))
marks3 = int(input("Enter marks 3 : "))

total_percentage = (100*(marks1 + marks2 +marks3))/300
if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("pass" ,total_percentage)
else:
    print("fail" ,total_percentage)
"""
# problem 3
'''p1 = " make a lot of money"
p2 = "click this link"
p3 = "Touch the image "
p4 = "comment on this" 
p5 = "share this"
message = input("Enter your comment : ")
if(p1 in message or p2 in message or p3 in message or p4 in message or p5 in message):
    print("This comment  is a spam")
else:
    print("This comment is safe")         
'''
# problem 4
'''username = input("Entetr your name : ")
if(len(username)<10):
    print("your username contains less than 10 character")
else:
    print('your user name contains greater than or equal to 10 character')    '''

# problem 5
'''l =["harry" , "Aman" ,"Sahil" ,"Sourav" ,"vidhi","laksh"]
name = input("Enter your name : ")
if(name in l):
    print("your name is in the list ")
else:
    print("your ame is not in the list")'''

# problem 6
marks = int(input("Enter your marks : "))   
if(marks<=100 and marks>=90 ):
    print("ex grade")
elif(marks<90 and marks>=80):
    print("A grade")
elif(marks<80 and marks>=70):
    print("B grade")
elif(marks<70 and marks>=60):
    print("C grade")
elif(marks<60 and marks>=50):
    print("D grade")    
elif(marks<50):
    print("fail")
# problem 7
post = "hey Ritti .. you are so sweet . ritti your eyes is so preety."
if("ritti".lower() in post.lower()):
    print("this post is talking about ritti")
else:
    print("this post is noot talking about harry")    
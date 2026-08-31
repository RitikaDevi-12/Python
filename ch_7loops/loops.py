# for loop
#*
for i in range(1,5):
    print(i)
#**
for  i in range(1,101):
    print(i) 

 #***  
for i in range(11):
    print(i)

#for loop with list
l = [1,2,3,4,5,6]
for i in l:
    print(i)

#for loop with tuples
t =(2,6,4,0,10)
for i in t:
    print(i)

#for loop  with string 
s ="Ritika"
for i in s:
    print(i)
# step_size    
for i in range(0,110,10):
    print(i)

    # while loop
    #*
    i = 1
    while(i<6):
        print(i) 
        i+=1 
    #**    
    i = 0
    while(i<5):
        print("chidiya")
        i =i+1
#***
l =[ 1,2,"ritti","chidiya","good","bad",33,44,] 
i = 0
while(i<len(l)):
    print(l[i]) 
    i+=1        
#****
l =[1,3,4,2,45,76,8]  
i = 0
while(i<len(l)):
    print(l[i])
    i += 1    


# for loop with Else
l = [1,2,3,4]
for item in l:
    print(item)
else:
    print('done')    
  
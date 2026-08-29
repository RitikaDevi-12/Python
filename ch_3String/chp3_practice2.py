# problem 1
name1 = input("Enter your name  : ")
print(f"Good morning,{name1}")

# problem 2
letter = ''' Dear <|Name|>,
            you are selected!
            <|Date|>'''
print(letter.replace("<|name|>","Ritika").replace("<|Date|>","15 march 2026"))

# find double space
name2 = "My name is ritti i am  good girl "
print(name2.find("  "))
# replace double space to single space
print(name2.replace(("  "),(" ")))
# problem 5
letter = "Dear Ritti,\n\tyou can do it.\nkeep it up...."
print(letter)
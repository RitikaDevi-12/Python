import random
#  problem 1
f = open("chp9_file/poem.txt")
content = f.read()
if("twinkle"in content):
    print("The word twinkel in the content ")
else:
    print("The word is not in the content ")    
f.close()   

# problem 2
def game():
    print("You are playing the game ")
    score = random.randint(1,65)
    # fetch the highscore
    with open("chp9_file/hiscore.txt") as f:
        hiscore = f.read().strip()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            higscore = 0

    print(f"your score:{score}")
    if(score>hiscore):
        with open("chp9_file/hiscore.txt " ,"w") as f :
            f.write(str(score))

    return score

game()      


# Table from 2 to 20
def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/tables_{n}.txt","w") as f :
            f.write(table)



for i in range(10,16):
    generateTable(i)


# problem 4 replace donkey word
word = "Donkey"

with open("chp9_file/File.txt" ,"r") as f:
    content = f.read()

contentNew = content.replace("word","######")

with open("chp9_file/file.txt" , "w") as f:
    content = f.write("contentNew")

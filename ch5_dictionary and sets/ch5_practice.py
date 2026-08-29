#problem 1
words = {
    "dukhi" : "sad",
    "kursi" : "chair",
    "billi" : "cat",
    "chidiya": "sparrow"
}
word = input("Enter the word you want meaning of :")
print(words[word])
# problem 2
s = set()
n = input("Enter the number :")
s.add(int(n))
n = input("Enter the number :")
s.add(int(n))
n = input("Enter the number :")
s.add(int(n))
n = input("Enter the number :")
s.add(int(n))
n = input("Enter the number :")
s.add(int(n))
n = input("Enter the number :")
s.add(int(n))
n = input("Enter the number :")
s.add(int(n))
n = input("Enter the number :")
s.add(int(n))
print(s)
#problem 3
s = set()
s.add(8)
s.add("8")
print(s)
#problem 4
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
# problem 5
s = {}
print(type(s))
# problem 6
d = {}
name = input("Enter friend name :")
lang= input("Enter language name : ")
d.update({name:lang})

name = input("Enter friend name :")
lang= input("Enter language name : ")
d.update({name:lang})

name = input("Enter friend name :")
lang= input("Enter language name : ")
d.update({name:lang})

name = input("Enter friend name :")
lang= input("Enter language name : ")
d.update({name:lang})

print(d)


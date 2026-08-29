marks = {
       "Harry" : 85,
       "Aman"  : 100,
       "Sahil" : 100,
     "Krishna" : 56

}
#print(marks,type(marks))
print(marks["Harry"])
print(marks["Aman"])
print(marks.items())
print(marks.keys())
print(marks.values())
#pop
m = marks.pop("Harry")
print(m)
print(marks)

# updation
marks.update({"Harry" : 91 ,"Reena" :85})
print(marks)
#get
print(marks.get("harry"))
#copy
print(dict.copy(marks))
#clear
print(dict.clear(marks))

#clear
print(dict.clear(marks))


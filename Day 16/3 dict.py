#Accessing elements from dictionaries

student = {"Name": "Aashritha", "Age" : 19}

#Using key name. If key doesn't exist we get error
print(student["Name"])
print(student["Age"])

#Using get()
print(student.get("Name"))
print(student.get("Marks")) #We get None as o/p no error
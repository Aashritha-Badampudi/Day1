#Methods in dictionary
student = {"Name": "Aashritha", "Age" : 19, "Collage" : "SMEC"}

#keys() method
print(student.keys()) 

#values() method
print(student.values()) 

#items() method
print(student.items())

#copy() method
a=student.copy()
a["Name"] = "Honey"
print(a)
print(student)
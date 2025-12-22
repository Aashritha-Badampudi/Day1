#Nested dictionary
student = {"Name": "Aashritha", 
           "Age" : 19, 
           "Collage" : "SMEC",
           "Marks" : {
               "English" : 90,
               "Maths" : 80,
               "Science" : 70
           }
           }
print("Name : ",student["Name"],"\n" ,
       "Age :",student["Age"],"\n", 
       "Collage: ", student["Collage"],"\n", 
       "Marks :", student["Marks"])
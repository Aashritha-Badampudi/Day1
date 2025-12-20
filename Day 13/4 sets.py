#Removing elements in sets
s={1,2,3,4}
s.remove(2)
# s.remove(5) #remove() method gives error if the element is not there 
print(s)

s.discard(3)
s.discard(5) #Removes safely
print(s)

s.pop()
print(s)
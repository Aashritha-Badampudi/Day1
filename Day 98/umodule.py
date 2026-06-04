import mymodule

mymodule.greeting("Aashritha")

a=mymodule.person1["age"]
print(a)

import mymodule as mx
a=mx.person1["age"]
print(a)

from mymodule import person1
print(person1["country"])
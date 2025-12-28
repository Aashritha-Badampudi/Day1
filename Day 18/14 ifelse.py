num=int(input("Enter the number:\n"))
if num>0:
    if num%2==0:
        print("Positive even")
    else:
        print("Positive odd")
elif num<0:
    if num%2==0:
        print("Negative even")
    else:
        print("Negative odd")
if num==0:
    print("Neutral")
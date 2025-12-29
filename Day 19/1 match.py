signal=input("Enter signal color: ")

match signal:
    case "red":
        print("Stop!")
    case "yellow":
        print("Get ready!")
    case "green":
        print("Go!")
    case _ :
        print("Invalid colour")
T = int(input("Enter signal Seconds: "))

position = T % 90

if position == 0:
    position = 90

if 1 <= position <=30:
    print("RED")
    print("POSITION: ", position)

elif 31 <=position<=45:
    print("YELLOW")
    print("POSITION: ", position)


else:
    print("GREEN")
    print("POSITION: ", position)

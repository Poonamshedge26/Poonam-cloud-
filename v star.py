 Upper part
for i in range(1, 6):
    for space in range(5 - i):
        print(" ", end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()

 Lower part
for i in range(4, 0, -1):
    for space in range(5 - i):
        print(" ", end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()

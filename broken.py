import math
while True:
    binarylist = []
    x = int(input("number to binary (Integers Only): "))
    while x != 0 or 1:
        y = x % 2
        x = math.ceil(x / 2)
        binarylist.append(y)
    
    for i in range(len(binarylist)):
        print(binarylist[len(binarylist) - i])
    
    print(binarylist)

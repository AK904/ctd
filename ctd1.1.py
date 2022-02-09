n = "start"
while n == "start":
    m = 0
    x = input("Enter mode1 or mode2: ")
    while x != "mode1" and x != "mode2":
        x = input("Please Enter only mode1 or mode2: ")
    while m == 0:
        temp = input("Enter the temp: ")
        try:
            temp = float(temp)
            m = 1
        except ValueError:
            print("Please Enter a number: ")
    if x == "mode1":
        temp += 49.6
        print(temp)
    else:
        temp -= 49.6
        print(temp)
    n = input("Enter start or stop: ")
    while n != "start" and n != "stop":
        n = input("Please Enter only start or stop: ")


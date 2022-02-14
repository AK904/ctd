bag = [9,10,49,58,570,555,1]

condition = "start"

while condition == "start":
    number = 0
    print(bag)
    flag = 0
    length = len(bag)
    stringg = input("Please type remove or enter: " )
    while (stringg != "remove" and stringg != "enter"):

        stringg = input("Please type remove or enter: ")
    
    if(stringg != "remove" or length > 5):
        number = input("Please enter a number: ")
        flag = 1
    
        while (not number.isdigit()):
            number = input("Please enter a number: ")
    if(stringg == "remove" and length <= 5):
        print("cannot remove bag is at minumum capacity")
    
    if stringg == "remove" and length > 5 and int(number) in bag :
        bag.remove(int(number))
    elif stringg == "remove" and int(number) not in bag and flag == 1:
        print(" the item is not in the list")

    elif (stringg == "enter"):
        bag.append(int(number))
    print(bag)
    condition = input("if you want to quit type stop if you want to continue type start: ")
    while (condition != "start" and condition != "stop"):
        condition = input("Please enter start or stop: ")








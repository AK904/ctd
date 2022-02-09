n = "start"
l = []
while n == "start":
    x = input("Please Enter a number or letter q: ")
    while not(x.isdigit() or x == 'q'):
        x = input("Enter only a number or letter q: ")

    if x == 'q':
        n = "stop"
    l.append(x)
l.remove('q')
print(l)
print(max(l))
print(min(l))

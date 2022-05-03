import random
import cv2
l1 = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
l2 = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
l3 = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
check = 0

while len(l1) != 0 or len(l2) != 0 or len(l3) != 0:
    print(l1)
    print(l2)
    print(l3)

    while len(l1) != 0 or len(l2) != 0 or len(l3) != 0:

        while True:
            try:
                n1 = int(input("pls enter from 1 to 3:"))
                n2 = int(input("pls enter from 1 to 5:"))
                break
            except Exception:
                print("Enter it correctly")

        if(n2<=5):
            if (n1 == 1 and len(l1) >= n2 and n2 != 0):
                for i in range(n2):
                    l1.pop()
                check += 1
                break
            if (n1 == 2 and len(l2) >= n2 and n2 != 0):
                for i in range(n2):
                    l2.pop()
                check += 1
                break
            if (n1 == 3 and len(l3) >= n2 and n2 != 0):
                for i in range(n2):
                    l3.pop()
                check += 1
                break

    while len(l1) > 0 or len(l2) > 0 or len(l3) > 0:
        x = random.choice(range(1, 4))

        if x == 1 and len(l1) > 0:
            if len(l1) <= 5 and len(l1) > 1:
                y = random.choice(range(1, len(l1)))
            elif len(l1) > 5:
                y = random.choice(range(1, 6))
            else:
                y=1
            for i in range(y):
                l1.pop()
            check += 1
            print(x)
            print(y)
            break
        if x == 2 and len(l2) > 0:
            if len(l2) <= 5 and len(l2) > 1:
                y = random.choice(range(1, len(l2)))
            elif len(l2) >5:
                y = random.choice(range(1, 6))
            else:
                y = 1
            for i in range(y):
                l2.pop()
            check += 1
            print(x)
            print(y)
            break
        if x == 3 and len(l3) > 0:
            if len(l3) <= 5 and len(l3) > 1:
                y = random.choice(range(1, len(l3)))
            elif len(l3) > 5:
                y = random.choice(range(1, 6))
            else:
                y=1
            for i in range(y):
                l3.pop()
            check += 1
            print(x)
            print(y)
            break

if check % 2 != 0:
    img = cv2.imread('winner-winner-chicken-dinner.jpg',1)
    cv2.imshow('image',img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
else:
    img = cv2.imread('loser.jpg', 1)
    cv2.imshow('image', img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()







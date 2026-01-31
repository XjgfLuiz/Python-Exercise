import sys

c = 50

while True :
    if c <= 0:
        print(f"amount owed: {abs(c)}")
        sys.exit()
    else:
        print(f"amount due: {c}")
        n = int(input("insert coin: "))
        if n in [5,10,25]:
            c -= n
        else:
            pass


"""
price = 50

while price > 0 :
    print(f"amount due: {price}")
    n = int(input("insert coin: "))
    if n in [5,10,25]:
        price -= n

print(f"amount owed: {abs(price)}")
"""
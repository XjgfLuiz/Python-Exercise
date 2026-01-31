text = input("something: ")

a =[]

for i in text:
    if i.isupper():
        i = "_" + i.lower()
        a += i
    else:
        a += i

result = "".join(a)

print(f"{result}")
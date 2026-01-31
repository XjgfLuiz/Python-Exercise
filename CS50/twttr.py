wovels = ["a","e","i","o","u"]

phrase = input("Tell me something: ")

newphrase = []

for i in phrase:
    if not i.lower() in wovels:
        newphrase.append(i)


print("".join(newphrase))
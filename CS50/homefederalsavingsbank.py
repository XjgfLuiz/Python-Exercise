import re

greet = input("Greeting: ")

if re.search(r"hello", greet, re.IGNORECASE):
    print("$0")
elif re.search(r"hi|hey|how", greet, re.IGNORECASE):
    print("$20")
elif re.search(r"what|dude|up", greet, re.IGNORECASE):
    print("$100")
else:
    print("$100")

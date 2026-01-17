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


"""greet = input("Greeting: ").strip().lower()

if greet.startswith("hello"):
    print("$0")
elif greet.startswith(("hi", "hey")):
    print("$20")
else:
    print("$100")
    """

"""greet = input("Greeting: ").strip().lower()

if "hello" in greet:
    print("$0")
elif "hi" or "hey" in greet:
    print("$20")
elif "what's" or "dude" in greet:
    print("$100")
else:
    print("$100")
"""
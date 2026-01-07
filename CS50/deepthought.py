#problem set 1 deep
import re

text = input("whats is the porpose of life? ").strip()

if re.search(r"^(forty+(.|-)+six)|(42)$",text, flags=re.IGNORECASE):
    print("Yes")
else:
    print("No")


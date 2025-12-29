import re

email = input("Enter your email: ")

pattern = r"[A-Za-z]+[\w.-]+@[A-Za-z]+\.[A-Za-z]{2,}$"

if re.search(pattern, email):
    print("Valid email")
else:
    print("Invalid email")




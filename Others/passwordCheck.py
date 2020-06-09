import re
pattern = re.compile(r"(^[a-zA-Z0-9@#$%]{8,}[0-9]$)+")
string = "Passwor@4"

a = pattern.search(string)

if (a):
  print("password successful")
  print(pattern.fullmatch(string))

else:
  print("Try a new password")
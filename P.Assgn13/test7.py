#6

import re

passwords = input("password: ")
passwords = passwords.split(",")

accepted_pw = []
for i in passwords:
    
    if len(i) < 6 or len(i) > 12:
        continue

    elif re.search("([a-z])+", i):
        continue

    elif re.search("([A-Z])+", i):
        continue

    elif re.search("([0-9])+", i):
        continue

    elif re.search("([!@$%^&])+", i):
        continue

    else:
        accepted_pw.append(i)

print((" ").join(accepted_pw))

import re

with open("akan.txt", "r") as f:
    s = f.read()
    print(s)

test = re.sub(r'[0-9\.\s]*(.*)', r'\1\n', s, flags=re.M)

#test2 = ','.join(test)

test2 = ','.join(test.split())
test3 = '"",'.join(test)

print(test3)

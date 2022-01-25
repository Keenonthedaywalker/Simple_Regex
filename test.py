import re

with open("northGermanic.txt", "r", encoding="utf8") as f:
    s = f.read()
    print(s)

test = re.sub(r'[0-9\.\s]*(.*)', r'\1\n', s, flags=re.M)

#test2 = ','.join(test)

test2 = ','.join(test.split())
test3 = '",'.join(test.split())

print(test3)

print(re.sub(r'([A-Z][a-z]+)', r'"\1"', test2))

# Removes all occurences of word from file
test4 = test3.replace("dynn_", "")
test5 = test4.replace("dynnp_af", "")
test6 = test5.replace("dynnp_of", "")
test7 = test6.replace('"""', "")
test8 = test7.replace("dynnp_av", "")

print(test4)
print(test5)
print(test6)
print(test7)

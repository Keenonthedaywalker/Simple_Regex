import re

# Make sure to add a space and a symbol in the dynasty part of the text file so
# that commas and quotes are generared correctly.
with open("baltic.txt", "r", encoding="utf8") as f:
    s = f.read()
    print(s)

test = re.sub(r'[0-9\.\s]*(.*)', r'\1\n', s, flags=re.M)

#test2 = ','.join(test)

test2 = ','.join(test.split())
test3 = '",'.join(test.split())
output_text = test.split(" ")

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
print(test8)


with open("text.txt", "w", encoding="utf8") as outfile:
    
    for word in output_text:
        t = (' "'+ word + '", ')
        test9 = t.replace("dynn_", "")
        test10 = test9.replace('dynnp_gada"', "")
        test11 = test10.replace('{",', "")
        test12 = test11.replace('""",', "")
        test13 = test12.replace('"}",', "")
        test14 = test13.replace('"#', "")
        test15 = test14.replace('""dynnp_is"",', "")
        outfile.write(test15)
        #print(test9)
        #print((' "'+ word + '", '))

with open("akan.txt", "r") as f:

    s = f.readlines()
    #print(s[2])

    #example of above, for line 22:
    #print(s[21])

    #or for a subset of lines, from lines 10 to 16
    #print(s[9:15])

    #this would allow you to do:
    for line in range(84,89): #the 16 is not a typo
        s[line] = s[line].replace(" ", "")
        s[line] = s[line].replace("\n", ",")
        print(s[line])

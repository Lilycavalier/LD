with open('database.txt', 'r', encoding="utf-8") as f:
    mylist = []
    # add each line as an item (string) in list
    for line in f:
        line = line.rstrip("\n")
        mylist.append(line)
    # item1 = lst[0].split(';')
    # print(item1)
    # search
    entry = "pirate"
    string = "\n".join(s for s in mylist if entry.lower() in s.lower())
    newstring = string.split(';')
    for i in range(len(newstring)):
        print(newstring[i])  # indented??
    if any(entry in sub for sub in mylist) is False:
        print("Couldn't find this item")
        check = input("Do you want to add it to the database?")
    # add
    if check == "yes":

    # delete
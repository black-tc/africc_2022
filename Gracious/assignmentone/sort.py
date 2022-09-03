names=[]
name_total=3
print("enter 3 names")
while len(names)< name_total:
    names.append(raw_input("name {0}".format(len(names)+1)))
    
    print sorted(names)
# open file on read mode
myfile = open('file handling/myFirstFile.txt','r')
# print(bool(myfile))
# print(myfile)
# exit()

# know time to read the file using for loop
for r in myfile:
    print(r)

    if 'Anjali padhlo abhi bhi time hai' in r:
        # print(r)
        break
    

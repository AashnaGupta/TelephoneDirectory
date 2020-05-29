import os

def add(filename,key,value):
    f= open(filename, 'a')
    f.write(key + '\t' + str(value) + '\n')
    print()
    print (key + "\t" + str(value) + " added succesfully.")
    f.close()
            

def find(filename, key):
    f = open(filename, 'r')
    found = False
    for row in f:
            (k,v) = row.split('\t', 1)
            if k == key:
                found = True
                break

    if found == True:
        print()
        print (key + " found succesfully. The value is: " + v)
    else:
        print()
        print (key + " not found.")



def delete(filename, key):
    f = open(filename, 'r')
    found = False
    new = open('new.txt', 'w')
    for (row) in f:
        (k, v) = row.split('\t', 1)
        if k == key:
            found = True
        else:
            new.write(row)
 
    if found == True:
        print()
        print (key + " deleted succesfully.")
    else:
        print()
        print (key + " not found.")

    f.close()
    new.close()
    os.replace('new.txt', filename)



    
def update(filename, key):
    f = open(filename, 'r')
    found = False
    new = open('new.txt', 'w')
    for (row) in f:
        (k, v) = row.split('\t', 1)
        if k == key:
            found = True
            value = input("Enter the new phone number(only digits 0-9): ")
            value = int(value)
            print()
            new.write(key + '\t' + str(value) + '\n')
            print ("Old value of key " + key + " replaced succesfully with: " + str(value))
            
        else:
            new.write(row)

    if found== False:
        print()
        print ("Name not found.")
                      
    f.close()
    new.close()
    os.replace('new.txt', filename)


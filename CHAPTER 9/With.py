f = open("file.txt")
print(f.read())
f.close()

# THE SAME CAN BE WRITTEN USING WITH STATEMENT LIKE THIS
with open("file.txt") as f:
    print(f.read())
    
    
#YOU DONT HAVE TO EXPLICITLY CLOSE THE FILE

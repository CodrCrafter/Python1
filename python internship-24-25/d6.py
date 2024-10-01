# 1prg to read the file


#file = open("example.txt","r")
#content = file.read()
#print(content)
#file.close()
#-------------------------------------------------------------------------

#2 prg to write the file

#file = open("example.txt", "w")
#file.write("hey! hi")
#file.close()

#-------------------------------------------------------------------------------
#3 prg for appending

#file = open("example.txt","a")
#file.write ("\n we are appending in example.txt file")
#file.close()

#------------------------------------------------------------------------
#4 prg 

file = open("/workspaces/Python1/python internship-24-25/data.txt","r")
total = 0
for line in file:
    total += int(line.strip())
file.close()
print("the sum of number is:",total)
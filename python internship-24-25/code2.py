# 1 prg control structures
#--------------------------------------------------
#if light_is_green:
    #print("Go Straight")
#else:
 #   print("Stop")
#----------------------------------------------------------

#2 prg

#age =18
#if age >= 18:
 #   print("U R eligible to vote")
#else:
 #   print("u r not eligible to vote")
#-----------------------------------------------------------------------

#3 prg

#fruits = ["apple","banana","Guava"]

#for fruit in fruits:
 #   print("fruit")
#-------------------------------------------------------------------------

#4 prg

#count = 1
#while count <= 100:
 #   print(count)
  #  count +=1
#------------------------------------------------------------------------------

#5 prg
#for num in range(1,100):
 #   if num %  2==0:
  #      print(f"{num} is even")
   # else:
    #    print(f"{num} is odd")
#----------------------------------------------------------------

#6 prg
number = int(input("enter the number"))
if number <0:
    print(f"{number} is negetive")
elif number:
    print(f"{number} is positive")
else:
    print(f"{number}is zeo")

if number > 0:
    for i in range(1,number+1):
        print(i)
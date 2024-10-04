#1 prg calculate the cosine of 0

#import math
#cos_value = math.cos(0)
#print(cos_value)
#------------------------------------------------

#2 prg calculate date and time

#import datetime
#current_time = datetime.datetime.now()
#print(current_time)
#----------------------------------------------------

#3 prg get a current working directory

#import os
#current_directory = os.getcwd()
#print(current_directory)
#------------------------------------------------------

#4 prg 

#import sys
#arguments = sys.argv
#print(arguments)
#-----------------------------------------------------------------------

#5 prg 1.write simple prg that calculates the squre root of a number. 2. prints the current date and time. 3. and disply the current working directory.

import math
import datetime
import os
value = int(input("enter the number"))
value_number = math.sqrt(value)
print(value_number)
current_datetime = datetime.datetime.now()
print(f"curre date and time is : {current_datetime}")
current_directory = os.getcwd()
print(f"current working directory: {current_directory}")

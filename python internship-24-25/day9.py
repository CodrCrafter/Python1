#1 writing prg that only accepts numbers. u can raise an axception if the users enters a negative numbers

#def check_positive(number):
 #   if number < 0:
  #      raise ValueError("Negative numbers are not allowed")
#try:
 #   print(check_positive(5))
#except ValueError as e:
#    print(e)

#2 prg using finally-clause

#try:
 #   file = open("/workspaces/Python1/python internship-24-25/example.txt","r")
#except FileNotFoundError:
 #   print("File not found")
#finally:
 #   file.close()
 #  print("File closed")
#---------------------------------------------------------------------------------------

#3 prg

try:
    num1 = float(input("Enter the 1st number"))
    num2 = float(input("Enter the 2nd number"))
    result = num1/num2
    print(f"the result is :{result}")
except ZeroDivisionError:
    print("error: u can not divide by zero")
except ValueError:
    print("Error: please enter valid number")
finally:
    print("program excution is complited")

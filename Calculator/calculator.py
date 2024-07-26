print("******************Calculator Project***********************")
print('-----------------------------------------------------------')

# Addition

def add(n1,n2):

  return n1 + n2

# Substraction

def sub(n1,n2):

  return n1 - n2

# Multiplication

def multi(n1,n2):

  return n1 * n2

# Division

def div(n1,n2):

  return n1 / n2

print("select Operations")

print(" 1. Addition \n"
       " 2. Substraction \n"
       "3.Multiplication \n"
       "4.Division\n")

      #  ----------giving options to user to choose-----------

operation=int(input("Enter the First choice of operation 1/2/3/4:"))


# taking inputs from the user

n1=int(input("Enter the First Number:"))
n2=int(input("Enter the Second Number:"))


# conditional statements

if operation == 1:

  print( n1 , '+' , n2 , '=' , add(n1,n2))

elif operation == 2:

  print( n1 , '-' , n2 , '=' , sub(n1,n2) )

elif operation == 3:

  print( n1 , '*' , n2 , '=' , multi(n1,n2) )

elif operation == 4:

  print( n1 , '/' , n2 , '=' , div(n1,n2) )

else:

  print("invalid input")
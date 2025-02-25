def hi(fname):  
    print('Hi this is ' + fname)  
  
hi("Armin")  
hi("Sara")  
hi("Matin")

# -----------------------------------
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):  
    print(fname + " " + lname)  
  
my_function("Zahra", "Khorshidi")

# -----------------------------------
# If the number of arguments is unknown, add a `*` before the parameter name:
def my_function(*kids):  
    print("The youngest child is " + kids[2])  
  
my_function("Hamid", "Majid", "Nader")

# -----------------------------------
def my_function(child3, child2, child1):  
    print("The youngest child is " + child3)  
  
my_function(child1 = "Hamid", child2 = "Majid", child3 = "Nader")

# -----------------------------------
def my_function(**kid):  
    print("His last name is " + kid["lname"])  
  
my_function(fname = "Hamid", lname = "Shaiegh")

# -----------------------------------
def my_function(country = "Norway"):  
    print("I am from " + country)  
  
my_function("Sweden")  
my_function("India")  
my_function()  
my_function("Brazil")

# -----------------------------------
# Return Values
def my_function(x):  
    return 5 * x  
 
y = my_function(3)
print(y)

# -----------------------------------
# The pass Statement
def myfunction():  
    pass
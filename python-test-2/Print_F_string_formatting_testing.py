# Testing Print F String formatting



# To insert characters that are illegal in a string, use an escape character.
print("To insert characters that are illegal in a string, use an escape character.")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

print()
print()
print()





# To format values in an f-string, add placeholders {},
# a placeholder can contain variables, operations,
# functions, and modifiers to format the value.
print("To format values in an f-string, add placeholders {}")
price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can also include a modifier to format the value.
print("placeholder can also include a modifier to format the value.")
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# You can also format a value directly without keeping it in a variable:
print("You can also format a value directly without keeping it in a variable")
txt = f"The price is {95:.2f} dollars"
print(txt)

print()
print()
print()







# You can perform if...else statements inside the placeholders:
print("You can perform if...else statements inside the placeholders")
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

# You can execute functions inside the placeholder:
print("You can execute functions inside the placeholder")
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


# The function does not have to be a built-in Python method,
# you can create your own functions and use them:
print("you can create your own functions and use them")
def myconverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)


print()
print()
print()







# Before Python 3.6 we used the format() method to format strings.
# The format() method can still be used, but f-strings are faster
# and the preferred way to format strings.
print("format() method to format strings")

# Add a placeholder where you want to display the price:
print("Add a placeholder where you want to display the price")
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Format the price to be displayed as a number with two decimals:
print("Format the price to be displayed as a number with two decimals")
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# If you want to use more values, just add more values to the format() method:
print("If you want to use more values, just add more values to the format() method")
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


print()
print()
print()





print("You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders")
# You can use index numbers (a number inside the curly brackets {0}) to be
# sure the values are placed in the correct placeholders
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print("You can also use named indexes by entering a name inside the curly brackets {carname}")
# You can also use named indexes by entering a name inside the curly brackets {carname}
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))





# Python3 program introducing f-string
print("Python3 program introducing f-string")
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")


print()
print()
print()









# Prints today's date with help
# of datetime library
print("Prints today's date with help")
import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")



# We can also evaluate expressions with f-strings in Python.
# To do so we have to write the expression inside the curly
# braces in f-string and the evaluated result will be printed
print("Evaluate Expressions with f-Strings in Python")
english = 78
maths = 56
hindi = 85
print(f"Ram got total marks {english + maths + hindi} out of 300")

print()
print()
print()








# f-string expression part cannot include a backslash
# However, we can put the backslash into a variable as a workaround though:
print("f-string expression part cannot include a backslash")
newline = ord('\n')
print(f"newline: {newline}")
# We cannot use comments inside F-string expressions. It will give an error:
print("We cannot use comments inside F-string expressions")
print("GeeksforGeeks is {5*2 + 3 #geeks-5} characters.")
# This will cause error


# Python String format() Method
# The format() method is a powerful tool that allows developers to create
# formatted strings by embedding variables and values into placeholders
# within a template string.
print("format() method is a powerful tool")
name2 = "Ram"
age2 = 22
message = "My name is {0} and I am {1} years \
                    old. {1} is my favorite \
                    number.".format(name2, age2)
print(message)


print()
print()
print()




print("Format A String That Contains Curly Braces")
txt = "I have {an:.2f} Rupees!"
print(txt.format(an = 4))


print("string bracket notation program to demonstrate the str. format()")
# using format option in a simple string
print("{}, A computer science portal for geeks."
      .format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))



# Multiple placeholders in format() function
print("Multiple placeholders in format() function")
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old"
      .format("User", 19))

# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}"
      .format("one", "two", "three", "four"))


print()
print()
print()







print("Formatters with Positional and Keyword Arguments")
print("Positional arguments")
# Positional arguments
# are placed in order
print("{0} love {1}!!".format("GeeksforGeeks",
                              "Geeks"))

print("Reverse the index numbers")
# Reverse the index numbers with the
# parameters of the placeholders
print("{1} love {0}!!".format("GeeksforGeeks",
                              "Geeks"))


print("Every {} should know the use of {} {} programming and {}"
      .format("programmer", "Open", "Source",
              "Operating Systems"))

print("Use the index numbers")
# Use the index numbers of the
# values to change the order that
# they appear in the string
print("Every {3} should know the use of {2} {1} programming and {0}"
      .format("programmer", "Open", "Source", "Operating Systems"))


print("Keyword arguments")
# Keyword arguments are called
# by their keyword name
print("{gfg} is a {0} science portal for {1}"
      .format("computer", "geeks", gfg="GeeksforGeeks"))


print()
print()
print()







print("Using %s – string conversion via str() prior to formatting")
# Using %c– character  prior to formatting
type = 'bug'
result = 'troubling'
print('I wondered why the program was %s me. Then\
it dawned on me it was a %s .' %
      (result, type))

print()
print()
print()






print("Padding Substitutions or Generating Spaces")
# Padding Substitutions or Generating Spaces
# By default, strings are left-justified within the field, and numbers are right-justified.
# <   :  left-align text in the field
# ^   :  center text in the field
# >   :  right-align text in the field
# To demonstrate spacing when
# strings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!"
      .format("GeeksforGeeks", "geeks"))

# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside !"
      .format(40))

# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!"
      .format("GeeksforGeeks", 2009))

# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<4}!"
      .format("GeeksforGeeks", 2009))

print("{:*^20s}".format("Geeks"))

print()
print()
print()





print("Formatters are generally used to Organize Data")
# Formatters are generally used to Organize Data.
# Formatters can be seen in their best light when
# they are being used to organize a lot of data in a visual way.
# If we are showing databases to users,
# using formatters to increase field size and
# modify alignment can make the output more readable.


# which prints out i, i ^ 2, i ^ 3,
#  i ^ 4 in the given range

# Function prints out values
# in an unorganized manner
def unorganized(a, b):
    for i in range(a, b):
        print(i, i**2, i**3, i**4)

# Function prints the organized set of values
def organized(a, b):
    for i in range(a, b):

        # Using formatters to give 6
        # spaces to each set of values
        print("{:6d} {:6d} {:6d} {:6d}"
              .format(i, i ** 2, i ** 3, i ** 4))

# Driver Code
n1 = 3 #int(input("Enter lower range :-\n"))
n2 = 9 #int(input("Enter upper range :-\n"))

print("------Before Using Formatters-------")

# Calling function without formatters
unorganized(n1, n2)

print()
print("-------After Using Formatters---------")
print()

# Calling function that contains
# formatters to organize the data
organized(n1, n2)



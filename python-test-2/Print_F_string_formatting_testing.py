# Testing Print F String formatting

# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")


# Prints today's date with help
# of datetime library
import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

english = 78
maths = 56
hindi = 85
print(f"Ram got total marks {english + maths + hindi} out of 300")

# f-string expression part cannot include a backslash
# However, we can put the backslash into a variable as a workaround though:
newline = ord('\n')
print(f"newline: {newline}")
# We cannot use comments inside F-string expressions. It will give an error:
# f"GeeksforGeeks is {5*2 + 3 #geeks-5} characters."
# This will cause error

# Python String format() Method
# The format() method is a powerful tool that allows developers to create
# formatted strings by embedding variables and values into placeholders
# within a template string.

name2 = "Ram"
age2 = 22
message = "My name is {0} and I am {1} years \
                    old. {1} is my favorite \
                    number.".format(name2, age2)
print(message)

txt = "I have {an:.2f} Rupees!"
print(txt.format(an = 4))


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
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old"
      .format("User", 19))

# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}"
      .format("one", "two", "three", "four"))

# Positional arguments
# are placed in order
print("{0} love {1}!!".format("GeeksforGeeks",
                              "Geeks"))

# Reverse the index numbers with the
# parameters of the placeholders
print("{1} love {0}!!".format("GeeksforGeeks",
                              "Geeks"))


print("Every {} should know the use of {} {} programming and {}"
      .format("programmer", "Open", "Source",
              "Operating Systems"))


# Use the index numbers of the
# values to change the order that
# they appear in the string
print("Every {3} should know the use of {2} {1} programming and {0}"
      .format("programmer", "Open", "Source", "Operating Systems"))


# Keyword arguments are called
# by their keyword name
print("{gfg} is a {0} science portal for {1}"
      .format("computer", "geeks", gfg="GeeksforGeeks"))


# Using %c– character  prior to formatting
type = 'bug'
result = 'troubling'
print('I wondered why the program was %s me. Then\
it dawned on me it was a %s .' %
      (result, type))


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
n1 = int(input("Enter lower range :-\n"))
n2 = int(input("Enter upper range :-\n"))

print("------Before Using Formatters-------")

# Calling function without formatters
unorganized(n1, n2)

print()
print("-------After Using Formatters---------")
print()

# Calling function that contains
# formatters to organize the data
organized(n1, n2)



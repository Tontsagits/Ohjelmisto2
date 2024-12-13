# Testing creating variable names dynamically

# printing some variable names with dynamic number at the end
name = "item"
for i in range(1, 10):
    print(f"{name}{i}")


# storing some variable names with dynamic number at the end into a list
name = "item"
strings = [f"{name}{i}" for i in range(1, 10)]
print(strings)

'''
self.hissit = []
for hissi in self.hissit:
    print(f"Hissi: {hissi}")
'''

'''
self.hissit = []
print(" ".join(f"Hissi: {hissi}" for hissi in self.hissit))
print("\n".join(f"Hissi: {hissi}" for hissi in self.hissit))
'''

'''
self.hissit = []

You can't use = inside append().
self.hissit.append(f"hissi{i}" = Hissi(self.alin, self.ylin))

Here’s how to fix it:
self.hissit.append(Hissi(self.alin, self.ylin))

If you want to store each new Hissi instance with a dynamic name, you should use a dictionary.
self.hissit = {}
self.hissit[f"hissi{i}"] = Hissi(self.alin, self.ylin)
'''

'''
Yes, you can dynamically create variable names, but it's generally better to use collections
like dictionaries or lists to store dynamically named items.
Creating variable names dynamically can lead to confusing and hard-to-maintain code.
Here's how you can do it with a dictionary:
'''

# Dynamic variables in dictionary

names = {}
for i in range(1, 10):
    names[f"name{i}"] = f"value{i}"
print(names)


# Dynamic variable names
for i in range(1, 10):
    exec(f"name{i} = f'value{i}'")
# Example usage
print(name1)  # Outputs: value1
print(name9)  # Outputs: value9
'''
A cleaner and more maintainable approach is to use a dictionary:
'''
variables = {}
for i in range(1, 10):
    variables[f"name{i}"] = f"value{i}"
# Example usage
print(variables['name1'])  # Outputs: value1
print(variables['name9'])  # Outputs: value9

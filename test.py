import main

iss = main.Iss()

# Print documentation
print(iss.__doc__)

# Print the location
print(iss.location())

# Print the crew names
print(iss.crews())

# Print the total crews
print(iss.count())
import main

nasa = main.Nasa()

# Print documentation
print(nasa.__doc__)

# Print the location
print(nasa.location())

# Print the crew names
print(nasa.crews())

# Print the total crews
print(nasa.count())
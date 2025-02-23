car = {  
    "brand": "Ford",  
    "model": "Mustang",  
    "year": 1964  
}  
print(car)

# Dictionary Items - Data Types
# String, int, boolean, and list data types:
thisdict = {  
    "brand": "Ford",  
    "electric": False,  
    "year": 1964,  
    "colors": ["red", "white", "blue"]  
}

# Accessing Items
car = {  
    "brand": "Ford",  
    "model": "Mustang",  
    "year": 1964  
}
x = car["model"]
print(x)

# Get Keys & Values
car = {  
    "brand": "Ford",  
    "model": "Mustang",  
    "year": 1964  
}

x = car.keys()  
y = car.values()  
print(x)
print(y)

# Change Values
car = {  
    "brand": "Ford",  
    "model": "Mustang",  
    "year": 1964  
}
car["year"] = 2018

# Update Dictionary
car = {  
    "brand": "Ford",  
    "model": "Mustang",  
    "year": 1964  
}

# Adding Items
car = {  
    "brand": "Ford",  
    "model": "Mustang",  
    "year": 1964  
}
car["color"] = "red"  
print(car)

# Removing Items
car = {  
    "brand": "Ford",  
    "model": "Mustang",  
    "year": 1964  
}
car.pop("model")  
print(car)
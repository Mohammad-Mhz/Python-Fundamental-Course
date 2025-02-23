fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit)

# Access Items
print(fruit[1])

# Negative Indexing
print(fruit[-1])

# Range of Indexes
print(fruit[2:5])
print(fruit[:4])
print(fruit[2:])

# Check if Item Exists
if "apple" in fruit:  
    print("Yes, 'apple' is in the fruits list")

# Change Item Value
fruit = ["apple", "banana", "cherry"]  
fruit[1] = "blackcurrant"  
print(fruit)
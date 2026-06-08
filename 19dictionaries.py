"""
PYTHON DICTIONARIES – COMPLETE COMMENTED GUIDE
==============================================
Dictionaries store data as KEY:VALUE pairs.
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be ANY data type (including lists, dicts, etc.)
- Ordered (since Python 3.7), mutable, no duplicate keys
"""

# =============================================================================
# 🔹 BASIC CREATION & PROPERTIES
# =============================================================================

# Create with curly braces {}
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Dictionaries are ordered (Python 3.7+), changeable, no duplicate keys
print(thisdict)           # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(type(thisdict))     # <class 'dict'>
print(len(thisdict))      # 3

# Duplicate keys overwrite previous values
dup_dict = {"a": 1, "a": 2}
print(dup_dict)           # {'a': 2}

# Values can be any data type
mixed = {
    "brand": "Ford",          # string
    "electric": False,        # boolean
    "year": 1964,             # int
    "colors": ["red", "white"]# list
}

# Alternative creation using dict() constructor
person = dict(name="John", age=36, country="Norway")


# =============================================================================
# 🔹 ACCESSING ITEMS
# =============================================================================

# Square bracket access (raises KeyError if key missing)
x = thisdict["model"]         # 'Mustang'

# Safe access with .get() — returns None or default if key missing
x = thisdict.get("model")     # 'Mustang'
x = thisdict.get("color", "N/A")  # 'N/A' (no crash!)

# Get all keys / values / items as VIEW objects (live-updating)
keys_view   = thisdict.keys()    # dict_keys(['brand', 'model', 'year'])
values_view = thisdict.values()  # dict_values(['Ford', 'Mustang', 1964])
items_view  = thisdict.items()   # dict_items([('brand','Ford'), ...])

# Views reflect changes automatically
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
k = car.keys()
print(k)                # before: dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
print(k)                # after:  dict_keys(['brand', 'model', 'year', 'color'])

# Check if a key exists
if "model" in thisdict:
    print("Model key exists!")


# =============================================================================
# 🔹 CHANGING & ADDING ITEMS
# =============================================================================

# Change value by key
thisdict["year"] = 2018

# Add new key-value pair
thisdict["color"] = "red"

# Update multiple items at once via .update()
thisdict.update({"year": 2020, "mileage": 5000})

# setdefault(): get value if exists, else insert with default
config = {}
config.setdefault("theme", "dark")   # inserts 'theme':'dark'
config.setdefault("theme", "light")  # does NOT overwrite → still 'dark'


# =============================================================================
# 🔹 REMOVING ITEMS
# =============================================================================

d = {"a": 1, "b": 2, "c": 3}

d.pop("b")            # removes key 'b', returns its value (2)
d.popitem()           # removes LAST inserted pair (LIFO since 3.7)
del d["a"]            # deletes specific key
# del d               # ⚠️ deletes entire dictionary object
d.clear()             # empties dict → {}


# =============================================================================
# 🔹 LOOPING THROUGH A DICTIONARY
# =============================================================================

sample = {"x": 10, "y": 20, "z": 30}

# Loop keys only
for key in sample:
    print(key)                    # x, y, z

# Loop values only
for val in sample.values():
    print(val)                    # 10, 20, 30

# Loop both keys and values
for key, val in sample.items():
    print(f"{key}: {val}")       # x: 10 / y: 20 / z: 30


# =============================================================================
# 🔹 NESTED DICTIONARIES
# =============================================================================

myfamily = {
    "child1": {"name": "Emil",  "year": 2004},
    "child2": {"name": "Tobias","year": 2007},
    "child3": {"name": "Linus", "year": 2011}
}

# Access nested value
print(myfamily["child2"]["name"])   # Tobias

# Loop through nested dictionaries
for child_key, child_data in myfamily.items():
    print(child_key)
    for attr, val in child_data.items():
        print(f"  {attr}: {val}")


# =============================================================================
#  BUILT-IN METHODS REFERENCE
# =============================================================================
# clear()      → Removes all elements
# copy()       → Returns a shallow copy
# fromkeys()   → Creates dict from iterable of keys + optional value
# get(k[,d])   → Returns value for k, or d (default None)
# items()      → View of (key, value) tuples
# keys()       → View of keys
# pop(k[,d])   → Removes & returns value for k; raises KeyError if missing
# popitem()    → Removes & returns last inserted (key, value) tuple
# setdefault() → Like get(), but inserts key with default if missing
# update()     → Merges another dict/iterable into this one
# values()     → View of values
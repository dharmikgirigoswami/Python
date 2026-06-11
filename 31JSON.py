"""
PYTHON JSON – COMPLETE GUIDE
============================
JSON (JavaScript Object Notation) is a lightweight syntax for storing and 
exchanging data. It is the standard format for APIs, web services, and 
configuration files.

Python has a built-in `json` module to handle JSON data.
"""

import json

# =============================================================================
# 1. PARSING JSON (JSON String ➡️ Python Object)
# =============================================================================
# If you have a JSON string (e.g., from an API response), you can parse it 
# into a Python dictionary using json.loads() (load string).

# 🔹 Basic Example from text
json_string = '{ "name":"John", "age":30, "city":"New York"}'

# Parse the JSON string
python_dict = json.loads(json_string)

# Now it's a Python dictionary, so we can access it normally
print("Parsed Name:", python_dict["name"])  # John
print("Parsed Age:", python_dict["age"])    # 30

# 🌟 Self-Generated Example: Processing a Mock API Response
api_response = '''
{
    "status": "success",
    "data": {
        "user_id": 101,
        "is_active": true,
        "roles": ["admin", "editor"]
    }
}
'''
parsed_response = json.loads(api_response)
user_roles = parsed_response["data"]["roles"]
print(f"\n🔍 User roles from API: {user_roles}")  # ['admin', 'editor']


# =============================================================================
# 2. CONVERTING PYTHON TO JSON (Python Object ➡️ JSON String)
# =============================================================================
# If you have a Python object, you can convert it into a JSON string using 
# json.dumps() (dump string).

# 🔹 Basic Example from text
python_obj = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string_out = json.dumps(python_obj)
print("\n📦 Python to JSON string:", json_string_out)

#  Python to JSON Type Conversion Table
# When converting, Python types map to their JSON equivalents:
"""
Python Type       ➡️  JSON Equivalent
----------------      -----------------
dict                ️  Object
list                ➡️  Array
tuple               ➡️  Array
str                 ➡️  String
int / float         ➡️  Number
True                ➡️  true
False               ➡️  false
None                ➡️  null
"""

#  Example showing all legal data types
complex_obj = {
    "name": "John",
    "age": 30,
    "married": True,          # ➡️ true
    "divorced": False,        # ➡️ false
    "children": ("Ann", "Billy"), # tuple ➡️ Array
    "pets": None,             # ➡️ null
    "cars": [                 # list ➡️ Array
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print("\n📦 Complex object to JSON:")
print(json.dumps(complex_obj))


# =============================================================================
# 3. FORMATTING AND BEAUTIFYING JSON
# =============================================================================
# By default, json.dumps() outputs a single, hard-to-read line. 
# You can use parameters to format it beautifully.

# 🔹 1. Indentation (indent)
# Adds line breaks and indentation for readability.
print("\n🎨 Formatted with indent=4:")
print(json.dumps(complex_obj, indent=4))

# 🔹 2. Custom Separators (separators)
# Default is (", ", ": "). You can change this to save space or match a specific style.
print("\n🎨 Custom separators (compact):")
print(json.dumps(complex_obj, indent=4, separators=(". ", " = ")))

# 🔹 3. Sorting Keys (sort_keys)
# Sorts the dictionary keys alphabetically in the output.
print("\n🎨 Sorted keys:")
print(json.dumps(complex_obj, indent=4, sort_keys=True))


# =============================================================================
# 4. REAL-WORLD SCENARIOS (Self-Generated)
# =============================================================================

# 🌟 Scenario A: Reading and Writing JSON Files
# While json.loads() and json.dumps() handle strings, 
# json.load() and json.dump() handle FILES directly.

# 1. Saving a Python dictionary to a JSON file
user_preferences = {
    "theme": "dark",
    "notifications": True,
    "font_size": 14
}

# (In a real script, you would use: 
#  with open('config.json', 'w') as file:
#      json.dump(user_preferences, file, indent=4)
print("\n💾 (Simulated) Saved preferences to config.json")

# 2. Loading a JSON file into Python
# (In a real script, you would use:
#  with open('config.json', 'r') as file:
#      loaded_prefs = json.load(file)
print("📂 (Simulated) Loaded preferences from config.json")


# 🌟 Scenario B: Handling JSON Errors Safely
# JSON parsing can fail if the string is malformed. Always use try/except!

bad_json_string = '{ "name": "John", "age": 30' # Missing closing brace

try:
    json.loads(bad_json_string)
except json.JSONDecodeError as e:
    print(f"\n⚠️ JSON Decode Error caught: {e}")
    print("Action: Returning default empty dictionary.")
    safe_data = {}


# =============================================================================
#  QUICK RECAP & PRO-TIPS
# =============================================================================
# 1. The "s" stands for String:
#    - json.loads()  ➡️ Parse a JSON STRING into Python.
#    - json.dumps()  ➡️ Dump Python object into a JSON STRING.
#    - json.load()   ➡️ Read from a JSON FILE.
#    - json.dump()   ➡️ Write to a JSON FILE.
#
# 2. None vs Null:
#    - Python uses `None`. JSON uses `null`. The `json` module handles 
#      the conversion automatically.
#
# 3. Tuples become Arrays:
#    - JSON doesn't have a "tuple" concept. If you dump a Python tuple, 
#      it becomes a JSON array (list). When you load it back, it becomes 
#      a Python list, not a tuple.
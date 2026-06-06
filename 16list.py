# Lists are used to store multiple items in a single variable.

thislist = ["apple", "banana", "cherry"]
print(thislist)

#List Items
#List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Note: There are some list methods that will change the order, but in general: the order of the items will not change
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
#To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#List Items - Data Types
#List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))




# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



# Access second item using index 1 (index starts at 0)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Access last item using negative index -1
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Get items from index 2 to 4 (5 is excluded)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Get items from start up to (but not including) index 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Get items from index 2 to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Get items from -4 (orange) to -1 (excludes mango)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if "apple" exists in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
 
 
 
 
 
   # Change a single item by index
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print("After changing index 1:", thislist)

# Change a range of items (replace 2 items with 2 new ones)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print("After replacing [1:3]:", thislist)

# Insert MORE items than replaced (list grows)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]  # replaces 1 item, inserts 2
print("After inserting extra item:", thislist)  # now has 4 items

# Insert FEWER items than replaced (list shrinks)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]  # replaces 2 items, inserts 1
print("After replacing two with one:", thislist)  # now has 2 items

# Insert an item WITHOUT replacing (using .insert())
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")  # insert at index 2 (becomes third item)
print("After using .insert():", thislist)



# Append an item to the END of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("After append:", thislist)

# Insert an item at a SPECIFIC index (e.g., position 1)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # inserts BEFORE current index 1
print("After insert:", thislist)

# Extend list with another LIST
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("After extend (list):", thislist)

# Extend list with a TUPLE (or any iterable!)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("After extend (tuple):", thislist)

# Remove by value (first occurrence only)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print("After remove('banana'):", thislist)

# Remove first occurrence when duplicates exist
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print("After removing first 'banana':", thislist)

# Remove by index using pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # removes index 1 ("banana")
print("After pop(1):", thislist)

# pop() with no index → removes last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print("After pop() (last item):", thislist)

# Remove by index using 'del'
thislist = ["apple", "banana", "cherry"]
del thislist[0]  # removes first item
print("After del thislist[0]:", thislist)

# Clear all items (list remains, but empty)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("After clear():", thislist)  # prints: []

# Delete the entire list (not just contents!)
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)  # ❌ Would cause NameError — list no longer exists!

thislist = ["apple", "banana", "cherry"]

# 1. Simple for loop (most common)
print("1. For loop over items:")
for x in thislist:
    print(x)

# 2. For loop using index numbers
print("\n2. For loop with index:")
for i in range(len(thislist)):
    print(thislist[i])

# 3. While loop with index
print("\n3. While loop:")
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1  # same as i = i + 1

# 4. List comprehension (note: print() returns None, so this is for side effects only)
print("\n4. List comprehension (for printing):")
[print(x) for x in thislist]


# 1. Sort alphabetically (ascending)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print("Alphabetical sort:", thislist)

# 2. Sort numerically (ascending)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print("Numerical sort:", thislist)

# 3. Sort descending (reverse=True)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print("Descending alphabetical:", thislist)

# 4. Sort numbers descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print("Descending numerical:", thislist)

# 5. Custom sort: closest to 50 first
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print("Custom sort (closest to 50):", thislist)

# 6. Case-sensitive sort (default) → uppercase first!
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("Case-sensitive sort:", thislist)

# 7. Case-insensitive sort using str.lower
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print("Case-insensitive sort:", thislist)


# ❌ WRONG: This creates a REFERENCE, not a copy
thislist = ["apple", "banana", "cherry"]
list2 = thislist  # both names point to the SAME list!
thislist[0] = "kiwi"
print("After modifying 'thislist', list2 shows:", list2)  # also changed!

# ✅ Method 1: Use .copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
thislist[0] = "orange"
print("After .copy(), mylist is unchanged:", mylist)

# ✅ Method 2: Use list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
thislist[0] = "mango"
print("After list(), mylist is unchanged:", mylist)

# ✅ Method 3: Use slice [:]
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
thislist[0] = "grape"
print("After slicing [:], mylist is unchanged:", mylist)

# Method 1: Use + operator (creates a NEW list)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print("Using + :", list3)

# Method 2: Append items one by one (modifies list1)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print("Using append() in loop:", list1)

# Method 3: Use extend() (modifies list1, most efficient)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print("Using extend():", list1)

# append()    → Adds an item to the end of the list
# clear()     → Removes all items (list becomes empty)
# copy()      → Returns a shallow copy of the list
# count(x)    → Returns how many times x appears in the list
# extend(iter)→ Adds all items from an iterable to the end
# index(x)    → Returns the index of the first occurrence of x
# insert(i,x) → Inserts x at position i
# pop(i)      → Removes and returns item at index i (default: last)
# remove(x)   → Removes first occurrence of x
# reverse()   → Reverses the list in place
# sort()      → Sorts the list in place (ascending by default)


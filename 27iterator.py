"""
PYTHON ITERATORS – COMPLETE GUIDE
=================================
An ITERATOR is an object that contains a countable number of values and can be 
iterated upon (traversed through). 

Technically, an iterator in Python is an object that implements the Iterator Protocol, 
which consists of two special methods:
  1. __iter__() : Initializes the iterator and returns the iterator object itself.
  2. __next__() : Returns the next value in the sequence.

⚠️ ITERATOR vs ITERABLE:
- ITERABLE: An object that CAN be iterated over (e.g., lists, tuples, dicts, strings). 
            They contain an `iter()` method to get an iterator.
- ITERATOR: The actual object that produces the values one by one using `next()`.
"""

# =============================================================================
# 1. GETTING AN ITERATOR FROM AN ITERABLE
# =============================================================================
# Built-in collections (lists, tuples, strings) are iterables. 
# We use the iter() function to convert them into iterators.

#  Example from text: Tuple iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry

#  Example from text: String iterator
# Strings are iterables containing a sequence of characters.
mystr = "banana"
mystr_it = iter(mystr)

print(next(mystr_it))  # b
print(next(mystr_it))  # a

# 🌟 Self-Generated Example: Dictionary iterator
# By default, iterating over a dict yields its KEYS.
mydict = {"name": "Alice", "age": 25}
dict_it = iter(mydict)
print(next(dict_it))  # name
print(next(dict_it))  # age


# =============================================================================
# 2. LOOPING THROUGH AN ITERATOR (The `for` loop)
# =============================================================================
# The `for` loop is actually just a convenient wrapper. 
# Under the hood, it calls iter() on the object, then repeatedly calls next() 
# until it hits a StopIteration exception.

#  Example from text: Looping through a tuple
print("\n--- For loop on tuple ---")
for x in mytuple:
    print(x)

# 🔹 Example from text: Looping through a string
print("\n--- For loop on string ---")
for x in mystr:
    print(x)


# =============================================================================
# 3. CREATING A CUSTOM ITERATOR
# =============================================================================
# To create your own iterator, build a class and implement __iter__() and __next__().

#  Example from text: Counting up infinitely
class MyNumbers:
    def __iter__(self):
        self.a = 1  # Initialize the starting value
        return self # Must return the iterator object itself

    def __next__(self):
        x = self.a
        self.a += 1 # Increment for the next call
        return x

# Using the custom iterator
myclass = MyNumbers()
myiter = iter(myclass)

print("\n--- Custom Count Up Iterator ---")
print(next(myiter))  # 1
print(next(myiter))  # 2
print(next(myiter))  # 3

# 🌟 Self-Generated Example: Powers of 2 Iterator
class PowersOfTwo:
    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        result = self.current
        self.current *= 2  # Multiply by 2 for the next iteration
        return result

pow2 = iter(PowersOfTwo())
print("\n--- Powers of 2 ---")
print(next(pow2))  # 1
print(next(pow2))  # 2
print(next(pow2))  # 4
print(next(pow2))  # 8


# =============================================================================
# 4. STOPITERATION (Preventing Infinite Loops)
# =============================================================================
# ⚠️ CRITICAL: If you call next() forever, or use an infinite iterator in a for loop,
# your program will crash or hang. 
# We use `raise StopIteration` to tell the loop when to stop.

# 🔹 Example from text: Stop after 20 iterations
class MyNumbersLimited:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # Signals the end of the iteration

myclass_limited = MyNumbersLimited()
myiter_limited = iter(myclass_limited)

print("\n--- Limited Iterator (For Loop) ---")
# The for loop automatically catches StopIteration and stops gracefully.
for x in myiter_limited:
    print(x, end=" ") 
# Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

#  Self-Generated Example: Countdown Iterator
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > 0:
            val = self.current
            self.current -= 1
            return val
        else:
            raise StopIteration

print("\n\n--- Countdown Iterator ---")
for num in Countdown(5):
    print(num, end=" ")
# Output: 5 4 3 2 1

print("\n\n✅ Iteration complete!")
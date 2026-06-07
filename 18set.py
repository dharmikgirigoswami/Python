"""
PYTHON SETS – COMPLETE GUIDE
============================

A set is an unordered, mutable collection of **unique** items.
- Unordered: No index-based access; order may change.
- Mutable: You can add/remove items (but not modify existing ones).
- Unique: Duplicates are automatically removed.
- Written with curly braces {} or the set() constructor.

Use sets when you need to:
- Eliminate duplicates
- Perform mathematical set operations (union, intersection, etc.)
- Quickly check membership (e.g., "Is this item in the collection?")
"""

# =============================================================================
# 1. Creating a Set
# =============================================================================
fruits = {"apple", "banana", "cherry"}
print("Basic set:", fruits)

# Duplicate values are ignored
with_dup = {"apple", "banana", "cherry", "apple"}
print("With duplicate:", with_dup)  # Only one "apple" remains

# Special case: True == 1 and False == 0 in sets
mixed_bools = {True, 1, False, 0, "hello"}
print("True/1 & False/0 treated as duplicates:", mixed_bools)
# Output includes either True or 1 (not both), same for False/0


# =============================================================================
# 2. Data Types & Length
# =============================================================================
# Sets can hold any hashable type (strings, numbers, booleans, tuples)
diverse_set = {"abc", 34, True, 40, "male"}
print("\nMixed data types:", diverse_set)

# Get number of items
print("Set size:", len(fruits))


# =============================================================================
# 3. Accessing Items
# =============================================================================
# ❌ No indexing! But you can:
# - Loop through items
# - Check membership with 'in'

print("\nLooping through set:")
for item in fruits:
    print("-", item)

print("\nIs 'banana' in the set?", "banana" in fruits)
print("Is 'grape' NOT in the set?", "grape" not in fruits)


# =============================================================================
# 4. Adding Items
# =============================================================================
colors = {"red", "blue"}

# Add one item
colors.add("green")
print("\nAfter add('green'):", colors)

# Add multiple items from any iterable (list, tuple, another set)
more_colors = ["yellow", "purple"]
colors.update(more_colors)
print("After update with list:", colors)


# =============================================================================
# 5. Removing Items
# =============================================================================
nums = {1, 2, 3, 4}

# remove(): raises error if item missing
nums.remove(2)
print("\nAfter remove(2):", nums)

# discard(): no error if item missing
nums.discard(99)  # safe!
print("After discard(99):", nums)

# pop(): removes a RANDOM item (sets are unordered!)
popped = nums.pop()
print("Popped item:", popped)
print("Set after pop:", nums)

# Clear all items
nums.clear()
print("After clear():", nums)

# Delete the entire set variable
del nums
# print(nums) → NameError!


# =============================================================================
# 6. Set Operations (Joining & Comparing)
# =============================================================================
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "date", "elderberry"}

# Union: all items from both sets
union_set = set_a | set_b          # or set_a.union(set_b)
print("\nUnion:", union_set)

# Intersection: only common items
intersect = set_a & set_b          # or set_a.intersection(set_b)
print("Intersection:", intersect)

# Difference: items in A but not in B
diff = set_a - set_b               # or set_a.difference(set_b)
print("Difference (A - B):", diff)

# Symmetric Difference: items in either set, but NOT both
sym_diff = set_a ^ set_b           # or set_a.symmetric_difference(set_b)
print("Symmetric Difference:", sym_diff)


# =============================================================================
# 7. In-Place Updates (Modify Original Set)
# =============================================================================
set_x = {1, 2, 3}
set_y = {3, 4, 5}

set_x.update(set_y)                # adds all from set_y → like |=
print("\nAfter update (|=):", set_x)

set_x = {1, 2, 3}
set_x.intersection_update({2, 3, 4})  # keeps only common items
print("After intersection_update (&=):", set_x)


# =============================================================================
# 8. frozenset – Immutable Sets
# =============================================================================
# Useful when you need a set that can't be changed (e.g., as a dict key)
frozen = frozenset({"a", "b", "c"})
print("\nfrozenset:", frozen)
print("Type:", type(frozen))

# Supports non-mutating operations
another = frozenset({"b", "c", "d"})
print("Union of frozensets:", frozen | another)


# 💡 Key Takeaways:
# - Use sets for uniqueness and fast lookups.
# - Use frozenset when immutability is required.
# - Operators (|, &, -, ^) only work between sets.
# - Methods like .union() accept any iterable (lists, tuples, etc.).

print("\n✅ Sets guide complete!")


"""
PYTHON SET METHODS – COMPLETE DEMO
==================================

This file shows every built-in set method in action.
Each example includes:
- What the method does
- How to use it (method vs operator)
- When to prefer one over the other
"""

# Sample sets for demonstrations
A = {"apple", "banana", "cherry"}
B = {"banana", "date", "elderberry"}
C = {"fig", "grape"}

print("Initial sets:")
print("A =", A)
print("B =", B)
print("C =", C)


# 1. add() → Adds an element
# --------------------------
A_copy = A.copy()
A_copy.add("orange")
print("\n1. add('orange'):", A_copy)


# 2. remove() vs discard()
# ------------------------
# remove() → raises KeyError if missing
# discard() → silent if missing
test_set = {"x", "y"}
test_set.discard("z")      # no error
# test_set.remove("z")     # would raise KeyError


# 3. pop() → Removes a RANDOM element
# -----------------------------------
popped_item = A_copy.pop()
print("3. pop() removed:", popped_item)
print("   Set after pop:", A_copy)


# 4. clear() → Empties the set
# ----------------------------
temp = {"a", "b"}
temp.clear()
print("4. clear() result:", temp)  # set()


# 5. copy() → Shallow copy
# ------------------------
original = {1, 2, 3}
duplicate = original.copy()
duplicate.add(4)
print("5. copy() – original unchanged:", original)


# 6. Set Comparison Methods
# -------------------------

# isdisjoint() → True if NO common elements
print("\n6a. A.isdisjoint(C):", A.isdisjoint(C))  # True

# issubset() → All elements in another set?
subset_check = {"apple", "banana"}.issubset(A)
print("6b. {'apple','banana'} ⊆ A?", subset_check)

# issuperset() → Contains all elements of another set?
print("6c. A ⊇ {'apple'}?", A.issuperset({"apple"}))


# 7. Set Operations (Returning New Sets)
# --------------------------------------

# union() → All unique elements from multiple sets
union_result = A.union(B, C)
print("\n7a. A ∪ B ∪ C:", union_result)

# intersection() → Common elements only
intersect = A.intersection(B)
print("7b. A ∩ B:", intersect)

# difference() → In A but not in B
diff = A.difference(B)
print("7c. A - B:", diff)

# symmetric_difference() → In either, but not both
sym_diff = A.symmetric_difference(B)
print("7d. A △ B:", sym_diff)


# 8. In-Place Update Methods (Modify Original)
# --------------------------------------------

X = {"red", "blue"}
Y = {"blue", "green"}

# update() → Add all from Y
X.update(Y)
print("\n8a. After X.update(Y):", X)

X = {"red", "blue"}  # reset
# intersection_update() → Keep only common items
X.intersection_update(Y)
print("8b. After intersection_update:", X)

X = {"red", "blue"}  # reset
# difference_update() → Remove items found in Y
X.difference_update(Y)
print("8c. After difference_update:", X)

X = {"red", "blue"}  # reset
# symmetric_difference_update() → Keep non-common items
X.symmetric_difference_update(Y)
print("8d. After symmetric_difference_update:", X)


# 9. Operator Shortcuts (Set-Only!)
# ---------------------------------
# Only work between sets (not lists/tuples)
P = {1, 2}
Q = {2, 3}

print("\n9. Operator shortcuts:")
print("P | Q (union):", P | Q)
print("P & Q (intersection):", P & Q)
print("P - Q (difference):", P - Q)
print("P ^ Q (symmetric diff):", P ^ Q)

# ❌ This fails: P | [4,5] → TypeError
# ✅ But this works: P.union([4,5])


# 💡 Pro Tips:
# - Use operators (|, &, etc.) for clean code when working with sets only.
# - Use methods (.union(), etc.) when mixing with lists/tuples.
# - Prefer discard() over remove() unless you need error handling.
# - pop() is unpredictable—only use when order doesn’t matter.

print("\n✅ All set methods demonstrated!")


"""
PYTHON IF STATEMENTS & CONDITIONS – COMPLETE GUIDE
==================================================
This file covers:
- Comparison operators & basic if statements
- Indentation rules & multiple statements
- elif, else, and evaluation order
- Shorthand if & ternary operators
- Logical operators (and, or, not)
- Nested if statements
- The pass statement
"""

# =============================================================================
# 1. COMPARISON OPERATORS & BASIC IF STATEMENTS
# =============================================================================
# Python uses standard mathematical conditions to compare values:
# ==  (Equals)      !=  (Not Equals)
# <   (Less than)   <=  (Less than or equal)
# >   (Greater than) >= (Greater than or equal)

# Basic if syntax:
#   if condition:
#       # indented code block runs only if condition is True

a = 33
b = 200

if b > a:
    print("✅ b is greater than a")

# 🔍 How it works: Python evaluates the condition. If True → runs block. If False → skips.
number = 15
if number > 0:
    print("✅ The number is positive")


# =============================================================================
# 2. INDENTATION & MULTIPLE STATEMENTS
# =============================================================================
# Python uses INDENTATION (whitespace) to define code blocks.
# ❌ This would raise an IndentationError:
#   if b > a:
#   print("b is greater than a")

# ✅ Correct indentation (4 spaces recommended):
age = 20
if age >= 18:
    print("✅ You are an adult")
    print("✅ You can vote")
    print("✅ You have full legal rights")
    # All lines at the same indentation level belong to this if-block


# =============================================================================
# 3. BOOLEAN VARIABLES IN CONDITIONS
# =============================================================================
# You can use boolean variables directly without == True / == False
is_logged_in = True

if is_logged_in:
    print("✅ Welcome back!")

is_admin = False
if not is_admin:
    print("ℹ️ Standard user access only")


# =============================================================================
# 4. ELIF & ELSE (MULTIPLE CONDITIONS)
# =============================================================================
# elif = "else if". Checks conditions top-to-bottom.
# Stops at the FIRST True condition and skips the rest.
# else = fallback if ALL previous conditions are False.

score = 75

if score >= 90:
    print(" Grade: A")
elif score >= 80:
    print("🎓 Grade: B")
elif score >= 70:
    print("🎓 Grade: C")  # ← This runs because 75 >= 70 is True
elif score >= 60:
    print("🎓 Grade: D")
else:
    print("📉 Grade: F")

# 🔸 Important: Even if multiple conditions are technically true,
# only the first matching block executes.
temp = 30
if temp > 25:
    print("️ It's warm")
elif temp > 20:
    print("🌡️ It's mild")
# Output: "️ It's warm" (second condition is never checked)


# =============================================================================
# 5. SHORTHAND IF & TERNARY OPERATORS
# =============================================================================
# 🔹 One-line if (when only ONE statement follows)
x = 10
y = 5
if x > y: print("✅ x is greater")

# 🔹 Ternary Operator (if-else on one line)
# Syntax: value_if_true if condition else value_if_false
max_val = x if x > y else y
print(f"🔢 Maximum: {max_val}")

# 🔹 Setting defaults safely
username = ""
display_name = username if username else "Guest"
print(f"👋 Hello, {display_name}")

# 🔹 Chained ternary (use sparingly for readability)
status = "Pass" if score >= 50 else "Fail" if score > 0 else "Invalid"
print(f"📝 Result: {status}")

# ⚠️ Best Practice: Use ternaries for simple assignments.
# Avoid chaining complex logic; use standard if/elif/else instead.


# =============================================================================
# 6. LOGICAL OPERATORS (and, or, not)
# =============================================================================
# Used to combine multiple conditions.

# 🔹 and → Both conditions must be True
has_ticket = True
has_id = True
if has_ticket and has_id:
    print("🎟️ Entry granted")

# 🔹 or → At least one condition must be True
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print(" Office is closed")

# 🔹 not → Reverses the boolean result
is_raining = False
if not is_raining:
    print("🌤️ Great day for a walk")

# 🔸 Truth Tables (Quick Reference):
# and: T+T=T | T+F=F | F+T=F | F+F=F
# or:  T+T=T | T+F=T | F+T=T | F+F=F
# not: T→F | F→T

# 🔸 Combining operators (Precedence: not > and > or)
age_user = 25
is_student = False
has_coupon = True

if (age_user < 18 or age_user > 65) and not is_student or has_coupon:
    print("💰 Discount applies!")


# =============================================================================
# 7. NESTED IF STATEMENTS
# =============================================================================
# An if statement inside another if statement.
# Useful for checking secondary conditions only when the first is met.

num = 41

if num > 10:
    print(" Number is above 10")
    if num > 20:
        print(" And also above 20!")
    else:
        print("📉 But not above 20.")

# ⚠️ Tip: Deep nesting (>3 levels) reduces readability.
# Consider combining conditions with logical operators instead.


# =============================================================================
# 8. THE PASS STATEMENT
# =============================================================================
# if blocks cannot be empty. Use `pass` as a placeholder during development.

value = 50
if value > 100:
    pass  # ← Does nothing. Prevents IndentationError while you plan logic.
else:
    print("✅ Value is under 100 (placeholder logic done)")

# 💡 Real-world use: Drafting classes/functions, stubbing out conditional branches,
# or temporarily disabling code without breaking syntax.


# =============================================================================
# ✅ QUICK RECAP / BEST PRACTICES
# =============================================================================
# 1. Always indent consistently (4 spaces)
# 2. Use elif for mutually exclusive conditions (stops at first match)
# 3. Prefer .get() or ternary for safe fallbacks
# 4. Group complex conditions with parentheses for clarity
# 5. Avoid deeply nested if chains; flatten with early returns or logical operators
# 6. Use `pass` only as a temporary placeholder, not in production logic


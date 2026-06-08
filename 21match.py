"""
PYTHON MATCH STATEMENT – COMPLETE GUIDE
=======================================
Introduced in Python 3.10, the `match` statement (Structural Pattern Matching)
provides a cleaner, more readable alternative to long if...elif...else chains.

⚠️ REQUIREMENT: This feature requires Python 3.10 or newer.

How it works:
1. The `match` expression is evaluated exactly ONCE.
2. The value is compared against each `case` from top to bottom.
3. The FIRST matching case executes, and the rest are skipped.
"""

# =============================================================================
# 1. BASIC SYNTAX & COMPARISON
# =============================================================================
# Instead of writing many if/elif statements, use match/case.

# ❌ Old way (if/elif):
day = 4
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

# ✅ New way (match/case):
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")  # ← This runs
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


# =============================================================================
# 2. DEFAULT VALUE (WILDCARD)
# =============================================================================
# Use the underscore `_` as the LAST case to catch unmatched values.
# It acts exactly like the `else` block in an if/else statement.

command = "restart"

match command:
    case "start":
        print(" Starting server...")
    case "stop":
        print("🔴 Stopping server...")
    case _:
        print("⚠️ Unknown command. Please use 'start' or 'stop'.")
        # Output: ⚠️ Unknown command... (because "restart" didn't match)


# =============================================================================
# 3. COMBINING VALUES (PIPE OPERATOR)
# =============================================================================
# Use the pipe `|` to check for multiple values in a single case.
# It acts like the `or` operator, keeping your code DRY (Don't Repeat Yourself).

day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("💼 Today is a weekday.")
    case 6 | 7:
        print("🎉 I love weekends!")  # ← This runs
    case _:
        print("Invalid day number.")


# =============================================================================
# 4. GUARDS (EXTRA CONDITIONS)
# =============================================================================
# You can add an `if` clause to a case to check an additional condition.
# This is called a "guard". The case only matches if BOTH the value and the guard are true.

month = 5
day = 4

match day:
    # Checks if day is 1-5 AND month is exactly 4
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("🌸 A weekday in April")
        
    # Checks if day is 1-5 AND month is exactly 5
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("🌷 A weekday in May")  # ← This runs
        
    case _:
        print("📅 No specific match found.")


# =============================================================================
# 5. REAL-WORLD EXAMPLE: HTTP STATUS CODES
# =============================================================================
# Match is incredibly useful for handling API responses or error codes.

status_code = 404

match status_code:
    case 200:
        print("✅ Success: Request fulfilled.")
    case 201:
        print("✅ Created: Resource successfully created.")
    case 400 | 401 | 403:
        print("🚫 Client Error: Bad request or unauthorized.")
    case 404:
        print(" Not Found: Resource does not exist.")
    case 500 | 502 | 503:
        print(" Server Error: Something went wrong on our end.")
    case _:
        print(f"️ Unhandled status code: {status_code}")


# =============================================================================
# 6. REAL-WORLD EXAMPLE: USER ROLES
# =============================================================================
# Combining match with guards for permission checks.

user_role = "editor"
is_active = True

match user_role:
    case "admin" if is_active:
        print("👑 Full system access granted.")
    case "admin":
        print("⚠️ Admin account is suspended.")
    case "editor" if is_active:
        print("️ Can edit and publish content.")
    case "viewer":
        print("️ Read-only access.")
    case _:
        print("🔒 No permissions assigned.")


# =============================================================================
# 💡 QUICK RECAP / BEST PRACTICES
# =============================================================================
# 1. Use `match` when comparing a single variable against 3+ specific values.
# 2. Always put the wildcard `_` at the very end as a fallback.
# 3. Use `|` to group cases that share the same action.
# 4. Use guards (`if`) for secondary conditions, but don't overcomplicate them.
# 5. If you only have 2 conditions, a standard `if/else` is still better.
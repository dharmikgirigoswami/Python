"""
PYTHON TRY EXCEPT (EXCEPTION HANDLING) – COMPLETE GUIDE
=======================================================
Exception handling allows you to test a block of code for errors and handle them 
gracefully, preventing your entire program from crashing.

Core Blocks:
- try:     Tests a block of code for errors.
- except:  Handles the error if one occurs.
- else:    Executes code ONLY if NO errors were raised in the try block.
- finally: Executes code REGARDLESS of the try/except results (great for cleanup).
"""

# =============================================================================
# 1. THE BASICS: TRY AND EXCEPT
# =============================================================================
# If an error occurs in the `try` block, Python jumps to the `except` block.
# Without this, the program would crash and show a traceback.

# ❌ Without try/except, this crashes the program:
# print(x)  # NameError: name 'x' is not defined

# ✅ With try/except, the program survives:
try:
    print(x)  # x is not defined, so this triggers an error
except:
    print("⚠️ An exception occurred! (Variable x is not defined)")


# =============================================================================
# 2. HANDLING MULTIPLE & SPECIFIC EXCEPTIONS
# =============================================================================
# You can define multiple `except` blocks to handle different types of errors 
# in specific ways. It's best practice to catch specific errors before generic ones.

try:
    # This will raise a NameError
    print(undefined_variable) 
except NameError:
    print(" NameError: The variable is not defined.")
except ZeroDivisionError:
    print(" ZeroDivisionError: You cannot divide by zero.")
except Exception as e:
    # Catches any other error and prints the actual error message
    print(f"❌ Something else went wrong: {e}")

# 🌟 Self-Generated Example: Safe Division
print("\n--- Safe Division Example ---")
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("️ Cannot divide by zero!")
except TypeError:
    print("⚠️ Please provide numbers, not strings!")


# =============================================================================
# 3. THE `else` BLOCK
# =============================================================================
# The `else` block runs ONLY if the `try` block finishes WITHOUT raising an error.
# It's useful for code that should only run if the test was successful.

try:
    print("✅ Hello")  # No error here
except:
    print("❌ Something went wrong")
else:
    print("🎉 Nothing went wrong! The else block executed.")


# =============================================================================
# 4. THE `finally` BLOCK
# =============================================================================
# The `finally` block runs NO MATTER WHAT. Whether there was an error or not.
# It is primarily used for cleaning up resources (like closing files or network connections).

print("\n--- Finally Block Example ---")
try:
    print(y)  # Error occurs here
except:
    print("❌ Something went wrong in the try block")
finally:
    print("🧹 The 'try except' is finished. Cleanup complete.")

# 🔹 Real-World Example: File Handling
# If we open a file, we MUST close it, even if writing fails.
print("\n--- File Handling Example ---")
try:
    # Simulating opening a file (using a mock object for this script)
    f = open("demofile.txt", "w")
    try:
        # Simulating a write error (e.g., file is read-only)
        f.write("Lorum Ipsum") 
    except:
        print("❌ Something went wrong when writing to the file")
    finally:
        f.close()  # This ALWAYS runs, ensuring the file isn't left open
        print("🔒 File closed successfully.")
except:
    print("❌ Something went wrong when opening the file")


# =============================================================================
# 5. RAISING EXCEPTIONS (`raise`)
# =============================================================================
# As a developer, you can manually trigger (throw) an exception if a certain 
# condition occurs using the `raise` keyword.

# 🔹 Raising a generic Exception
x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# 🔹 Raising a specific Error Type (e.g., TypeError, ValueError)
x_val = "hello"
# if not type(x_val) is int:
#     raise TypeError("Only integers are allowed")

# 🌟 Self-Generated Example: User Age Validation
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise PermissionError("You must be 18 or older to access this content.")
    return "Access Granted"

try:
    check_age(15)
except ValueError as ve:
    print(f"⚠️ Value Error: {ve}")
except PermissionError as pe:
    print(f"🔒 Permission Error: {pe}")


# =============================================================================
#  BEST PRACTICES & PRO-TIPS
# =============================================================================
# 1. Avoid Bare `except:`: 
#    Writing just `except:` catches EVERYTHING, including system exits (Ctrl+C).
#    Always specify the error type (e.g., `except ValueError:`) or use `except Exception as e:`.
#
# 2. Keep `try` blocks small:
#    Only wrap the specific lines of code that might fail. Don't wrap your whole program.
#
# 3. Use Context Managers (`with` statement) for files:
#    Instead of using `try/finally` to close files, Python's `with` statement 
#    handles closing automatically, even if an error occurs:
#
#    with open("file.txt", "r") as f:
#        content = f.read()
#    # File is automatically closed here!
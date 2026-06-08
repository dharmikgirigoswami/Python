"""
PYTHON WHILE LOOPS – COMPLETE GUIDE
===================================
Python has two primary loop commands: `while` and `for`.
This file focuses on the `while` loop, which executes a block of code 
repeatedly as long as a specified condition remains True.

⚠️ CRITICAL: You must update the condition variable inside the loop, 
otherwise you will create an infinite loop that crashes your program!
"""

# =============================================================================
# 1. BASIC WHILE LOOP
# =============================================================================
# Syntax:
#   while condition:
#       # code block
#       # update condition variable

#  Example from text: Print numbers 1 to 5
i = 1
while i < 6:
    print(f"Count: {i}")
    i += 1  # ⚠️ Crucial: Increment 'i' to eventually make the condition False
# Output: 1, 2, 3, 4, 5

# 🔹 My Example: A simple countdown timer
countdown = 5
while countdown > 0:
    print(f"🚀 Launch in {countdown}...")
    countdown -= 1  # Decrementing
print("Liftoff! 🚀")


# =============================================================================
# 2. THE `break` STATEMENT
# =============================================================================
# The `break` statement immediately terminates the loop, 
# even if the while condition is still True.

# 🔹 Example from text: Exit when i is 3
i = 1
while i < 6:
    print(f"Current i: {i}")
    if i == 3:
        print(" Breaking the loop!")
        break
    i += 1
# Output: 1, 2, 3 (then stops)

#  My Example: Searching for a target number in a sequence
target = 7
num = 1
while num <= 10:
    if num == target:
        print(f"✅ Found target {target} at step {num}!")
        break
    num += 1


# =============================================================================
# 3. THE `continue` STATEMENT
# =============================================================================
# The `continue` statement skips the rest of the current iteration 
# and jumps back to the top of the loop to evaluate the condition again.

# 🔹 Example from text: Skip printing when i is 3
i = 0
while i < 6:
    i += 1  # ⚠️ Must increment BEFORE the continue check to avoid infinite loop!
    if i == 3:
        continue  # Skips the print() below and goes back to the while check
    print(f"Number: {i}")
# Output: 1, 2, 4, 5, 6 (3 is missing)

# 🔹 My Example: Processing a list of numbers but skipping negatives
numbers = [-2, -1, 0, 1, 2, 3]
index = 0
while index < len(numbers):
    val = numbers[index]
    index += 1
    if val < 0:
        continue  # Skip negative numbers
    print(f"Processing positive/zero value: {val}")


# =============================================================================
# 4. THE `else` CLAUSE
# =============================================================================
# The `else` block runs EXACTLY ONCE when the while condition becomes False.
#  IMPORTANT: The `else` block is SKIPPED if the loop is exited via `break`.

# 🔹 Example from text: Print message when condition is false
i = 1
while i < 6:
    # print(i) # (omitted to keep output clean)
    i += 1
else:
    print("✅ i is no longer less than 6. Loop finished naturally!")

# 🔹 My Example: Password retry limit (Demonstrating break vs else)
print("\n--- Password Attempt Demo ---")
attempts = 0
max_attempts = 3
correct_password = "secret123"

# Scenario A: User fails all attempts (else block WILL run)
print("Scenario A (Failing):")
attempts = 0
while attempts < max_attempts:
    attempts += 1
    # Imagine user enters wrong password here
    if attempts == max_attempts:
        print("❌ Too many failed attempts.")
        break  # Because of 'break', the else block below is SKIPPED
else:
    # This only runs if the loop finishes WITHOUT hitting 'break'
    print("🔒 Account locked.") 

# Scenario B: User succeeds (else block WILL run)
print("\nScenario B (Succeeding):")
attempts = 0
while attempts < max_attempts:
    attempts += 1
    if attempts == 2:
        print("✅ Password accepted!")
        break  # Exits loop
else:
    # This is skipped because we used 'break'
    print(" Account locked.")
    
# 💡 Pro-Tip: The `else` clause is perfect for "loop completed without finding what we wanted" 
# or "loop completed without errors".


# =============================================================================
# 5. REAL-WORLD SCENARIO: MENU LOOP
# =============================================================================
# A common use case for while loops is keeping a program running until the user chooses to exit.

running = True

print("\n--- Simple Menu ---")
while running:
    print("\nOptions: [1] Check Balance, [2] Deposit, [3] Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("💰 Your balance is $1,000.")
    elif choice == '2':
        print("💵 Deposit functionality coming soon!")
    elif choice == '3':
        print("👋 Goodbye!")
        running = False  # Changes condition to False to end the loop
    else:
        print("️ Invalid option. Please try again.")
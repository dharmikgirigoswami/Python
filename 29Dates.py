"""
PYTHON DATETIME MODULE – COMPLETE GUIDE
=======================================
Python does not have a native "date" data type. Instead, we use the built-in 
`datetime` module to work with dates and times as date objects.

A datetime object contains: year, month, day, hour, minute, second, and microsecond.
"""

import datetime

# =============================================================================
# 1. GETTING THE CURRENT DATE & TIME
# =============================================================================
# Use datetime.datetime.now() to get the exact moment the code runs.

current_datetime = datetime.datetime.now()
print(" Current Date & Time:", current_datetime)
# Output format: YYYY-MM-DD HH:MM:SS.ffffff
# Example: 2024-05-15 14:32:10.123456


# =============================================================================
# 2. CREATING CUSTOM DATE OBJECTS
# =============================================================================
# Use the datetime() constructor. Required: year, month, day.
# Optional: hour, minute, second, microsecond, tzinfo (timezone)

# 🔹 Basic date (time defaults to 00:00:00)
my_date = datetime.datetime(2023, 11, 25)
print("\n📆 Custom Date:", my_date)

# 🔹 Date with specific time
event_datetime = datetime.datetime(2024, 12, 31, 23, 59, 59)
print("⏰ Custom DateTime:", event_datetime)

# ⚠️ Note: Month must be 1-12, Day must be valid for the month.
# Invalid dates (e.g., Feb 30) will raise a ValueError.


# =============================================================================
# 3. EXTRACTING DATE & TIME COMPONENTS
# =============================================================================
# Once you have a datetime object, you can access its parts directly.

now = datetime.datetime.now()

print("\n🔍 Extracted Components:")
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)


# =============================================================================
# 4. FORMATTING WITH strftime() (String Format Time)
# =============================================================================
# The .strftime() method converts a datetime object into a formatted string.
# It takes a format string with special directives (starting with %).

formatted_date = now.strftime("%Y-%m-%d")
print(f"\n📝 Formatted Date: {formatted_date}")  # e.g., 2024-05-15

# 🔹 Combining multiple directives
full_format = now.strftime("%A, %B %d, %Y at %I:%M %p")
print(f"📝 Human Readable: {full_format}")  # e.g., Wednesday, May 15, 2024 at 02:30 PM


# =============================================================================
# 5. strftime() FORMAT CODE REFERENCE TABLE
# =============================================================================
# Commonly used directives (keep this as a quick lookup):
"""
Directive   Description                  Example Output
--------    -----------                  --------------
%a          Weekday, short version       Wed
%A          Weekday, full version        Wednesday
%w          Weekday as number (0=Sun)    3
%d          Day of month (01-31)         15
%b          Month, short version         May
%B          Month, full version          May
%m          Month as number (01-12)      05
%y          Year, short (no century)     24
%Y          Year, full version           2024
%H          Hour (00-23)                 14
%I          Hour (00-12)                 02
%p          AM/PM                        PM
%M          Minute (00-59)               30
%S          Second (00-59)               45
%f          Microsecond (000000-999999)  123456
%z          UTC offset                   +0000
%Z          Timezone name                UTC
%j          Day of year (001-366)        136
%c          Local date & time            Wed May 15 14:30:45 2024
%x          Local date                   05/15/24
%X          Local time                   14:30:45
%%          Literal % character          %
"""

# 🌟 Self-Generated Example: Log Timestamp Format
log_entry_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"\n📜 Log Timestamp: [{log_entry_time}] System initialized.")


# =============================================================================
# 6. REAL-WORLD SCENARIOS (Self-Generated)
# =============================================================================

#  Scenario A: Calculate Age from Birthdate
def calculate_age(birthdate_str):
    # Parse string to datetime object (strptime = string parse time)
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.datetime.now()
    
    # Calculate rough age
    age = today.year - birthdate.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

print("\n Age Calculator:")
print(f"Born on 1995-08-20 → Age: {calculate_age('1995-08-20')}")

# 🔹 Scenario B: Generate File Names with Timestamps
def create_timestamped_filename(prefix="report"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.csv"

print(f"\n📁 Generated Filename: {create_timestamped_filename('sales')}")

#  Scenario C: Check if a Date is in the Past/Future
def check_date_status(date_str):
    target = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    now = datetime.datetime.now()
    
    if target < now:
        return "🔴 Past Date"
    elif target > now:
        return "🟢 Future Date"
    else:
        return "🟡 Today"

print(f"\n📅 Status of 2025-01-01: {check_date_status('2025-01-01')}")


# =============================================================================
#  BEST PRACTICES & PRO-TIPS
# =============================================================================
# 1. strftime() vs strptime():
#    - strftime() = Format TIME to STRING (for display/logging)
#    - strptime() = Parse STRING to TIME (for processing calculations)
#
# 2. Timezone Awareness:
#    - By default, datetime objects are "naive" (no timezone info).
#    - For production apps, use `datetime.timezone.utc` or the `zoneinfo` module.
#
# 3. Date Arithmetic:
#    - Use `datetime.timedelta` to add/subtract days, hours, etc.
#    - Example: tomorrow = today + datetime.timedelta(days=1)
#
# 4. Performance:
#    - datetime objects are lightweight, but avoid creating thousands in tight loops.
#    - For heavy date/time math, consider the `dateutil` or `pendulum` libraries.
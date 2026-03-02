# ==============================
# Conditional Statements in Python
# ==============================

# ==============================
# If Statement
# ==============================

print("=== IF Statement ===")

age = 20

if age >= 18:
    print("Eligible to vote.")


# ==============================
# Short-hand if
# ==============================

print("\n=== Short-hand IF ===")

age = 19

if age > 18: 
    print("Eligible to Vote.")


# ==============================
# If-Else Statement
# ==============================

print("\n=== IF ELSE Statement ===")

age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


# ==============================
# Short-hand if-else (Ternary)
# ==============================

print("\n=== Short-hand IF ELSE ===")

marks = 45

res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")


# ==============================
# elif Statement
# ==============================

print("\n=== ELIF Statement ===")

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


# ==============================
# Nested if-else
# ==============================

print("\n=== Nested IF ELSE ===")

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


# ==============================
# Ternary Conditional Statement
# ==============================

print("\n=== Ternary Conditional ===")

age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)


# ==============================
# Match-Case Statement (Python 3.10+)
# ==============================

print("\n=== Match Case ===")

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
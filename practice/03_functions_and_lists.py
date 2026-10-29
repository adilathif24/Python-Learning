# My practice: functions and lists

def add(a, b):
    """Return the sum of two values."""
    return a + b

answer = add(4, 6)
print("Sum:", answer)


def greet(name):
    """Display a greeting for the supplied name."""
    print("Hello", name)

greet("Adil")

names = ["Syed", "Adil", "Ali"]
print("First name:", names[0])

names.append("Athif")
print("Names:", names)
print("Count:", len(names))
print("Is Ali present?", "Ali" in names)

# Check before removing to avoid ValueError if the item is absent.
name_to_remove = "Adil"
if name_to_remove in names:
    names.remove(name_to_remove)

print("After removal:", names)

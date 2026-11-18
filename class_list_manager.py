# Class List Manager - Group 3
# MIS 211 Bonus Assignment (GitHub Teamwork)
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]
# ===== Each student adds her function BELOW this line =====

# Written by: Rand (task 2)
def search_name(names, name):
    for student in names:
        if student.lower() == name.lower():
            return True
    return False


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Is Noura in the list?", search_name(names, "Noura"))
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))

main()

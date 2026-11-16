# COS 101 ASSIGNMENT
# PHYSICS CALCULATOR

# FUNCTION 1: SPEED
def calculate_speed():
    distance = float(input("Enter distance (metres): "))
    time = float(input("Enter time (seconds): "))

    if time == 0:
        print("Time cannot be zero.")
    else:
        speed = distance / time
        print("Speed =", speed, "m/s")


# FUNCTION 2: FORCE
def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))

    force = mass * acceleration
    print("Force =", force, "N")


# FUNCTION 3: DENSITY
def calculate_density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m^3): "))

    if volume == 0:
        print("Volume cannot be zero.")
    else:
        density = mass / volume
        print("Density =", density, "kg/m^3")


# FUNCTION 4: WEIGHT
def calculate_weight():
    mass = float(input("Enter mass (kg): "))
    gravity = 9.81

    weight = mass * gravity
    print("Weight =", weight, "N")


# FUNCTION 5: WORK DONE
def calculate_work():
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (metres): "))

    work = force * distance
    print("Work Done =", work, "J")


# MAIN PROGRAM
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Density")
    print("4. Calculate Weight")
    print("5. Calculate Work Done")

    choice = input("\nChoose a physics operation (1-5): ")

    if choice == "1":
        calculate_speed()

    elif choice == "2":
        calculate_force()

    elif choice == "3":
        calculate_density()

    elif choice == "4":
        calculate_weight()

    elif choice == "5":
        calculate_work()

    else:
        print("Invalid choice. Please select between 1 and 5.")

    # ASK USER IF THEY WANT TO CONTINUE
    again = input("\nWould you like to perform another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
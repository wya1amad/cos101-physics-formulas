```python
# COS 101 Assignment
# Five Physics Formulas

# 1. Speed = Distance / Time
def calculate_speed(distance, time):
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return distance / time


# 2. Force = Mass * Acceleration
def calculate_force(mass, acceleration):
    return mass * acceleration


# 3. Density = Mass / Volume
def calculate_density(mass, volume):
    if volume == 0:
        raise ValueError("Volume cannot be zero.")
    return mass / volume


# 4. Weight = Mass * Gravitational Acceleration
def calculate_weight(mass, gravity=9.81):
    return mass * gravity


# 5. Work Done = Force * Distance
def calculate_work(force, distance):
    return force * distance


# Display results
if __name__ == "__main__":
    print("COS 101 Physics Formulas")
    print("Speed:", calculate_speed(100, 20), "m/s")
    print("Force:", calculate_force(10, 5), "N")
    print("Density:", calculate_density(20, 4), "kg/m^3")
    print("Weight:", calculate_weight(10), "N")
    print("Work Done:", calculate_work(50, 3), "J")
```

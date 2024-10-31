force = 0
mass = 0
acceleration = 0

def logic(mass, acceleration, force):
    force = mass * acceleration
    return force


mass = float(input("Mass: "))
acceleration = float(input("Acceleration: "))

print(logic(mass,acceleration, force))
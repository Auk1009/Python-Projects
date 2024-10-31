force = 0
mass = 0
acceleration = 0

def calculateForce(mass, acceleration):
    force = mass * acceleration
    return force


mass = float(input("Mass: "))
acceleration = float(input("Acceleration: "))

force = calculateForce(mass,acceleration)

print(f'force = {force} N')
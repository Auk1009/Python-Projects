# --- 1. Class Definition (The Blueprint) ---
# This is the base class for all pets. Think of it as the "General Pet" instruction booklet.
class Pet:
    # This is the "constructor" method. It runs when you create a new Pet object.
    # It sets up the initial attributes (characteristics).
    def __init__(self, name, species, noise):
        print(f"Creating a new {species} named {name}!")
        self.name = name         # Attribute: The pet's name
        self.species = species   # Attribute: What kind of animal
        self.noise = noise       # Attribute: The sound it makes

    # This is a method (behavior).
    def make_sound(self):
        print(f"{self.name} says {self.noise}!")

    # Another method.
    def show_info(self):
        print(f"--- Info ---")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Sound: {self.noise}")
        print(f"------------")

    def set_name(self, newName):
        self.name = newName
        print(f"Name changed to {self.name }")
    
    def get_name(self):
        return self.name

# --- 2. Inheritance (Creating Specific Blueprints from the Base) ---
# The Dog class inherits from the Pet class.
# Think: "Dog" booklet uses the "General Pet" booklet and adds dog-specific things.
class Dog(Pet):
    # Dog's own constructor. It first calls the Pet constructor using super()
    def __init__(self, name, breed):
        # Call the Pet class's __init__ method to set up name, species, noise
        super().__init__(name, species="Dog", noise="Woof")
        # Add a Dog-specific attribute
        self.breed = breed
        print(f"{self.name} is a {self.breed}.")

    # Dog-specific method
    def fetch(self):
        print(f"{self.name} excitedly fetches the ball!")

    # Override the show_info method to add breed info (Example of Polymorphism later)
    def show_info(self):
        super().show_info() # Call the original Pet show_info first
        print(f"Breed: {self.breed}") # Add the extra Dog info
        print(f"------------")

# The Cat class also inherits from the Pet class.
class Cat(Pet):
    def __init__(self, name, mood):
        # Call the Pet class's __init__ method
        super().__init__(name, species="Cat", noise="Meow")
        # Add a Cat-specific attribute
        self.mood = mood
        print(f"{self.name} seems to be {self.mood} today.")

    # Cat-specific method
    def judge_you(self):
        print(f"{self.name} stares at you with {self.mood} judgment.")

    # Override make_sound (Example of Polymorphism)
    def make_sound(self):
        if self.mood == "grumpy":
            print(f"{self.name} hisses!")
        else:
            # Call the original Pet make_sound method if not grumpy
            super().make_sound()

# --- 3. Creating Objects (Instances of Classes) ---
# Now we use the blueprints (Classes) to create actual pets (Objects).

print("\n--- Creating Pets ---")
my_dog = Dog(name="Buddy", breed="Golden Retriever") # Creates a Dog object
my_cat = Cat(name="Whiskers", mood="sleepy")       # Creates a Cat object
grumpy_cat = Cat(name="Shadow", mood="grumpy")     # Creates another Cat object

# --- 4. Using Objects (Accessing Attributes and Calling Methods) ---

print("\n--- Interacting with Pets ---")

# Calling methods defined in the base Pet class (available to Dog and Cat via Inheritance)
my_dog.show_info()
my_cat.show_info()

# Calling methods specific to the derived classes
my_dog.fetch()
my_cat.judge_you()
grumpy_cat.judge_you()

print("\n--- Demonstrating Polymorphism ---")
# Polymorphism: Treating different objects (Dog, Cat) in the same way.
# We can put different pets in a list...
pets_list = [my_dog, my_cat, grumpy_cat]

print("Let's hear from all the pets:")
# ...and loop through them, calling the same method 'make_sound()'.
# Each pet will respond correctly based on its specific class implementation.
for pet in pets_list:
    pet.make_sound() # Dog says Woof, sleepy Cat says Meow, grumpy Cat hisses!

print("\n--- Encapsulation Reminder ---")
# Each pet object (my_dog, my_cat) bundles its own data (name, breed/mood)
# and its actions (make_sound, fetch/judge_you) together.
# We interact with the pet through its methods (like my_dog.fetch()),
# we don't need to worry about the internal details of *how* fetching works.
print(f"{my_dog.name} has its own name and breed ({my_dog.breed}).")
print(f"{my_cat.name} has its own name and mood ({my_cat.mood}).")

my_dog.set_name("Snoopy")

print(my_dog.get_name())

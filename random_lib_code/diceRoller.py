import random

def randomize() -> int:
   ran = random.randint(1,7)
   return ran

while True:
   result = randomize()
   print(f"dice -> {result}")
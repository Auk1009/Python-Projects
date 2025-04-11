import random
#Add letters,Alpabets
alphabets = 'abcdefghijklmnopqrstuvwxyz'
password = ''
for letter in alphabets:
    decideralpha = random.choice([0,1])
    if decideralpha == 1:
        password = password + letter
    
#Add numbers to password
numbers = '1234567890'

for num in numbers:
    decidernum = random.choice([0,1])
    if decidernum == 1:
        password = password + num
        

#Add special characters

specialchac = '!#$%*?'

for character in specialchac:
    deciderchract = random.choice([0,1])
    if deciderchract == 1:
        password = password + character
        

#shuffle the password
shuffledpassword = list(password)
random.shuffle(shuffledpassword)
shuffledword = ''.join(shuffledpassword)

print(f"Here is your random password: {shuffledword}")

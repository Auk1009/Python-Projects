# loops practice
#1
# n = int(input('Enter the number: '))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i} ")

#2
l1 = ['Harry', 'Soham', 'Sacthin', 'Rahul']

for items in l1:
    if items.startswith('S'):
        print(f'Good Afternoon, {items}')
    else:
        print('Nothing')

#3
# n = int(input('enter number: '))
# i = 1
# while(i<11):
#     i+=1
#     print(f"{n} X {i} = {n*i} ")

#4
# n = int(input('Enter number: '))

# for i in range(2,n):
#     if n%i == 0:
#         print('number is not prime')
#         break
#     else:
#         print('Nmber is prime')

#5
# n = int(input('Enter number'))
# sum = 0
# i = 0
# while(i<=n):
#     sum  = sum + i
#     i = i + 1
    
# print(sum)

#6
# n = int(input('Enter number: '))
# mul = 1
# for i in range(1,n):
#     i = i +1
#     mul = mul*i
#     print(mul)

# #7
# n = int(input('Enter number: '))
# for i in range(1,n+1):
#     print(' '*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

#8    
n = int(input('Enter number: '))
for i in range(1,n+1):
    print("*"*(i))
    print("")
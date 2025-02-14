# number = int(input('Which number do u what to multiply with?'))
# for x in range(1,11):
#     result = number*x
#     print(f"{number} X {x} = {result}")

total_sum = 0
for number in range(1, 10 + 1):  # end + 1 to include the ending number
   total_sum = total_sum + number
   print(total_sum)
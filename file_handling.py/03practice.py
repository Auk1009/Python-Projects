
for number in range(2,21):
    f = open(f'{number}.txt','w')
    for num in range(1,11):
        t = number*num
        f.write(f"{number}X{num} = {t}\n")
    f.close()
        


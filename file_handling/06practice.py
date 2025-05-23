# file = open('file.html','r')
# content = file.read()
# if 'python' in content:
#     print('Found python')
#     line = 0
#     string = 'python'
#     for string in content:
#         con = file.readline()
#         line += 1
#         if 'python' in con:
#             print(f'python in line {line}')

# else:
#     print('something went wrong')

with open('file.html') as file:
    content = file.read()
    lines = file.readlines()
    lineno = 0
for line in lines:
    print(lineno)
    print('hi')
    lineno += 1
        
    if 'python' in line:
        print(f'found python in line {lineno}')
        break
    



import os

print('current working directory: ',os.getcwd())
os.rmdir('hello.py')
print('content of the current directory: ',os.listdir())
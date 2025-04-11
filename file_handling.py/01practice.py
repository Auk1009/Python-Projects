f = open('/Users/aryanukiran/python/Python-Projects/file_handling.py/poem.txt', 'r')

r = f.read()
if 'Twinkle' in r:
    print('True')
else:
    print('False')
f.close()
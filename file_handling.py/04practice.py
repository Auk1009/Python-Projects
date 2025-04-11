with open('file.txt') as file:
    content = file.read()
    if 'Donkey' in content:
        content.replace('Donkey','######')
    else:
        print('something went wrong')
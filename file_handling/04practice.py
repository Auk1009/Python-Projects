with open('file.txt', 'r+') as file:
    content = file.read()
    file.close()
    print(content)
    if 'Donkey' in content:
        print('here')
        transfer = content
        content = transfer.replace('Donkey','######')
        print(content)
        with open('file.txt', 'r+') as f:
            f.write(content)
    else:
        print('something went wrong')
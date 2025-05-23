with open('this.txt','r') as file:
    content = file.read()


with open('thiscopy.txt', 'w') as f:
    paste = f.write(content)


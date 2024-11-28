import os


def find_file(target_file,path='/Users/aryanukiran/python/Python-Projects'):
    for root, files in os.walk(path):
    
        if target_file in files:
            print(f'found {files}, in {os.path.join(root,target_file)}')

def add_file(name_folder:str):
    os.system(f'cd ..')
    os.mkdir(name_folder)
    os.system(f"cd {name_folder}")
    with open('autofile.py', 'w') as f:
        f.write('Hello this is a new file')



add_file('hello23')

    



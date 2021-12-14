import random
import os

p = 'F:\WallpapersHD'

def fileWalk(p):
    os.chdir(p)
    file_name = random.choice(os.listdir(p))
    print(file_name)
    print(type(file_name))

    if os.path.isfile(file_name):
        print("Check this out!")
        os.system(file_name)
    else:
        print('else clause hit')
        new_path = str(os.path.realpath(file_name))
        
        fileWalk(new_path)

fileWalk(p)
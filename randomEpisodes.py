import random
import os

p = 'G:\Try not to open\Cowboy.Bebop.2021.S01.COMPLETE.720p.NF.WEBRip.x264-GalaxyTV[TGx]'

os.chdir(p)
file_name = random.choice(os.listdir(p))
print(type(file_name))
print('Check this out')
os.system(file_name)
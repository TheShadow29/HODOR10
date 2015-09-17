import fnmatch
import os
list = []
for file in os.listdir("./Images/HeatBlast/"):
    if fnmatch.fnmatch(file, '*.png'):
        list.append(file)
hblist = sorted(list)
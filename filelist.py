import fnmatch
import os
list = []
for file in os.listdir("./Images/HeatBlast/"):
    if fnmatch.fnmatch(file, '*.png'):
        list.append(file)
hblist = sorted(list)

list1=[]
for file in os.listdir("./Images/Wildmutt/"):
    if fnmatch.fnmatch(file, '*.png'):
        list1.append(file)
wmlist = sorted(list1)
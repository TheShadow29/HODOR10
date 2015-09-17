import fnmatch
import os

list1=[]

for files in os.listdir("./Images/HeatBlast/"):
    if fnmatch.fnmatch(files, '*.png'):
        list1.append(files)
hblist = sorted(list1)

list1 = []

for files in os.listdir("./Images/Wildmutt/"):
    if fnmatch.fnmatch(files, '*.png'):
        list1.append(files)
wmlist = sorted(list1)

list1=[]

for files in os.listdir("./Images/Ghostfreak/"):
    if fnmatch.fnmatch(files, '*.png'):
        list1.append(files)
gflist = sorted(list1)

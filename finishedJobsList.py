import os
from datetime import datetime

#this program keeps track of projects that have a number in the end of their name
#creates a sorted list in a text file

path = os.path.abspath("D:\ZBrush2022.0.3\Prop_stock")

currDate = datetime.now()
day = currDate.day
month = currDate.month

fileList = os.listdir(path)
fileList = sorted(fileList)
fileList = [x for x in fileList if x[-1].isdigit()]
print(fileList)
with open(f"listOfTasks{day}_{month}.txt", "w") as file:
    for item in fileList:
        file.writelines(item + "\n")

file.close()


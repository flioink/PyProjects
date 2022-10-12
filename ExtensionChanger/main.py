import os
#import kivy
import datetime

#Window.size = (500, 200)

path = r"D:\My Pictures\LewisLarosa"


def renameFiles(x, lim):
    limit = lim
    filePath = os.path.abspath(x)
    fileCounter = 0
    dateEnd = 0
    fileList = os.listdir(filePath)

    for i, file in enumerate(fileList):
        nameLen = len(file)
        
        if file.endswith(".webp"):
            date = datetime.datetime.now()
            date.strftime("%M:%S.%f")
            print(dateEnd)
            changeExtension(file, filePath, dateEnd[7:])

        if nameLen-4 > limit and file.endswith("jpg"):
            fileCounter += 1
            date = datetime.datetime.now()
            dateEnd = date.strftime("%M:%S.%f")

            oldName = os.path.join(filePath, fileList[i])
            newName = os.path.join(filePath, f"{fileList[i][:limit]}_{dateEnd[7:]}_{str(fileCounter)}.jpg")
            print(dateEnd)
            os.rename(oldName, newName)
            print(oldName, "->", newName)


    print(fileCounter)

def changeExtension(file, filePath, counter):

    oldName = os.path.join(filePath, file)
    newName = os.path.join(filePath, f"{file[:-5]}_{str(counter)}.jpg")
    print(oldName, newName)
    os.rename(oldName, newName)
        



if __name__ == '__main__':

    # ExtensionChangerApp().run()
    renameFiles(path, 15)

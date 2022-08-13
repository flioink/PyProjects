from zipfile import ZipFile
import os
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class ZipExtractorScreen(GridLayout):
    def __init__(self, **kwargs):
        super(ZipExtractorScreen, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 5
        title = Label(text="Zip Extractor", font_size="32sp", color=(1, 0.8, 0), bold=True, size_hint=(1, 0.5))
        self.add_widget(title)
        instructions = Label(text="Enter source and destination folders: ", font_size="20sp", bold=True, size_hint=(1, 0.5))
        self.add_widget(instructions)
        self.sourceFolder = TextInput(text="Source folder path")
        self.destinationFolder = TextInput(text="Destination folder path")
        self.add_widget(self.sourceFolder)
        self.add_widget(self.destinationFolder)
        self.buttons = ButtonBox()
        self.add_widget(self.buttons)
        self.buttons.extract.bind(on_press=self.extractAllZipFiles)

    def extractAllZipFiles(self, button):
        path = self.sourceFolder.text
        dest = self.destinationFolder.text
        totalFilesCount = 0

        # check file path validity
        if os.path.isdir(os.path.abspath(path)):
            fileList = os.listdir(path)
            zipped = []
            fullPath = []

            # fill a list with the zip file names
            for file in fileList:
                if file.endswith(".zip"):
                    zipped.append(file)
            # construct a list of paths to each zip file
            for file in zipped:
                fullPathName = os.path.join(path, file)
                fullPath.append(fullPathName)
            # extract and count all the files
            for file in fullPath:
                with ZipFile(file, "r") as zipObj:
                    zipObj.extractall(path=dest)
                    totalFilesCount += len(zipObj.namelist())
        else:
            print("Invalid filepath")
        print(path, "+", dest)
        print(totalFilesCount)


class ButtonBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ButtonBox, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 1
        self.extract = Button(text="Extract!", color=(1, 0, 0))
        self.add_widget(self.extract)


class ZipExtractor(App):
    def build(self):
        return ZipExtractorScreen()


if __name__ == "__main__":

    ZipExtractor().run()



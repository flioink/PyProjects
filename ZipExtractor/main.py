import os
from zipfile import ZipFile
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
# A simple program with GUI that can take multiple zip files and extracts them in a given folder:)
# Main window size
Window.size = (400, 300)

class ZipExtractorScreen(GridLayout):
    def __init__(self, **kwargs):
        super(ZipExtractorScreen, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 7
        # Title label
        title = Label(text="Zip Extractor", font_size="30sp", color=(1, 0.8, 0), bold=True, size_hint=(1, 0.5))
        self.add_widget(title)
        # Instructions label
        instructions = Label(text="Extract multiple zip files at once.", font_size="20sp", color=(0, 0.8, 0), bold=True, size_hint=(1, 0.5))
        self.add_widget(instructions)
        # Source label
        srcLabel = Label(text="Enter the source folder: ", font_size="20sp", bold=True, size_hint=(1, 0.5))
        self.add_widget(srcLabel)
        self.sourceFolder = TextInput()
        # Destination label
        destLabel = Label(text="Enter the destination folder: ", font_size="20sp", bold=True, size_hint=(1, 0.5))
        self.destinationFolder = TextInput()
        self.add_widget(self.sourceFolder)
        self.add_widget(destLabel)
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
        self.extract = Button(text="Extract!", font_size="34sp", bold=True, color=(0, 0.8, 0))
        self.add_widget(self.extract)


class ZipExtractor(App):
    def build(self):
        return ZipExtractorScreen()


if __name__ == "__main__":

    ZipExtractor().run()



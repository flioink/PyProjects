from pytube import YouTube
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.window import Window
from functools import partial
import os
import pickle

destination = ""

try:
    with open("downloads_location", "rb") as f:
        destination = f.read()
except FileNotFoundError:
    if not os.path.exists("downloads_location"):
        with open("downloads_location", "wb") as f:
            f.write("D:\\Downloads\\YOUTUBE_DOWNLOADS")

except OSError:
    destination = "D:\\Downloads\\YOUTUBE_DOWNLOADS"


# width & height of window
Window.size = (500, 300)
Builder.load_file("DownloaderGUI.kv")

class DownloaderGUI(Widget):

    def __init__(self, **kwargs):
        super(DownloaderGUI, self).__init__(**kwargs)
        self.stream = None
        self.videObj = None
        self.warnText1 = "Must Have A Destination Folder!"

    def initDestination(self):
        self.ids.destinationBox = destination

    def downloader(self):
        self.background_color = (1, 0, 0, 1)
        try:
            videoURL = self.ids.urlBox.text
            downloadFolder = destination
            self.ids.destinationBox.text = destination

            self.videObj = YouTube(videoURL, on_progress_callback=partial(self.updateProgressBar, self))
            self.stream = self.videObj.streams.get_highest_resolution()
            self.ids.linkLabel.text = "Enter Youtube URL:"

            if os.path.exists(downloadFolder):

                self.ids.folderLabel.text = "Enter Download Folder:"
                self.stream.download(downloadFolder)
                self.ids.urlBox.text = ""

        except Exception as e:
            self.ids.folderLabel.text = "Invalid YouTube URL or download folder not found!"


    def clearURL(self):
        self.ids.urlBox.text = ""
        self.ids.bar.value = 0.0

    def clearDest(self):
        self.ids.destinationBox.text = ""

    def updateProgressBar(self, stream, chunk, fileHandle, remaining):
        highestResolutionStream = self.videObj.streams.get_highest_resolution()
        progress = (highestResolutionStream.filesize - remaining) / highestResolutionStream.filesize
        self.ids.bar.value = progress


class YouTubeDownloaderApp(App):
    def build(self):
        return DownloaderGUI()


if __name__ == '__main__':
    YouTubeDownloaderApp().run()










from pytube import YouTube
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.window import Window
import os
from pytube.cli import on_progress

# width & height of window
Window.size = (500, 300)
Builder.load_file("DownloaderGUI.kv")

class DownloaderGUI(Widget):

    def __init__(self, **kwargs):
        super(DownloaderGUI, self).__init__(**kwargs)
        self.stream = None
        self.videObj = None
        self.warnText1 = "Must Have A Destination Folder!"

    def downloader(self):

        videoURL = self.ids.urlBox.text
        downloadFolder = self.ids.destinationBox.text
        print(videoURL, downloadFolder)
        if videoURL != "":
            self.videObj = YouTube(videoURL, on_progress_callback=on_progress)
            self.stream = self.videObj.streams.get_highest_resolution()
            self.ids.linkLabel.text = "Enter Youtube URL:"
        else:
            self.ids.linkLabel.text = "No link provided, action cancelled!"

        if os.path.exists(downloadFolder) and videoURL != "":
            self.ids.folderLabel.text = "Enter Download Folder:"
            self.stream.download(downloadFolder)
            self.ids.bar.value = 1.0
            self.ids.urlBox.text = ""

        else:
            self.ids.folderLabel.text = "No folder provided, action cancelled!"

    def clearURL(self):
        self.ids.urlBox.text = ""
        self.ids.bar.value = 0.0

    def clearDest(self):
        self.ids.destinationBox.text = ""


class YouTubeDownloaderApp(App):
    def build(self):
        return DownloaderGUI()


if __name__ == '__main__':
    YouTubeDownloaderApp().run()










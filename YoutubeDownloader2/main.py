import validators
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from audio_extract import extract_audio


# check for previously saved default file
path = ""
try:
    with open("settings.txt", "r") as file:
        value = file.readline()
        if value != "":
            path = value
        else:
            path = os.path.abspath(r"C:\\")

except FileNotFoundError:
    path = os.path.abspath(r"C:\\")  # set C:\ as default if no file is present
    with open("settings.txt", "w") as file:
        file.writelines(path)

# print(path)


class YoutubeDownloader(ttk.Frame):
    def __init__(self, master_window, dest_path):
        super().__init__(master_window, padding=(20, 10))
        # self.iconbitmap("icon9.ico")
        self.pack(fill=BOTH, expand=YES)
        # form variables
        self.url = ttk.StringVar(value="")
        self.destination_folder = ttk.StringVar(value=dest_path)
        self.clip_name = ""
        # form header
        hdr_txt = "Enter the URL and the destination folder."
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)
        # entries
        self.create_form_entry("URL", self.url)
        self.create_form_entry("Destination Folder", self.destination_folder)
        # button box
        self.create_button_box()
        # meter
        self.create_meter()
        # path variable
        self.path = path
        # default bar value
        self.bar_value = 0
        # info label
        self.create_info_label()

        self.create_audio_box()

    # form entry setup
    def create_form_entry(self, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        label = ttk.Label(master=container, text=label.title(), width=10)
        label.pack(side=LEFT)

        entry = ttk.Entry(master=container, textvariable=variable)
        entry.pack(side=LEFT, padx=5, fill=X, expand=YES)
        entry.bind("<Button-1>", self.clear_meter)

    # button box setup
    def create_button_box(self):
        self.container_1 = ttk.Frame(self)
        self.container_1.pack(fill=X, expand=YES, pady=(15, 10))

        submit_btn = ttk.Button(
            master=self.container_1,
            text="Get!",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6)

        submit_btn.pack(side=RIGHT, padx=5)
        submit_btn.focus_set()

        cancel_btn = ttk.Button(
            master=self.container_1,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6)
        cancel_btn.pack(side=RIGHT, padx=5)

        # Set default destination for files with check button
        self.check = ttk.Radiobutton(master=self.container_1, command=self.on_radio_btn)
        self.check.pack(side=RIGHT, padx=5)

        self.msg = ttk.Label(master=self.container_1, text="Set current destination as default")
        self.msg.pack(side=LEFT, padx=5)

    def create_audio_box(self):
        self.container_2 = ttk.Frame(self)
        self.container_2.pack(fill=X, expand=YES, pady=(15, 10))

        submit_btn = ttk.Button(
            master=self.container_2,
            text="To MP3",
            command=self.convert_to_audio,
            bootstyle=SUCCESS,
            width=10)

        submit_btn.pack(side=RIGHT, padx=5)


        audio_msg = ttk.Label(master=self.container_2, text="Convert the last downloaded file to mp3")
        audio_msg.pack(side=LEFT, padx=5)

    # info label
    def create_info_label(self):
        self.info_label = ttk.Label(master=self, text="Download status:")
        self.info_label.pack()

    # pressing the download
    def on_submit(self):
        self.info_label.config(text="Downloading, please wait...")
        self.download()

        print("Link: ", self.url.get())
        print("Dest: ", self.path)
        self.info_label.configure(text="Download status: Complete!")
        self.url.set(value="")

    # check if the link works
    def validate_url(self, url):
        return validators.url(self.url.get())

    # DOWNLOAD
    def download(self):

        if self.validate_url(self.url.get()):

            try:  # check if video can be downloaded

                yt = YouTube(self.url.get(),
                             on_progress_callback=self.update_progress_bar,
                             on_complete_callback=self.on_complete_callback)

                self.stream = yt.streams.get_highest_resolution()
                self.clip_name = yt.title + ".mp4"
                print(self.clip_name)
                self.stream.download(self.path)

            except VideoUnavailable:
                print("The video is either unavailable or requires a login.")
        else:
            self.url.set(value="Invalid Link!")

    # create the progress bar
    def create_meter(self):
        self.progress_bar = ttk.Progressbar(
            self,
            bootstyle="danger-striped",
            maximum=100,
            length=350,
            mode="determinate")

        # danger colored striped progressbar style

        self.progress_bar.pack(pady=10)

    def check_entry(self):
        text = self.destination_folder.get()
        if text.strip():  # Check if the text is not empty (after stripping whitespace)
            return True
        else:
            return False

    def on_radio_btn(self):
        if self.check_entry() and os.path.exists(self.path):
            default_folder = self.destination_folder.get()
            self.destination_folder.set(value=default_folder)

            with open("settings.txt", "w") as f:
                f.write(default_folder)
            print(default_folder)

            self.msg.config(text="Set!")
            # self.after(500, self.default_msg.config(text="Set current destination as default"))
            # self.check.config(value=1)
        else:
            self.msg.config(text="Field is empty!")

            print("Empty Field")

    # progress bar gauge
    def update_progress_bar(self, *args):
        pass
        # self.info_label.config(text="Downloading, please wait...")
        # size = self.stream.filesize - bytes_remaining
        # print("size: ", size)
        # percent = 0
        # while percent <= 100:
        #     progress = percent
        #     percent = self.percent(bytes_remaining, size)
        #
        #     print(progress)

    def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

    # put the progress bar at 100 when download is complete
    def on_complete_callback(self, *args):
        self.progress_bar["value"] = 100

    # clear the progress bar when the entry is clicked
    def clear_meter(self, event):
        self.progress_bar["value"] = 0
        self.info_label.configure(text="Download status:")

    def convert_to_audio(self):
        print("Converting")
        if self.clip_name != "":
            audio_name = self.clip_name.split(".")[0]
            extract_audio(os.path.join(path, self.clip_name), os.path.join(path, audio_name))
            print(os.path.join(path, self.clip_name + "123"))
            self.clip_name = ""
        else:
            print("clip must be downloaded first")

    def on_cancel(self):
        self.quit()


if __name__ == "__main__":
    vid_file = os.path.join(path, "The Force Theme.mp4")
    output = os.path.join(path, "The Force Theme.mp4")
    print(vid_file, output)
    app = ttk.Window("Youtube Video Downloader", "superhero", resizable=(False, False))
    YoutubeDownloader(app, path)
    app.mainloop()

import os
import random

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel,\
                             QListWidget, QFileDialog, QSlider, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtMultimedia import  QMediaPlayer, QAudioOutput

import json

# app class
class AudioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.volume = 100
        self.current_song_index = None
        self.settings()
        self.init_UI()
        self.event_handler()
        self.folder_path = None
        self.playlist = None
        self.load_playlist()
        self.paused = False
        self.shuffle = False


    # settings
    def settings(self):
        self.setWindowTitle("Small Audio Player")
        self.setGeometry(800, 500, 800, 600)
    # UI
    def init_UI(self):
        self.title = QLabel("Small Audio Player")
        self.title.setObjectName("title")
        self.file_list = QListWidget()
        self.btn_opener = QPushButton("Choose a folder")

        # Play Buttons
        self.btn_play = QPushButton("Play")
        self.btn_pause = QPushButton("Pause")
        self.btn_reset = QPushButton("Reset")
        self.btn_shuffle = QPushButton("🔀: OFF")
        #self.btn_shuffle.setStyleSheet("font-size: 10px;")
        self.playback_buttons_layout = QHBoxLayout()
        self.btn_play.setFixedSize(100, 80)
        self.btn_pause.setFixedSize(100, 80)
        self.btn_reset.setFixedSize(100, 80)
        self.btn_shuffle.setFixedSize(100, 80)
        self.playback_buttons_layout.addWidget(self.btn_play)
        self.playback_buttons_layout.addWidget(self.btn_pause)
        self.playback_buttons_layout.addWidget(self.btn_reset)
        self.playback_buttons_layout.addWidget(self.btn_shuffle)
        self.playback_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.playback_buttons_layout.setSpacing(5)  # Reduce space between buttons
        self.playback_buttons_layout.setContentsMargins(0, 0, 0, 0)  # Remove extra margins

        self.btn_save = QPushButton("Save Playlist")
        # disable buttons on start
        self.btn_pause.setDisabled(True)

        self.btn_reset.setDisabled(True)

        # speed label
        self.slider_text = QLabel("Speed: 100%")
        self.slider_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # speed slider
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(50)
        self.speed_slider.setMaximum(150)
        self.speed_slider.setValue(100)


        # progress slider
        self.progress_bar = QSlider(Qt.Orientation.Horizontal)
        self.progress_bar.setRange(0, 100)

        # enable interactive progress bar
        self.progress_bar.setEnabled(True)
        self.progress_bar.setTracking(True)


        # volume slider
        self.volume_text = QLabel(f"Volume: {self.volume}%")
        self.volume_bar = QSlider(Qt.Orientation.Horizontal)
        self.volume_bar.setRange(0, 100)

        self.volume_bar.setValue(self.volume)


        # slider layout
        progress_bar_layout = QVBoxLayout()
        adjust_settings_layout = QHBoxLayout()

        adjust_settings_layout.addWidget(self.slider_text)
        adjust_settings_layout.addWidget(self.speed_slider)
        adjust_settings_layout.addWidget(self.volume_text)
        adjust_settings_layout.addWidget(self.volume_bar)

        progress_bar_layout.addWidget(self.progress_bar)

        # layout
        self.master = QVBoxLayout()
        row = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()
        col2.setAlignment(Qt.AlignmentFlag.AlignTop)

        # load the layout
        self.master.addWidget(self.title)
        self.master.addLayout(progress_bar_layout)
        self.master.addLayout(adjust_settings_layout)

        col1.addWidget(self.file_list)
        col2.addWidget(self.btn_opener)
        col2.addLayout(self.playback_buttons_layout)

        col2.addWidget(self.btn_save)

        row.addLayout(col1, 4)
        row.addLayout(col2, 2)

        self.master.addLayout(row)
        self.setLayout(self.master)

        # special audio classes
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        self.media_player.setAudioOutput(self.audio_output)

        self.media_player.mediaStatusChanged.connect(self.play_next_song)

        self.style()

    # Connect events
    def event_handler(self):
        self.speed_slider.valueChanged.connect(self.update_slider)
        self.btn_opener.clicked.connect(self.open_file)
        self.btn_play.clicked.connect(self.play_audio)
        self.btn_pause.clicked.connect(self.pause_audio)
        self.btn_reset.clicked.connect(self.reset_audio)
        self.btn_shuffle.clicked.connect(self.toggle_shuffle)
        self.btn_save.clicked.connect(self.save_playlist)
        # progress bar
        self.media_player.positionChanged.connect(self.update_progress_bar)
        self.media_player.durationChanged.connect(self.set_slider_range)
        self.progress_bar.sliderReleased.connect(self.seek_audio)
        self.speed_slider.sliderMoved.connect(self.update_speed)
        self.file_list.itemDoubleClicked.connect(self.play_new_song)
        self.volume_bar.sliderMoved.connect(self.volume_control)

    def update_slider(self):
        speed = self.speed_slider.value()
        self.slider_text.setText(f"Speed: {speed}%")

    def open_file(self):
        path = QFileDialog.getExistingDirectory(self, "Select Folder")

        if path:
            self.file_list.clear()
            self.folder_path = path
            self.playlist = []

            for filename in os.listdir(path):
                if filename.endswith(".mp3"):
                    full_path = os.path.join(path, filename)
                    self.playlist.append(full_path)
                    self.file_list.addItem(filename)

        else:
            file, _ = QFileDialog.getOpenFileName(self, "Select File", filter="Audio Files (*.mp3)")
            if file:
                self.file_list.clear()
                self.playlist = [file]
                self.file_list.addItem(os.path.basename(file))


    def play_audio(self):
        self.progress_bar.setEnabled(True)

        if self.paused and self.file_list.currentRow() == self.current_song_index:
            self.media_player.play()
            self.paused = False

            self.btn_pause.setEnabled(True)
            self.btn_reset.setEnabled(True)
            self.btn_play.setDisabled(True)

        else:
            self.play_new_song()

    def play_new_song(self):

        self.current_song_index = self.file_list.currentRow()

        if self.current_song_index >= 0:
            file_path = self.playlist[self.current_song_index]
            file_url = QUrl.fromLocalFile(file_path)
            self.media_player.setSource(file_url)
            self.media_player.setPlaybackRate(self.speed_slider.value() / 100.0)
            self.media_player.play()
            self.paused = False

            self.btn_pause.setEnabled(True)
            self.btn_play.setDisabled(True)
            self.progress_bar.setEnabled(True)

    def play_next_song(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            if self.shuffle:
                self.current_song_index = random.randint(0, len(self.playlist) - 1)

            else:
                self.current_song_index = self.file_list.currentRow() + 1

            if self.current_song_index < len(self.playlist):
                self.file_list.setCurrentRow(self.current_song_index)  # Keep UI in sync
                self.play_audio()
            else:
                self.media_player.stop()



    def pause_audio(self):
        if not self.paused:
            self.media_player.pause()
            self.btn_pause.setDisabled(True)
            self.btn_play.setEnabled(True)
            self.paused = True


    def reset_audio(self):
        if self.media_player.isPlaying():
            self.media_player.stop()

        self.media_player.setPosition(0)
        self.media_player.setPlaybackRate(self.speed_slider.value() / 100.0)
        self.media_player.play()

        self.btn_pause.setEnabled(True)
        self.btn_reset.setDisabled(True)
        self.btn_play.setDisabled(True)
        self.paused = False

        QTimer.singleShot(100, lambda: self.btn_reset.setEnabled(True))

    def style(self):
        self.setStyleSheet(
            """
            QWidget{
                background-color: #F9DBBA;
                
            }
            
            QPushButton {
                background-color: #5BB9C2;
                padding: 15px;  /* Increase padding for bigger buttons */
                border-radius: 12px; /* More rounded corners */
                color: white;
                font-weight: bold;
                font-size: 16px; /* Bigger text */
                margin: 5px; /* Add spacing between buttons */
                border: 2px solid #1A4870;
                transition: 0.2s;
            }

            QPushButton:hover {
                background-color: #1A4870;
                color: #F9DBBA;
                border: 2px solid #5BB9C2;
            }
            
            QLabel{
                color: #333;
            
            }
            
            #title{
                font-family: Papyrus;
                font-size: 40px;
            }
            
            QSlider{
                margin-right: 15px;
            }
            
            QListWidget{
                color: #333;
            }
            
            QListWidget::item {
                padding: 4px;
            }         
            
            QListWidget {
                background-color: #E5E5E5; /* Light gray for contrast */
                border: 2px solid #5BB9C2; /* Adds a subtle border */
                color: #333; 
            }

            QListWidget::item:selected {
                background: #1A4870;
                color: #5BB9C2;
                font-weight: bold;
            }
            
            QSlider::groove:horizontal {
                height: 10px;
                background: #ddd;
                border-radius: 5px;
            }
            
            QSlider::handle:horizontal {
            background: #5BB9C2;
            width: 14px;
            height: 14px;
            border-radius: 7px;  /* This makes it circular */
            }

            
            QSlider::handle:horizontal:hover {
            background: #FF5733;
            width: 16px;
            height: 16px;
            border-radius: 8px;  /* Stays circular even when hovered */
            }
            
            QSlider::tick-mark {
                background: black;
                width: 2px;
                height: 10px;
            }   
                                 
            """
        )


    def update_progress_bar(self, position):
        if not self.progress_bar.isSliderDown():
            self.progress_bar.setValue(position)

    def set_slider_range(self, duration):
        self.progress_bar.setRange(0, duration)


    def load_playlist(self):
        if os.path.exists("playlist.json"):
            with open("playlist.json", "r") as file:
                self.playlist = json.load(file)

            self.file_list.clear()

            for idx, file in enumerate(self.playlist, start=1):
                song_name = os.path.basename(file)
                self.file_list.addItem(f"{idx}. {song_name}")
                idx += 1

    def save_playlist(self):
        if self.playlist:
            json_object = json.dumps(self.playlist, indent=4)

            # Writing to sample.json
            with open("playlist.json", "w") as outfile:
                outfile.write(json_object)
                QMessageBox.information(self, "Saving", "Saved current playlist.")

    def seek_audio(self):
        position = self.progress_bar.value()
        self.media_player.setPosition(position)

    def update_speed(self, value):

        self.media_player.setPlaybackRate(value / 100.0)
        self.slider_text.setText(f"Speed: {value}%")

    def volume_control(self, value):
        self.volume = value
        self.volume_text.setText(f"Volume: {self.volume}%")
        self.audio_output.setVolume(value / 100.0)

    def toggle_shuffle (self):
        if self.shuffle:
            self.shuffle = False
        else:
            self.shuffle = True

        self.btn_shuffle.setText("🔀: ON" if self.shuffle else "🔀: OFF")


if __name__ == "__main__":
    app = QApplication([])
    main = AudioApp()
    main.show()
    app.exec()
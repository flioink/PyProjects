from pytube import YouTube

def YtDownload():
    downloadFolder = "D:\\Downloads"
    videoURL = "https://www.youtube.com/watch?v=mQppXRN841w&list=LL&index=3"
    videObj = YouTube(videoURL)
    stream = videObj.streams.get_highest_resolution()
    stream.download(downloadFolder)
    
    
YtDownload()
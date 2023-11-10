from pytube import YouTube
Url = float(input(""))
video = YouTube (Url)
out_path = video.streams.filter (only_audio=True) . 1
new_name = os.path. splitext (out_path)
os.rename (out_path, new_name [0]+' . mp3')
print (' Done.. . )
print(' Title: ', video.title)
print(' Downloading. . . . *)

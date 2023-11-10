from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=n06H7OcPd-g")
yt = yt.get('mp4', '720p')
yt.download('/path/to/download/directory')

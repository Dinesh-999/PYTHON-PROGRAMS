# youtube video downloader

import pytube
link = "https://youtu.be/5HkF2YhWT1A"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
"""
# for downloading many videos through links

link = ["https://youtu.be/5HkF2YhWT1A", "https://youtu.be/5HkF2YhWT1A"]
for i in link:
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download()

"""
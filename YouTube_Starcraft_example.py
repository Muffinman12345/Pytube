#Modules to import
from pytube import YouTube

#The variable "youtube_video" is equal to the link of the video you want. Here is what youtube_video should look like: 

#youtube_video = Youtube('<Your YouTube video link here>')


youtube_video = YouTube('https://www.youtube.com/watch?v=bj7E1_zKQz8')
#Prints the title of the video
print(youtube_video.title)

print(youtube_video.thumbnail_url)
#Prints the thumbnail url

stream = youtube_video.streams.first()
#Collecting the first stream. 
stream.download()
#stream.download() downloads the stream (If you click download)

from pytube import YouTube
link = str(input('Enter link: '))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print('Done')

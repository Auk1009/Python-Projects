from pytube import YouTube
def downloader(url):
    try:
        yt = YouTube(url)

        print(f'downloading..{yt.title}')

        video_stream = yt.streams.get_highest_resolution()

        video_stream.download()

        print('download complete')
    except Exception as e:
        print(e)

url = input('Type the url from youtube')
downloader(url)
    

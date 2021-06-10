import youtube_dl


# Получение списка всех качеств у видео и передача их пользователю на выбор
def take_format_video(download_url):
    print(download_url)
    videos_info = youtube_dl.YoutubeDL().extract_info(download_url, download=False)

    formats = videos_info['formats']

    videos_quality = []

    for el in videos_info['formats']:
        if el['quality'] > 3:
            videos_quality.append(el['format_note'])

    return videos_quality


# Загрузка видео по ссылке и запрашиваемому качеству
def take_download_link(download_url, video_format):
    ydl_opts = {
        'format': video_format+'bestaudio/best',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        vid = ydl.extract_info(download_url, download=False)
        print(vid['url'])
        return vid['url']

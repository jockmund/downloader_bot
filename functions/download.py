import youtube_dl


# Загрузка видео по ссылке и запрашиваемому качеству
def take_download_link(download_url):
    ydl_opts = {
        'format': f"bestvideo/best+bestaudio/best",
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        vid = ydl.extract_info(download_url, download=False)
        return vid['url']

import youtube_dl as ytd

print('Conversos de videos a mp3.')


def proceso():
    url = input('Url de video o lista de reproduccion: ')
    ydl_opts = {
        'outtmpl': 'D:\Musica\%(title)s-%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # 'flac',
            'preferredquality': '320',
        }],
    }
    try:
        with ytd.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        print('No se a podido completar la operacion.')
        return salir()


def salir():
    question = input('Cerrar la app ? (y/n): ')
    if question == 'y':
        quit()
    elif question == 'n':
        return proceso()
    else:
        return salir()


proceso()
salir()

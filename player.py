import yt_dlp
import vlc
import time
import urllib.parse

ydl_opts = {"quiet":True}

def getStreamUrl(url):
	print("Buscando dados do Vídeo")
	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			info = ydl.extract_info(url, download=False)
			formats = info['formats']

			for i,format in enumerate(formats):
				note = None
					
				if 'format_note' in format:
					note = str(format['format_note'])
				
				if note == 'Default':
					print("Ok!")
					return {'title': info['title'], 'duration': info['duration'], 'url': format['url']}
	except:
		print("Erro!")
		return None

def playYTAudio(url, requester):
	data = getStreamUrl(url)
	speakSongInfo(data, requester)
	print("Iniciando Vídeo")
	player = vlc.MediaPlayer(data['url'])
	player.play()
	time.sleep(1.5)
	time.sleep(data['duration'])

def speakSongInfo(songInfo, requester):
	sentence = "Tocando {}, pedido de {}".format(songInfo['title'], requester)
	print(sentence)
	player = vlc.MediaPlayer("http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={}&tl=pt".format(urllib.parse.quote(sentence), safe=''))
	player.play()
	time.sleep(1.5)
	duration = player.get_length() / 1000
	time.sleep(duration + 3)


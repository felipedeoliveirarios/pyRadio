import yt_dlp
import vlc
import time
import urllib.parse
import os
from queue import Queue
from threading import Thread

ydl_opts = {"quiet":True}

class Player(Thread):

	def getStreamUrl(self, url):
	
		if self.debug:
			print("PLAYER THREAD >> Buscando dados do Vídeo...")
		
		if True:
			with yt_dlp.YoutubeDL(ydl_opts) as ydl:
				info = ydl.extract_info(url, download=False)
				formats = info['formats']

				for format in formats:
					note = None
						
					if 'format_note' in format:
						note = str(format['format_note'])
					
					if note == 'Default':
						if self.debug:
							print("PLAYER >> Ok!")
						
						return {'title': info['title'], 'duration': info['duration'], 'url': format['url']}
		

	def playYTAudio(self, url, requester):
		data = self.getStreamUrl(url)
		
		if not data:
			return
			
		sentence = "Tocando {} a pedido de {}".format(data['title'], requester)
		self.speakSentence(sentence)
		
		if self.debug:
			print("PLAYER THREAD >> Iniciando Vídeo")
		
		player = vlc.MediaPlayer(data['url'])
		player.play()
		time.sleep(2)
		time.sleep(data['duration'])
		
		if self.debug:
			print("PLAYER THREAD >> Encerrando Vídeo")

	def speakSentence(self, sentence):
	
		if self.debug:
			print("PLAYER THREAD >> " + sentence)
		
		player = vlc.MediaPlayer("http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={}&tl=pt".format(urllib.parse.quote(sentence), safe=''))
		player.play()
		time.sleep(2)
		duration = player.get_length() / 1000
		time.sleep(duration + 5)
	
	def run(self):
		self.playYTAudio(self.request.url, self.request.requester)
		self.callback()
	
	def __init__(self, request, callback = lambda: None, debug = False):
		Thread.__init__(self)
		self.request = request
		self.callback = callback
		self.debug = debug
		os.environ["VLC_VERBOSE"] = str("-1")


from queue import Queue
from player import Player
from threading import Thread
import time

class Controller(Thread):
	
	def __init__(self):
		self.queue = Queue()
	
	def enqueue_request(self, request):
		if self.debug:
			print("PLAYER CONTROLLER THREAD >> Adicionando pedido de {} à fila".format(request.requester))
			
		self.queue.put(request)
	
	def play_next_song(self):		
		if not self.currently_playing:
			
			if self.debug:
				print("PLAYER CONTROLLER THREAD >> Tocando próximo pedido")
			
			self.currently_playing = True
			request = self.queue.get()		
			player = Player(request, self.on_finish_playing, self.debug)
			player.start()
	
	def on_finish_playing(self):
	
		if self.debug:
			print("PLAYER CONTROLLER THREAD >> Pedido finalizado")
		
		if self.currently_playing:
			self.currently_playing = False
	
	def run(self):
		while True:
			if not self.queue.empty():
				if not self.currently_playing:
					self.play_next_song()
				else:
					time.sleep(1)
			else:
				time.sleep(1)
	
	def __init__(self, queue, debug = False):
		Thread.__init__(self)
		self.queue = queue
		self.debug = debug
		self.currently_playing = False
		
	

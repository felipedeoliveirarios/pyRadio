from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from queue import Queue
from controller import Controller
from radio_request import Request

queue = Queue()
controller = Controller(queue, True)
controller.start()
app = Flask(__name__)
api = Api(app)

class Radio(Resource):
	controller = None

	def post(self):
		url = request.json['url']
		requester = request.json['requester']
		request_obj = Request(url, requester)
		
		print("RESOURCE THREAD INSTANCE >> Received post with data {}".format(request.json))
		
		self.controller.queue.put(request_obj)
		return
	
	def __init__(self):
		print("RESOURCE THREAD INSTANCE >> Initializing resource instance...")
		
		self.queue = queue
		self.controller = controller
		
		print("RESOURCE THREAD INSTANCE >> Done!")

api.add_resource(Radio, '/radio')

if __name__ == '__main__':
    app.run()

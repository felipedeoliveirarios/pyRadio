from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import player

app = Flask(__name__)
api = Api(app)

class Radio(Resource):
	def post(self):
		url = request.json['url']
		requester = request.json['requester']
		
		player.playYTAudio(url, requester)
		return

api.add_resource(Radio, '/radio')

if __name__ == '__main__':
    app.run()

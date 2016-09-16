import os, sys
from flask import Flask, render_template, flash, url_for, g, session, request, \
	redirect, send_from_directory, abort

import logging

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def hello():
	return render_template('home.html', message="Hello World!")


if __name__ == '__main__':
	# start server
	import SimpleHTTPServer
	import SocketServer

	PORT = 5000
	HOST = ""
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer((HOST, PORT), Handler)

	print "serving at port", PORT
	httpd.serve_forever()
	quit()
	
	#app.run()
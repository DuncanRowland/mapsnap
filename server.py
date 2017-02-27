#!/usr/bin/env python

from subprocess import check_output
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
import re

class requestHandler(tornado.web.RequestHandler):
   def get(self):
      species = self.get_argument('species',default="")
      species = re.sub(r'[^a-zA-Z ]', '', species) #sanitise
      ID = check_output(['/bin/bash','render.sh', species]).rstrip()
      filename = 'tmp/map.'+ID+'.png'
      self.set_header("Content-type",  "image/png")
      with open(filename) as f: 
         data = f.read()
         self.write(data)
      os.remove(filename)

application = tornado.web.Application([
   (r'/', requestHandler),
])

if __name__ == "__main__":
   http_server = tornado.httpserver.HTTPServer(application)
   http_server.listen(8080)
   loop=tornado.ioloop.IOLoop.instance()
loop.start()

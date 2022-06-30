from flask import Flask, redirect
from threading import Thread
from speakIU import shards
from asyncio.tasks import sleep
app = Flask('')

@app.route('/')
def hello():
  return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)

@app.route('/api')
def home():
  run='true'
  shard=shards
  return f"""{{"run":{run}}}"""

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
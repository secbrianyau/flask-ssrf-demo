from flask import *
import requests, random

app = Flask(__name__)

@app.route('/')
def home():
  random_image_url = [ "https://images.pngnice.com/download/2007/Coffin-Dance-Meme-PNG-Transparent-Image.png",
                       "https://cdn.dribbble.com/users/312139/screenshots/11186286/coffin_dance_animacijai_no_audio.png",
                       "https://i.pinimg.com/originals/45/44/ea/4544eafc95442d16e1a7cd5da9a0b60d.png",
                       "https://i.redd.it/0u6pv3t0ed471.png"
                     ]
  url = request.args.get('r', '')
  if url:
    return (requests.get(url).text)
  return Response(requests.get(random.choice(random_image_url)), mimetype="image/png")

@app.route('/log')
def log():
  with open('web.log', 'r') as f:
    return Response(f.read(), mimetype="text/plain")

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

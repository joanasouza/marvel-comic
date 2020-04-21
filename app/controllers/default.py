from app import app
from app import auth_marvel as auth
from flask import jsonify
import requests

auth_hash = auth.generate_hash()
api_url = auth.generate_url(auth_hash)

@app.route("/")
def index():
    response = requests.get(api_url)
    
    return response.json()

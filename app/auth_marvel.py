import requests
import hashlib
import time
import json
from app import config

time_stamp = str(time.time())

def generate_hash():
    time_stamp_byte = bytes(time_stamp, 'utf-8')
    m = hashlib.md5()
    m.update(time_stamp_byte)
    m.update(b"fa0a8e041508ac17588546287534cd7242a1ced1") 
    m.update(b"f4554c85607601d49751d47f4f9ca606") 
    api_hash = m.hexdigest()

    return api_hash

def generate_url(api_hash):
    base_url = "https://gateway.marvel.com"  
    query = "/v1/public/stories/" + config.story_id + "?"
    query_url = base_url + query +"ts=" + time_stamp+ "&apikey=" + config.public_key + "&hash=" + api_hash
    
    return query_url

    
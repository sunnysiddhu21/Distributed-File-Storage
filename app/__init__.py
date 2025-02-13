from flask import Flask
from redis import Redis

app = Flask(__name__)
app.config.from_object('app.config.Config')
redis = Redis(host='redis', port=6379)

from app import routes

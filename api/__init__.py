from flask import Flask

print("Start initializing the server...")
app = Flask(__name__)

print("Initializing config...")
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

print("Importing controllers...")
from api.controllers import *
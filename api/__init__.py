from flask import Flask

print("Start initializing the server...")
app = Flask(__name__)

print("Initializing config...")
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
app.config["SECRET_KEY"] = "secret-key-goes-here"

print("Importing controllers...")
from api.controllers import *

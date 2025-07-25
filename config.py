import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv() # automatically loads .flaskenv file

app = Flask(__name__) 
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
from flask import Flask, Blueprint
from flask_cors import CORS
import json
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:doctorwho3210@172.17.0.1:5432", echo=True, future=True)
conn = engine.connect()

app = Flask(__name__)
CORS(app)

api = Blueprint('api', __name__)

@api.route('/')
def main_route():
    return 'Faaala LEK'

@api.route('/user', methods=['GET'])
def userdata():
    return json.dumps({
      'name': 'Matheus',
      'age': '23',
      'gender': 'Autobot'
    })

app.register_blueprint(api, url_prefix='/api')
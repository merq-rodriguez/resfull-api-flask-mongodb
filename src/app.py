from flask import Flask, request
from flask_cors import CORS
from routes import routes_api
from common import setting

port = setting.config['port-api']

#Init server
app = Flask(__name__)

# Set routes
routes_api(app)

# Enable cors
CORS(app)

if __name__ == '__main__':
  app.run(debug=True, port=port)

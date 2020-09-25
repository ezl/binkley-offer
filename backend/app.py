from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from controllers.routes import initialize_routes
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/dev_redfin'
}

initialize_db(app)
initialize_routes(api)

app.run()
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db'
# turn off the flask sql alchemy modification tracker (it does not turn off the sql alchemy modification tracker)
# know when an object had changed but not been saved in the db
# this comes from the extension flask sql alchemy
# we do this because sqlalchemy has its own modification tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'pepe'
db = SQLAlchemy(app)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

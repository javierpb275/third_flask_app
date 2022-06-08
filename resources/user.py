from flask_restful import Resource, reqparse
import sqlite3
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        new_user = (data['username'], data['password'])
        cursor.execute(query, new_user)
        connection.commit()
        connection.close()

        return {"message": "User created successfully"}, 201

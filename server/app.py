#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import User, Recipe

class Signup(Resource):
    def post(self):

        request_json = request.get_json()

        username = request_json.get('username')
        password = request_json.get('password')
        image_url = request_json.get('image_url')
        bio = request_json.get('bio')
        # # grab parameters from form
        # username = request.form['username'],
        # password = request.form['password'],
        # image_url = request.form['image_url'],
        # bio = request.form['bio']

        print('\n\n\n ====================== LOG LOG LOG LOG \n\n')
        print(type(username))

        # create user with visible parameters
        new_user = User(
            username=username,
            image_url=image_url,
            bio=bio
        )

        # encrypt password
        new_user.password_hash = password

        # try / except to add to database
        try:
            db.session.add(new_user)
            db.session.commit()

            # update user_id for session
            session['user_id'] = new_user.id

            return new_user.to_dict(), 201
        except IntegrityError:
            return {'error': 'Unprocessable Entity'}, 422
        

class CheckSession(Resource):
    pass

class Login(Resource):
    pass

class Logout(Resource):
    pass

class RecipeIndex(Resource):
    pass

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')

# @app.errorhandler(UnprocessableEntity)
# def handle_unprocessable_entity(e):

#     return {'Unprocessable Entity': 'Entity cannot be processed'}, 422

# app.register_error_handler(422, handle_unprocessable_entity)

if __name__ == '__main__':
    app.run(port=5555, debug=True)



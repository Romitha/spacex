from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, test_user, find_user, verification_email, \
    update_user
from app.main.util.decorator import token_required, admin_token_required
from ..util.decorator import token_required, admin_token_required
from flask_cors import cross_origin

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=False)
    @cross_origin()
    def post(self):
        print('Creates a new User')
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

    @api.response(201, 'User successfully updated.')
    @api.doc('Update a User')
    @token_required
    @api.expect(_user, validate=False)
    @cross_origin()
    def put(self):
        """Update User"""

        data = request.json
        auth_header = request.headers.get('Authorization')
        return update_user(data=data, auth_header=auth_header)


@api.route('/find-user')
class FindUser(Resource):
    @api.doc('Find registered user')
    @token_required
    @cross_origin()
    def get(self):
        auth_header = request.headers.get('Authorization')
        return find_user(auth_header)


@api.route('/list_of_users')
class ListOfUsers(Resource):
    @api.doc('Find registered users')
    @token_required
    @cross_origin()
    def get(self):
        auth_header = request.headers.get('Authorization')
        return get_all_users(auth_header)


@api.route('/confirm/<token>')
@api.param('token', 'The gnerated token when register')
class VerifyUser(Resource):
    @api.doc('Verify newly registered user')
    @cross_origin()
    def get(self, token):
        return verification_email(token)

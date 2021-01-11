from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto
from ..util.decorator import token_required, admin_token_required
from flask_cors import cross_origin

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """

    @api.doc('user login')
    @api.expect(user_auth, validate=False)
    @cross_origin()
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """

    @api.doc('logout a user')
    @cross_origin()
    @token_required
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)


@api.route('/get-login-user')
class GetLoginUser(Resource):
    """
    Get Logged in User
    """

    @api.doc('Logged in user')
    @cross_origin()
    @token_required
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.get_logged_in_user(data=auth_header)


@api.route('/token_validation')
class TokenValidation(Resource):
    """
    Token Validation
    """

    @api.doc('Token Validation')
    @cross_origin()
    @token_required
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        print('token_validation')
        return Auth.token_validation(data=auth_header)

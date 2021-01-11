from app.main.model.user import User
from ..service.blacklist_service import save_token
from app.main import db
import pyotp
import base64


class Auth:

    @staticmethod
    def login_user(data):
        print(data)
        try:

            user = User.query.filter_by(email=data.get('email')).first()

            if user and user.check_password(data.get('password')):
                if user.is_tfa:
                    if data.get('code') is None:
                        print('need two factor authentication')
                        response_object = {
                            'link': Auth.create_google_authenticator(),
                            'status': 'fail',
                            'message': 'Need to send 2FA code'
                        }
                        return response_object, 200
                    else:

                        totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
                        print("Current OTP:", totp.now())

                        if totp.now() == data.get('code'):
                            auth_token = user.encode_auth_token(user.id)
                            if auth_token:
                                response_object = {
                                    'status': 'success',
                                    'message': 'Successfully logged in.',
                                    'Authorization': auth_token.decode()
                                }
                                return response_object, 200

                        else:
                            response_object = {
                                'status': 'fail',
                                'message': 'OTP code does not match.'
                            }
                            return response_object, 401
                else:
                    if user.is_active:
                        auth_token = user.encode_auth_token(user.id)
                        if auth_token:
                            response_object = {
                                'status': 'success',
                                'message': 'Successfully logged in.',
                                'Authorization': auth_token.decode()
                            }
                            return response_object, 200
                    else:
                        response_object = {
                            'status': 'fail',
                            'message': 'Verify your email and click to activate account'
                        }
                        return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        auth_token = data
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(data):
        # get the auth token
        auth_token = data
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'is_active': user.is_active,
                        'is_tfa': user.is_tfa,
                        'is_admin': user.is_admin,
                        'created_at': str(user.created_at)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

    @staticmethod
    def token_validation(data):
        # get the auth token
        auth_token = data
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                print('not isinstance')
                response_object = {
                    'status': 'success',
                    'message': resp
                }
                return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

    @staticmethod
    def create_google_authenticator():
        str = "JanithRomithaAlgewatta"
        secret = base64.b64encode(bytes(str, 'utf-8'))
        otp_url = pyotp.totp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri("janith2011@google.com",
                                                                       issuer_name="XchangeApp")
        main_url = "https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl="
        return main_url + otp_url

from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.Integer(required=False, description='User table primary_key'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'is_active': fields.Boolean(description='is_active'),
        'is_tfa': fields.Boolean(description='is_tfa'),
        'is_admin': fields.String(description='is_admin')
    })

class DecryptDto:
    api = Namespace('decrypt_tiff_file', description='Tiff file decryptrd related operations')
    decrypt = api.model('', {
        'file_path': fields.String(required=True, description='Encrypted file path'),
        'base_key': fields.String(required=True, description='Base Key'),
        'salt': fields.String(required=True, description='Salt ')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
        'code': fields.String(required=False, description='2FA code'),
    })

class TimerDto:
    api = Namespace('Timer', description='Timer related operations')
    timer = api.model('Timer', {
        'id': fields.Integer(required=False, description='Timer table primary_key'),
        'timer_duration': fields.Float(required=True, description='timer_duration'),
        'description': fields.String(required=True, description='description'),
        'mac_address': fields.String(required=True, description='mac_address'),
        'is_complete': fields.Integer(required=True, description='is_complete'),
        'is_cancel': fields.Integer(required=True, description='is_cancel'),
        'user_id': fields.Integer(required=True, description='user_id'),
        'device_id': fields.Integer(required=True, description='device_id')

    })

class SatelliteDto:
    api = Namespace('Satellite', description='Satellite related operations')
    satellite = api.model('Satellite', {
        'id': fields.Integer(required=False, description='Timer table primary_key'),
        'satellite_name': fields.String(required=True, description='satellite_name'),
        'address': fields.String(required=True, description='address'),
        'is_active': fields.Integer(required=True, description='is_active'),
        'user_id': fields.Integer(required=True, description='user_id')

    })
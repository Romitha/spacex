from app.main import db
from app.main.model.satellite import Satellite
from app.main.model.user import User
from flask import jsonify
from uuid import uuid4
import random


def save_satellite(data, auth_header):
    id = User.decode_auth_token(auth_header)
    address = data['address']
    
    if address:

        satellite_name = data['satellite_name']
        address = data['address']
        is_active = data['is_active']
        user_id = id

        if user_id:
            satellite = Satellite(satellite_name, address, is_active, user_id)
            satellite.save()
            response = jsonify({
                'satellite_name': satellite.satellite_name,
                'created_at': satellite.created_at
            })
            response.status_code = 201
            return response
        else:
            response_object = {
                'status': 'fail',
                'message': 'satellite save action not success',
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'Something went wrong',
        }
        return response_object, 409


def update_satellite(data, auth_header):
    user_id = User.decode_auth_token(auth_header)
    id = data['id']
    satellite = Satellite.query.filter_by(user_id=user_id,id=id).first()

    if satellite:

        satellite.satellite_name = data['satellite_name']
        satellite.address = data['address']
        satellite.is_active = data['is_active']

        satellite.save()

        response = jsonify({
            'status': 'success',
            'message': 'satellite details update action success',
            'device_name': satellite.is_active,
            'mac_address': satellite.address
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'satellite details update action not success',
        }
        return response_object, 409


def find_satellite(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    satellite = Satellite.query.filter_by(user_id=user_id,id=id).first()
    if satellite:
        response = jsonify({
            'satellite_name': satellite.satellite_name,
            'address': satellite.address,
            'is_active': satellite.is_active
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'No data',
        }
        return response_object, 409


def delete_satellite(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    satellite = Satellite.query.filter_by(user_id=user_id,id=id).first()

    if satellite:
        satellite.delete()
        response_object = {
            'status': 'success',
            'message': 'satellite deleted !',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'satellite details delete action not success',
        }
        return response_object, 409


def health_satellite(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    satellite = Satellite.query.filter_by(user_id=user_id,id=id).first()

    if satellite:
        response_object = {
            'status': 'success',
            'health-check': satellite.is_active,
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'satellite details health check action not success',
        }
        return response_object, 409

def orbit_satellite(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    satellite = Satellite.query.filter_by(user_id=user_id,id=id).first()
    random.seed(7)

    if satellite:
        response_object = {
            'status': 'success',
            'orbit-check': random.random(),
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'satellite details health check action not success',
        }
        return response_object, 409

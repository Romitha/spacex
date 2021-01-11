from app.main import db
from app.main.model.device import Device
from app.main.model.user import User
from flask import jsonify
from uuid import uuid4


def save_device(data, auth_header):
    id = User.decode_auth_token(auth_header)
    mac_address = data['mac_address']
    
    if mac_address:

        device_name = data['device_name']
        mac_address = data['mac_address']
        is_active = data['is_active']
        user_id = id

        if user_id:
            device = Device(device_name, mac_address, is_active, user_id)
            device.save()
            response = jsonify({
                'device_name': device.device_name,
                'created_at': device.created_at
            })
            response.status_code = 201
            return response
        else:
            response_object = {
                'status': 'fail',
                'message': 'Device save action not success',
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'Something went wrong',
        }
        return response_object, 409


def update_device(data, auth_header):
    user_id = User.decode_auth_token(auth_header)
    id = data['id']
    device = Device.query.filter_by(user_id=user_id,id=id).first()

    if device:

        device.device_name = data['device_name']
        device.mac_address = data['mac_address']
        device.is_active = data['is_active']
        user_id = id

        device.save()

        response = jsonify({
            'status': 'success',
            'message': 'Device details update action success',
            'device_name': device.device_name,
            'mac_address': device.mac_address
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'Timer details update action not success',
        }
        return response_object, 409

def find_devices_by_user(auth_header):
    id = User.decode_auth_token(auth_header)
    device_lists = Device.query.filter_by(user_id=id).all()
    result = []
    if len(device_lists) > 0:
        for device in device_lists:
            data = {
                'device_name': device.timer_duration,
                'mac_address': device.description,
                'is_active': device.mac_address
            }
            result.append(data)
        response = jsonify(result)
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'No data',
        }
        return response_object, 409


def find_device(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    device = Device.query.filter_by(user_id=user_id,id=id).first()
    if device:
        response = jsonify({
            'device_name': device.timer_duration,
            'mac_address': device.description,
            'is_active': device.mac_address
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'No data',
        }
        return response_object, 409


def delete_device(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    device = Device.query.filter_by(user_id=user_id,id=id).first()

    if device:
        device.delete()
        response_object = {
            'status': 'success',
            'message': 'Device deleted !',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Device details delete action not success',
        }
        return response_object, 409

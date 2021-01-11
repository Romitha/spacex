from app.main import db
from app.main.model.timer import Timer
from app.main.model.user import User
from flask import jsonify
from uuid import uuid4


def save_timer(data, auth_header):
    id = User.decode_auth_token(auth_header)
    timer_duration = data['timer_duration']
    
    if timer_duration:

        # timer_duration = data['timer_duration']
        # description = data['description']
        # mac_address = data['mac_address']
        # is_complete = data['is_complete']
        # is_cancel = data['is_cancel']
        # user_id = id
        # device_id = data['device_id']

        timer_duration = data['timer_duration']
        description = None
        mac_address = None
        is_complete = 0
        is_cancel = 0
        user_id = id
        device_id = None

        if user_id:
            timer = Timer(timer_duration, description, mac_address, is_complete, is_cancel, user_id, device_id)
            timer.save()
            response = jsonify({
                'timer_id': timer.id
            })
            response.status_code = 201
            return response
        else:
            response_object = {
                'status': 'fail',
                'message': 'Timer save action not success',
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'Something went wrong',
        }
        return response_object, 409


def update_timer(data, auth_header):
    user_id = User.decode_auth_token(auth_header)
    id = data['id']
    timer = Timer.query.filter_by(user_id=user_id,id=id).first()

    if timer:

        timer.timer_duration = data['timer_duration']
        timer.description = data['description']
        timer.mac_address = data['mac_address']
        timer.is_complete = data['is_complete']
        timer.is_cancel = data['is_cancel']
        user_id = id
        timer.device_id = data['device_id']

        timer.save()

        response = jsonify({
            'status': 'success',
            'message': 'Timer details update action success',
            'timer_duration': timer.timer_duration,
            'mac_address': timer.mac_address,
            'created_at': timer.created_at,
            'user_id': timer.user_id,
            'updated_at': timer.updated_at
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'Timer details update action not success',
        }
        return response_object, 409

def update_timer_duration(auth_header, id, duration):
    user_id = User.decode_auth_token(auth_header)
    timer = Timer.query.filter_by(user_id=user_id,id=id).first()

    if timer:

        timer.timer_duration = duration
        timer.save()

        response = jsonify({
            'status': 'success',
            'message': 'Timer details update action success'
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'Timer details update action not success',
        }
        return response_object, 409

def update_timer_complete(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    timer = Timer.query.filter_by(user_id=user_id,id=id).first()

    if timer:

        timer.is_complete = 1
        timer.save()

        response = jsonify({
            'status': 'success',
            'message': 'Timer complete action success'
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'Timer complete action not success',
        }
        return response_object, 409


def update_timer_description(auth_header, id, description):
    user_id = User.decode_auth_token(auth_header)
    timer = Timer.query.filter_by(user_id=user_id,id=id).first()

    if timer:

        timer.description = description
        timer.save()

        response = jsonify({
            'status': 'success',
            'message': 'Timer details update action success'
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'Timer details update action not success',
        }
        return response_object, 409

def find_timers_by_user(auth_header):
    id = User.decode_auth_token(auth_header)
    timer_lists = Timer.query.filter_by(user_id=id).all()
    print(timer_lists)
    result = []
    if len(timer_lists) > 0:
        for timer in timer_lists:
            data = {
                'id': timer.id
            }
            result.append(data)
        print(result)
        response = jsonify(result)
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'No data',
        }
        return response_object, 409


def find_timer(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    timer = Timer.query.filter_by(user_id=user_id,id=id).first()
    if timer:
        response = jsonify({
            'timer_duration': timer.timer_duration,
            'description': timer.description,
            'mac_address': timer.mac_address,
            'is_complete': timer.is_complete,
            'is_cancel': timer.is_cancel,
            'user_id': timer.user_id,
            'device_id': timer.device_id
        })
        response.status_code = 201
        return response
    else:
        response_object = {
            'status': 'fail',
            'message': 'No data',
        }
        return response_object, 409


def delete_timer(auth_header, id):
    user_id = User.decode_auth_token(auth_header)
    timer = Timer.query.filter_by(user_id=user_id,id=id).first()

    if timer:
        timer.delete()
        response_object = {
            'status': 'success',
            'message': 'Timer deleted !',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Timer details delete action not success',
        }
        return response_object, 409

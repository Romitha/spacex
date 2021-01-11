import uuid
import datetime
import json
from flask import Flask, url_for, render_template
from app.main import db, flask_bcrypt
from app.main.model.user import User
from flask import jsonify, request
from app.main.util.token import generate_confirmation_token, confirm_token
from app.main.util.email import send_email


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    token = ''
    if not user:
        email = data['email']
        password_hash = flask_bcrypt.generate_password_hash(data['password']).decode('utf-8')
        is_active = data['is_active']
        is_tfa = data['is_tfa']
        is_admin = data['is_admin']

        user = User(email, password_hash, is_active, is_tfa, is_admin)
        user.save()
        if user.id:
            token = generate_confirmation_token(data['email'])
            body = "Welcome! Thanks for signing up. Please click this link to activate your account: "+request.base_url+"confirm/{}".format(token)
            subject = "Please confirm your email"
            email_send = 0
            send_email(user.email, subject, body)

            response = jsonify({
                'status': 'success',
                'message': 'User Successfully Registered ... ! check your email ['+email+']',
                'account_name': user.email,
                'created_at': user.created_at
            })
            response.status_code = 201
            return response
    else:
        response = jsonify({
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
            })
        response.status_code = 409
        return response


def get_all_users(auth_header):
    print('get_all_users')
    id = User.decode_auth_token(auth_header)
    user = User.query.filter_by(id=id).first()
    print(user.is_admin)
    if user.is_admin:
        return User.query.all()
    else:
        response_object = {
            'status': 'fail',
            'message': 'You can not access this URL',
        }
        return response_object, 409


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
    sql = "SELECT LAST_INSERT_ID() as user_id"
    result = db.engine.execute(sql)
    return [dict(row) for row in result]


def test_user():
    sql = "select * from users"
    result = db.engine.execute(sql)
    return jsonify({'result': [dict(row) for row in result]})


def find_user(auth_header):
    id = User.decode_auth_token(auth_header)
    user = User.query.filter_by(id=id).first()
    response = jsonify({
        'id': user.id,
        'email': user.email,
        'is_tfa': user.is_tfa,
        'is_active': user.is_active,
        'is_admin': user.is_admin,
        'status': 'success',
        'message': 'User Successfully Find ... !',
    })
    response.status_code = 201
    return response


def verification_email(token):
    try:
        email = confirm_token(token)
    except:
        response_object = {
            'status': 'danger',
            'message': 'The confirmation link is invalid or has expired.',
        }
        return response_object, 409

    user = User.query.filter_by(email=email).first_or_404()
    if user.is_active:
        response_object = {
            'status': 'success',
            'message': 'Account already confirmed. Please login.',
        }
        return response_object, 201
    else:
        user.is_active = 1
        user.updated_at = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'You have confirmed your account. Thanks!',
        }
        return response_object, 201


def update_user(data, auth_header):
    id = User.decode_auth_token(auth_header)
    if id:

        email = data['email']
        is_active = data['is_active']
        is_tfa = data['is_tfa']
        is_admin = data['is_admin']
        user = User.query.filter_by(id=id).first()

        if user:
            user.email = email
            user.is_active = is_active
            user.is_tfa = is_tfa
            user.is_admin = is_admin
            user.save()
            response = jsonify({
                'email': user.email,
                'created_at': user.created_at,
                'status': 'success',
                'message': 'User Successfully Updated ... !',
            })
            response.status_code = 201
            return response
        else:
            response_object = {
                'status': 'fail',
                'message': 'Setup details update action not success',
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'Unauthorized access',
        }
        return response_object, 409

from flask import request, jsonify
from flask_restplus import Resource
from flask_cors import cross_origin
from ..util.dto import TimerDto
from ..service.timer_service import save_timer, update_timer, find_timers_by_user, find_timer, delete_timer, update_timer_duration, update_timer_complete, update_timer_description
from ..util.decorator import token_required, admin_token_required
import requests

api = TimerDto.api
_timer = TimerDto.timer


@api.route('/')
class Timer(Resource):
    @api.response(201, 'Timer successfully created.')
    @api.doc('create a new timer')
    @api.expect(_timer, validate=False)
    @token_required
    @cross_origin()
    def post(self):
        """Creates a new Timer """
        data = request.json
        auth_header = request.headers.get('Authorization')
        return save_timer(data=data, auth_header=auth_header)

    @api.response(201, 'Timer successfully updated.')
    @api.doc('Update a timer')
    @token_required
    @cross_origin()
    @api.expect(_timer, validate=False)
    def put(self):
        """Update timer """
        data = request.json
        auth_header = request.headers.get('Authorization')
        return update_timer(data=data, auth_header=auth_header)

@api.route('/')
@api.response(404, 'timer not found.')
class GetTimerList(Resource):
    @api.doc('list_of_timer')
    @token_required
    @cross_origin()
    def get(self):
        """List all Timer details"""
        print('List all Timer details')
        auth_header = request.headers.get('Authorization')
        resp = find_timers_by_user(auth_header=auth_header)
        print(resp)
        return resp

@api.route('/<id>/duration')
@api.response(404, 'timer not found.')
class UpdateTimerDuration(Resource):
    @api.doc('update a timer')
    @token_required
    @cross_origin()
    def put(self, id):
        """Update a duration """
        auth_header = request.headers.get('Authorization')
        data = request.json
        duration = data['timer_duration']
        resp = update_timer_duration(auth_header=auth_header, id=id, duration=duration)
        return resp

@api.route('/<id>/complete')
@api.response(404, 'timer not found.')
class UpdateTimerComplete(Resource):
    @api.doc('update a timer')
    @token_required
    @cross_origin()
    def put(self, id):
        """Update a setting """
        auth_header = request.headers.get('Authorization')
        resp = update_timer_complete(auth_header=auth_header, id=id)
        return resp

@api.route('/<id>/description')
@api.response(404, 'timer not found.')
class UpdateTimerDescription(Resource):
    @api.doc('update a timer description')
    @token_required
    @cross_origin()
    def put(self, id):
        """Update a description """
        auth_header = request.headers.get('Authorization')
        data = request.json
        description = data['description']
        resp = update_timer_description(auth_header=auth_header, id=id, description=description)
        return resp

@api.route('/<id>')
@api.response(404, 'Timer not found.')
class FindTimer(Resource):
    @api.doc('get a timer')
    @token_required
    @cross_origin()
    def get(self, id):
        """get a timer given its id"""
        auth_header = request.headers.get('Authorization')
        timer = find_timer(auth_header=auth_header, id=id)
        return timer


@api.route('/<id>')
@api.response(404, 'timer not found.')
class DeleteTimer(Resource):
    @api.doc('delete a timer')
    @token_required
    @cross_origin()
    def delete(self, id):
        """Delete a setting """
        auth_header = request.headers.get('Authorization')
        resp = delete_timer(auth_header=auth_header, id=id)
        return resp
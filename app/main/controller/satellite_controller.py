from flask import request, jsonify
from flask_restplus import Resource
from flask_cors import cross_origin
from ..util.dto import SatelliteDto
from ..service.sattelite_service import save_satellite, update_satellite, health_satellite, delete_satellite, orbit_satellite
from ..util.decorator import token_required, admin_token_required
import requests

api = SatelliteDto.api
_satellite = SatelliteDto.satellite


@api.route('/')
class Satellite(Resource):
    @api.response(201, 'Satellite successfully created.')
    @api.doc('create a new Satellite')
    @api.expect(_satellite, validate=False)
    @token_required
    @cross_origin()
    def post(self):
        """Creates a new Satellite """
        data = request.json
        auth_header = request.headers.get('Authorization')
        return save_satellite(data=data, auth_header=auth_header)

    @api.response(201, 'Satellite successfully updated.')
    @api.doc('Update a Satellite')
    @token_required
    @cross_origin()
    @api.expect(_satellite, validate=False)
    def put(self):
        """Update timer """
        data = request.json
        auth_header = request.headers.get('Authorization')
        return update_satellite(data=data, auth_header=auth_header)

@api.route('/<id>')
@api.response(404, 'timer not found.')
class DeleteSatellite(Resource):
    @api.doc('delete a timer')
    @token_required
    @cross_origin()
    def delete(self, id):
        """Delete a setting """
        auth_header = request.headers.get('Authorization')
        resp = delete_satellite(auth_header=auth_header, id=id)
        return resp


@api.route('/health-check/<id>')
@api.response(404, 'Satellite not found.')
class SatelliteHealthCheck(Resource):
    @api.doc('get a health-check')
    @token_required
    @cross_origin()
    def get(self, id):
        """Get a health Check """
        auth_header = request.headers.get('Authorization')
        resp = health_satellite(auth_header=auth_header, id=id)
        return resp


@api.route('/get-orbit/<id>')
@api.response(404, 'Satellite not found.')
class SatelliteHealthCheck(Resource):
    @api.doc('get a orbit-check')
    @token_required
    @cross_origin()
    def get(self, id):
        """Get a health Check """
        auth_header = request.headers.get('Authorization')
        resp = orbit_satellite(auth_header=auth_header, id=id)
        return resp
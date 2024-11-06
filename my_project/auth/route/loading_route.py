from flask import Blueprint, request, jsonify
from my_project.auth.controller.loading_controller import LoadingController


loading_bp = Blueprint('loading', __name__)

@loading_bp.route('/loading', methods=['GET'])
def get_all_loadings():
    return LoadingController.get_all_loadings()

@loading_bp.route('/loading/<int:loading_id>', methods=['GET'])
def get_loading_by_id(loading_id):
    return LoadingController.get_loading_by_id(loading_id)

@loading_bp.route('/loading', methods=['POST'])
def create_loading():
    data = request.get_json()
    return LoadingController.create_loading(data)

@loading_bp.route('/loading/<int:loading_id>', methods=['PUT'])
def update_loading(loading_id):
    data = request.get_json()
    return LoadingController.update_loading(loading_id, data)

@loading_bp.route('/loading/<int:loading_id>', methods=['DELETE'])
def delete_loading(loading_id):
    return LoadingController.delete_loading(loading_id)

from flask import Blueprint, request, jsonify
from my_project.auth.controller.loading_controller import LoadingController
from my_project.auth.models.all import LoadinDetail

loading_bp = Blueprint('loading', __name__)

@loading_bp.route('/loading', methods=['GET'])
def get_all_loadings():
    return LoadingController.get_all_loadings()

@loading_bp.route('/loading/<int:loading_id>', methods=['GET'])
def get_loading_by_id(loading_id):
    return LoadingController.get_loading_by_id(loading_id)

@loading_bp.route('/loading', methods=['POST'])
def create_loading():
    return LoadingController.create_loading()

@loading_bp.route('/loading/<int:loading_id>', methods=['PUT'])
def update_loading(loading_id):
    return LoadingController.update_loading(loading_id)

@loading_bp.route('/loading/<int:loading_id>', methods=['DELETE'])
def delete_loading(loading_id):
    return LoadingController.delete_loading(loading_id)

from db_init import db
from my_project.auth.service.loading_service import LoadinDetailService

loadin_detail_bp = Blueprint('loadin_detail', __name__)


@loadin_detail_bp.route('/loadin_details', methods=['GET'])
def get_all_loadin_details():
    session = db.session
    loadin_details = LoadinDetailService.get_all_loadin_details(session)
    return jsonify([detail.to_dict() for detail in loadin_details])


@loadin_detail_bp.route('/loadin_detail/<int:loading_id>/<int:snack_id>', methods=['GET'])
def get_loadin_detail_by_ids(loading_id, snack_id):
    """Отримати запис по loading_id та snack_id."""
    session = db.session
    loadin_detail = LoadinDetailService.get_loadin_detail_by_ids(session, loading_id, snack_id)
    if loadin_detail:
        return jsonify(loadin_detail.to_dict())
    return jsonify({"message": "Not found"}), 404

@loadin_detail_bp.route('/loadin_detail', methods=['POST'])
def add_loadin_detail():
    return LoadingController.create_loadin_detail()

@loadin_detail_bp.route('/loadin_detail/<int:loadin_detail_id>', methods=['GET'])
def get_loadin_detail(loadin_detail_id: int):
    session = db.session
    loadin_detail = session.query(LoadinDetail).filter(LoadinDetail.loading_id == loadin_detail_id).first()

    if loadin_detail:
        return jsonify(loadin_detail.to_dict())  # Повертаємо дані у форматі JSON
    return jsonify({"message": "LoadinDetail not found"}), 404


@loadin_detail_bp.route('/loadin_detail', methods=['POST'])
def create_loadin_detail():
    """Створити новий зв'язок між Loading і Snack."""
    session = db.session
    data = request.get_json()
    loading_id = data.get('loading_id')
    snack_id = data.get('snack_id')

    if not loading_id or not snack_id:
        return jsonify({"message": "Missing required fields"}), 400

    loadin_detail = LoadinDetailService.create_loadin_detail(session, loading_id, snack_id)
    return jsonify(loadin_detail.to_dict()), 201


@loadin_detail_bp.route('/loadin_detail/<int:loading_id>/<int:snack_id>', methods=['DELETE'])
def delete_loadin_detail(loading_id, snack_id):
    """Видалити зв'язок між Loading і Snack."""
    session = db.session
    loadin_detail = LoadinDetailService.delete_loadin_detail(session, loading_id, snack_id)
    if loadin_detail:
        return jsonify({"message": "Deleted successfully"}), 200
    return jsonify({"message": "Not found"}), 404


@loadin_detail_bp.route('/loadings_by_snack/<int:snack_id>', methods=['GET'])
def get_loadings_by_snack(snack_id):
    session = db.session
    loadin_details = LoadinDetailService.get_loadings_by_snack(session, snack_id)
    if loadin_details:
        loadings = [detail.loading.to_dict() for detail in loadin_details]
        return jsonify(loadings)
    return jsonify({"message": "Not found"}), 404


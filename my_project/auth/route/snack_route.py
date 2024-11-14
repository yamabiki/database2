from flask import Blueprint, jsonify
from my_project.auth.controller.snack_controller import SnackController
from my_project.auth.models.all import Snack

snack_bp = Blueprint('snack', __name__)

@snack_bp.route('/snacks', methods=['GET'])
def get_all_snacks():
    return SnackController.get_all_snacks()

@snack_bp.route('/brands/<int:brand_id>/snacks', methods=['GET'])
def get_snacks_by_brand(brand_id):
    # Fetch all snacks by brand_id
    snacks = Snack.query.filter_by(brand_id=brand_id).all()
    return jsonify([snack.to_dict() for snack in snacks])

@snack_bp.route('/snacks/<int:snack_id>', methods=['GET'])
def get_snack_by_id(snack_id):
    return SnackController.get_snack_by_id(snack_id)

@snack_bp.route('/snacks', methods=['POST'])
def create_snack():
    return SnackController.create_snack()

@snack_bp.route('/snacks/<int:snack_id>', methods=['PUT'])
def update_snack(snack_id):
    return SnackController.update_snack(snack_id)

@snack_bp.route('/snacks/<int:snack_id>', methods=['DELETE'])
def delete_snack(snack_id):
    return SnackController.delete_snack(snack_id)

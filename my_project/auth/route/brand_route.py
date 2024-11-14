from flask import Blueprint
from my_project.auth.controller.brand_controller import BrandController

brand_bp = Blueprint('brand', __name__)

@brand_bp.route('/brands', methods=['GET'])
def get_all_brands():
    return BrandController.get_all_brands()

@brand_bp.route('/brands/<int:brand_id>', methods=['GET'])
def get_brand_by_id(brand_id):
    return BrandController.get_brand_by_id(brand_id)

@brand_bp.route('/brands', methods=['POST'])
def create_brand():
    return BrandController.create_brand()

@brand_bp.route('/brands/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    return BrandController.update_brand(brand_id)

@brand_bp.route('/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    return BrandController.delete_brand(brand_id)

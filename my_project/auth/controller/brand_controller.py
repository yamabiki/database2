from flask import jsonify, request
from my_project.auth.service.brand_service import BrandService
from db_init import db

class BrandController:
    @staticmethod
    def get_all_brands():
        brands = BrandService.get_all_brands(db.session)
        return jsonify([brand.to_dict() for brand in brands])

    @staticmethod
    def get_brand_by_id(brand_id):
        brand = BrandService.get_brand_by_id(db.session, brand_id)
        return jsonify(brand.to_dict()) if brand else (jsonify({"error": "Brand not found"}), 404)

    @staticmethod
    def create_brand():
        brand_data = request.json
        brand = BrandService.create_brand(db.session, brand_data)
        return jsonify(brand.to_dict()), 201

    @staticmethod
    def update_brand(brand_id):
        updated_data = request.json
        brand = BrandService.update_brand(db.session, brand_id, updated_data)
        return jsonify(brand.to_dict()) if brand else (jsonify({"error": "Brand not found"}), 404)

    @staticmethod
    def delete_brand(brand_id):
        brand = BrandService.delete_brand(db.session, brand_id)
        return jsonify({"message": "Brand deleted"}) if brand else (jsonify({"error": "Brand not found"}), 404)

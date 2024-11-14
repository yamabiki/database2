from flask import jsonify, request
from my_project.auth.service.snack_service import SnackService
from db_init import db

class SnackController:
    @staticmethod
    def get_all_snacks():
        snacks = SnackService.get_all_snacks(db.session)
        return jsonify([snack.to_dict() for snack in snacks])

    @staticmethod
    def get_snack_by_id(snack_id):
        snack = SnackService.get_snack_by_id(db.session, snack_id)
        return jsonify(snack.to_dict()) if snack else (jsonify({"error": "Snack not found"}), 404)

    @staticmethod
    def create_snack():
        snack_data = request.json
        snack = SnackService.create_snack(db.session, snack_data)
        return jsonify(snack.to_dict()), 201

    @staticmethod
    def update_snack(snack_id):
        updated_data = request.json
        snack = SnackService.update_snack(db.session, snack_id, updated_data)
        return jsonify(snack.to_dict()) if snack else (jsonify({"error": "Snack not found"}), 404)

    @staticmethod
    def delete_snack(snack_id):
        snack = SnackService.delete_snack(db.session, snack_id)
        return jsonify({"message": "Snack deleted"}) if snack else (jsonify({"error": "Snack not found"}), 404)

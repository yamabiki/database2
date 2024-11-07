from flask import jsonify, request
from my_project.auth.service.loading_service import LoadingService
from db_init import db
from datetime import datetime

class LoadingController:
    @staticmethod
    def get_all_loadings():
        loadings = LoadingService.get_all_loadings(db.session)
        return jsonify([loading.to_dict() for loading in loadings])

    @staticmethod
    def get_loading_by_id(loading_id: int):
        loading = LoadingService.get_loading_by_id(db.session, loading_id)
        return jsonify(loading.to_dict()) if loading else (jsonify({"error": "Loading not found"}), 404)

    @staticmethod
    def create_loading():
        loading_data = request.json

        # Convert date string to datetime object if necessary
        if 'date' in loading_data:
            try:
                loading_data['date'] = datetime.strptime(loading_data['date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        loading = LoadingService.create_loading(db.session, loading_data)
        return jsonify(loading.to_dict()), 201

    @staticmethod
    def update_loading(loading_id: int):
        updated_data = request.json

        # Convert date string to datetime object if necessary
        if 'date' in updated_data:
            try:
                updated_data['date'] = datetime.strptime(updated_data['date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        loading = LoadingService.update_loading(db.session, loading_id, updated_data)
        return jsonify(loading.to_dict()) if loading else (jsonify({"error": "Loading not found"}), 404)

    @staticmethod
    def delete_loading(loading_id: int):
        loading = LoadingService.delete_loading(db.session, loading_id)
        return jsonify({"message": "Loading deleted"}) if loading else (jsonify({"error": "Loading not found"}), 404)

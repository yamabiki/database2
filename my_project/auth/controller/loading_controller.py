from flask import jsonify, request
from my_project.auth.service.loading_service import LoadingService
from db_init import db

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
        loading = LoadingService.create_loading(db.session, loading_data)
        return jsonify(loading.to_dict()), 201

    @staticmethod
    def update_loading(loading_id: int):
        updated_data = request.json
        loading = LoadingService.update_loading(db.session, loading_id, updated_data)
        return jsonify(loading.to_dict()) if loading else (jsonify({"error": "Loading not found"}), 404)

    @staticmethod
    def delete_loading(loading_id: int):
        loading = LoadingService.delete_loading(db.session, loading_id)
        return jsonify({"message": "Loading deleted"}) if loading else (jsonify({"error": "Loading not found"}), 404)
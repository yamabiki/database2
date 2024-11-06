from flask import jsonify, request
from my_project.auth.service.technician_service import TechnicianService
from db_init import db

class TechnicianController:
    @staticmethod
    def get_all_technicians():
        technicians = TechnicianService.get_all_technicians(db.session)
        return jsonify([technician.to_dict() for technician in technicians])

    @staticmethod
    def get_technician_by_id(technician_id):
        technician = TechnicianService.get_technician_by_id(db.session, technician_id)
        return jsonify(technician.to_dict()) if technician else (jsonify({"error": "Technician not found"}), 404)

    @staticmethod
    def create_technician():
        technician_data = request.json
        technician = TechnicianService.create_technician(db.session, technician_data)
        return jsonify(technician.to_dict()), 201

    @staticmethod
    def update_technician(technician_id):
        updated_data = request.json
        technician = TechnicianService.update_technician(db.session, technician_id, updated_data)
        return jsonify(technician.to_dict()) if technician else (jsonify({"error": "Technician not found"}), 404)

    @staticmethod
    def delete_technician(technician_id):
        technician = TechnicianService.delete_technician(db.session, technician_id)
        return jsonify({"message": "Technician deleted"}) if technician else (jsonify({"error": "Technician not found"}), 404)

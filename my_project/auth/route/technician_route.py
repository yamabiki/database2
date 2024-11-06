from flask import Blueprint
from my_project.auth.controller.technician_controller import TechnicianController

technician_bp = Blueprint('technician', __name__)

@technician_bp.route('/technicians', methods=['GET'])
def get_all_technicians():
    return TechnicianController.get_all_technicians()

@technician_bp.route('/technicians/<int:technician_id>', methods=['GET'])
def get_technician_by_id(technician_id):
    return TechnicianController.get_technician_by_id(technician_id)

@technician_bp.route('/technicians', methods=['POST'])
def create_technician():
    return TechnicianController.create_technician()

@technician_bp.route('/technicians/<int:technician_id>', methods=['PUT'])
def update_technician(technician_id):
    return TechnicianController.update_technician(technician_id)

@technician_bp.route('/technicians/<int:technician_id>', methods=['DELETE'])
def delete_technician(technician_id):
    return TechnicianController.delete_technician(technician_id)

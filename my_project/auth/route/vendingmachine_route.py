from flask import Blueprint, request, jsonify
from my_project.auth.controller.vendingmachine_controller import VendingMachineController

vending_machine_bp = Blueprint('vending_machine', __name__)

@vending_machine_bp.route('/vending_machine', methods=['GET'])
def get_all_vending_machines():
    return VendingMachineController.get_all_vending_machines()

@vending_machine_bp.route('/vending_machine/<int:vending_machine_id>', methods=['GET'])
def get_vending_machine_by_id(vending_machine_id):
    return VendingMachineController.get_vending_machine_by_id(vending_machine_id)

@vending_machine_bp.route('/vending_machine', methods=['POST'])
def create_vending_machine():
    data = request.get_json()
    return VendingMachineController.create_vending_machine(data)

@vending_machine_bp.route('/vending_machine/<int:vending_machine_id>', methods=['PUT'])
def update_vending_machine(vending_machine_id):
    data = request.get_json()
    return VendingMachineController.update_vending_machine(vending_machine_id, data)

@vending_machine_bp.route('/vending_machine/<int:vending_machine_id>', methods=['DELETE'])
def delete_vending_machine(vending_machine_id):
    return VendingMachineController.delete_vending_machine(vending_machine_id)

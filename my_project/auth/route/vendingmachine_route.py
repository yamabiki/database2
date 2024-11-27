from flask import Blueprint, request, jsonify
from sqlalchemy import text
from sqlalchemy.engine.result import null_result
from my_project.auth.models.all import TechnicianHasVendingMachine
from my_project.auth.controller.vendingmachine_controller import VendingMachineController
from db_init import db

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


@vending_machine_bp.route('/vending_machine/aggregation', methods=['GET'])
def get_vending_machine_aggregation():
    try:


        operation = request.args.get('operation')

        valid_operations = ['MAX', 'MIN', 'AVG', 'SUM']

        if operation not in valid_operations:
            return jsonify(
                {"error": "Invalid operation provided. Please use one of the following: MAX, MIN, AVG, SUM"}), 400

        if not operation:
            return jsonify({"error": "Missing parameter: operation"}), 400

        query = text("SELECT get_vending_machine_aggregation(:operation)")

        result = db.session.execute(query, {'operation': operation}).fetchone()

        if result:
            return jsonify({"result": result[0]}), 200
        else:
            return jsonify({"error": "Error calculating aggregation result"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


from flask import request, jsonify


@vending_machine_bp.route('/add_snack_to_machine', methods=['POST'])
def add_snack_to_machine_route():
    data = request.get_json()
    machine_id = data.get('machine_id')
    snack_id = data.get('snack_id')

    # Викликаємо функцію для додавання
    response = VendingMachineController.add_snack_to_machine(machine_id, snack_id)
    return jsonify(response)


@vending_machine_bp.route('/vending_machine_stock', methods=['GET'])
def vending_machine_stock_route():
    # Отримуємо всі записи
    stocks = VendingMachineController.get_vending_machine_stock()

    # Повертаємо їх як JSON
    return jsonify(stocks)


@vending_machine_bp.route('/technician_has_vending_machine', methods=['POST'])
def assign_technician_to_vending_machine_route():
    data = request.get_json()
    technician_id = data.get('technician_id')
    machine_id = data.get('machine_id')

    if not technician_id or not machine_id:
        return jsonify({"message": "Technician ID and Machine ID are required."}), 400

    response = VendingMachineController.add_technician_to_vending_machine(technician_id, machine_id)
    return jsonify(response)

@vending_machine_bp.route('/technician_has_vending_machine', methods=['GET'])
def get_technician_has_vending_machine():
    # Отримуємо всі записи з таблиці technician_has_vending_machine
    technician_vending_machines = TechnicianHasVendingMachine.query.all()

    # Перетворюємо дані в словники для зручності
    technician_vending_machines_list = [{
        "technician_id": record.technician_id,
        "machine_id": record.machine_id,
        "technician_name": record.technician.name,
        "vending_machine_address": record.vending_machine.adress
    } for record in technician_vending_machines]

    return jsonify(technician_vending_machines_list), 200

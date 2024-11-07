from flask import jsonify, request
from my_project.auth.service.vendingmachine_service import VendingMachineService
from db_init import db

class VendingMachineController:
    @staticmethod
    def get_all_vending_machines():
        vending_machines = VendingMachineService.get_all_vending_machines(db.session)
        return jsonify([vending_machine.to_dict() for vending_machine in vending_machines])

    @staticmethod
    def get_vending_machine_by_id(vending_machine_id: int):
        vending_machine = VendingMachineService.get_vending_machine_by_id(db.session, vending_machine_id)
        return jsonify(vending_machine.to_dict()) if vending_machine else (jsonify({"error": "Vending machine not found"}), 404)

    @staticmethod
    def create_vending_machine(vending_machine_data: dict):
        vending_machine = VendingMachineService.create_vending_machine(db.session, vending_machine_data)
        return jsonify(vending_machine.to_dict()), 201

    @staticmethod
    def update_vending_machine(vending_machine_id: int, updated_data: dict):
        vending_machine = VendingMachineService.update_vending_machine(db.session, vending_machine_id, updated_data)
        return jsonify(vending_machine.to_dict()) if vending_machine else (jsonify({"error": "Vending machine not found"}), 404)

    @staticmethod
    def delete_vending_machine(vending_machine_id: int):
        vending_machine = VendingMachineService.delete_vending_machine(db.session, vending_machine_id)
        return jsonify({"message": "Vending machine deleted"}) if vending_machine else (jsonify({"error": "Vending machine not found"}), 404)

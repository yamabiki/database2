from flask import jsonify, request
from my_project.auth.service.vendingmachine_service import VendingMachineService
from my_project.auth.models.all import VendingMachineStock, TechnicianHasVendingMachine

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

    @staticmethod
    def add_snack_to_machine(machine_id, snack_id):
        # Перевіряємо, чи вже існує зв'язок
        existing_stock = VendingMachineStock.query.filter_by(machine_id=machine_id, snack_id=snack_id).first()
        if existing_stock:
            return {"message": "This snack is already added to the vending machine."}

        # Створюємо новий запис у таблиці зв'язку
        new_stock = VendingMachineStock(machine_id=machine_id, snack_id=snack_id)
        db.session.add(new_stock)
        db.session.commit()

        return {"message": "Snack added to the vending machine successfully."}

    @staticmethod
    def get_vending_machine_stock():
        # Отримуємо всі записи з таблиці VendingMachineStock
        all_stocks = VendingMachineStock.query.all()

        # Перетворюємо їх у список словників для зручного відображення
        result = []
        for stock in all_stocks:
            result.append({
                "machine_id": stock.machine_id,
                "snack_name": stock.snack.name,  # Отримуємо назву снука через зв'язок
            })

        return result

    @staticmethod
    def add_technician_to_vending_machine(technician_id, machine_id):
        # Перевіряємо, чи вже існує запис
        existing_record = TechnicianHasVendingMachine.query.filter_by(technician_id=technician_id,
                                                                      machine_id=machine_id).first()

        if existing_record:
            return {"message": "Technician already assigned to this vending machine."}

        # Створюємо новий запис
        new_assignment = TechnicianHasVendingMachine(technician_id=technician_id, machine_id=machine_id)
        db.session.add(new_assignment)
        db.session.commit()

        return {"message": "Technician assigned to vending machine."}
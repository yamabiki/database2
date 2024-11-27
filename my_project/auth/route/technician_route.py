from flask import Blueprint, jsonify
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db_init import db
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

@technician_bp.route('/technicians/insert_noname', methods=['POST'])
def insert_noname_technicians():
    try:
        # Викликаємо збережену процедуру insert_noname_technicians
        db.session.execute(text("CALL insert_noname_technicians()"))
        db.session.commit()
        return jsonify({"message": "10 technicians inserted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@technician_bp.route('/technicians/create_dynamic_tables', methods=['POST'])
def create_dynamic_tables():
    try:
        db.session.execute(text("CALL CreateDynamicDatabases()"))
        db.session.commit()
        return jsonify({"message": "Dynamic tables created successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@technician_bp.route('/technicians/drop_dynamic_databases', methods=['POST'])
def drop_dynamic_databases():
    try:
        # Виконання збереженої процедури
        db.session.execute(text("CALL DropDynamicDatabases()"))
        db.session.commit()
        return jsonify({"message": "Dynamic databases dropped successfully"}), 200
    except SQLAlchemyError as e:
        # У разі помилки виконуємо відкат транзакції
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
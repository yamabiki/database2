from flask import Blueprint, jsonify, request
from db_init import db
from my_project.auth.controller.snack_controller import SnackController, PromotionController
from my_project.auth.models.all import Snack, Brand

snack_bp = Blueprint('snack', __name__)

@snack_bp.route('/snacks', methods=['GET'])
def get_all_snacks():
    return SnackController.get_all_snacks()

@snack_bp.route('/brands/<int:brand_id>/snacks', methods=['GET'])
def get_snacks_by_brand(brand_id):
    # Fetch all snacks by brand_id
    snacks = Snack.query.filter_by(brand_id=brand_id).all()
    return jsonify([snack.to_dict() for snack in snacks])

@snack_bp.route('/snacks/<int:snack_id>', methods=['GET'])
def get_snack_by_id(snack_id):
    return SnackController.get_snack_by_id(snack_id)

@snack_bp.route('/snacks', methods=['POST'])
def create_snack():
    return SnackController.create_snack()

@snack_bp.route('/snacks/<int:snack_id>', methods=['PUT'])
def update_snack(snack_id):
    return SnackController.update_snack(snack_id)

@snack_bp.route('/snacks/<int:snack_id>', methods=['DELETE'])
def delete_snack(snack_id):
    return SnackController.delete_snack(snack_id)


@snack_bp.route('/promotions/<int:snack_id>', methods=['GET'])
def get_promotions_by_snack(snack_id):
    return PromotionController.get_promotions_by_snack(snack_id)

@snack_bp.route('/promotions/<int:snack_id>', methods=['DELETE'])
def delete_promotions_by_snack(snack_id):
    return PromotionController.delete_promotions_by_snack(snack_id)

@snack_bp.route('/promotions', methods=['POST'])
def create_promotion():
    return PromotionController.create_promotion()

@snack_bp.route('/brands', methods=['POST'])
def add_brand():
    # Отримуємо параметр brand_name з заголовка
    brand_name = request.headers.get('Brand-Name')  # Параметр "Brand-Name" з headers

    # Перевірка, чи передано значення brand_name
    if not brand_name:
        return jsonify({"message": "Brand name is required in headers"}), 400

    # Створення нового бренду
    new_brand = Brand(
        brand_name=brand_name  # Тільки правильний параметр
    )

    # Додавання нового бренду до бази даних
    try:
        db.session.add(new_brand)
        db.session.commit()  # Фіксація змін у базі даних
        return jsonify(new_brand.to_dict()), 201  # Повертаємо інформацію про створений бренд
    except Exception as e:
        db.session.rollback()  # Откат змін у разі помилки
        return jsonify({"message": str(e)}), 500
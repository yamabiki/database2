from flask import jsonify, request
from my_project.auth.service.snack_service import SnackService
from db_init import db

class SnackController:
    @staticmethod
    def get_all_snacks():
        snacks = SnackService.get_all_snacks(db.session)
        return jsonify([snack.to_dict() for snack in snacks])

    @staticmethod
    def get_snack_by_id(snack_id):
        snack = SnackService.get_snack_by_id(db.session, snack_id)
        return jsonify(snack.to_dict()) if snack else (jsonify({"error": "Snack not found"}), 404)

    @staticmethod
    def create_snack():
        snack_data = request.json
        snack = SnackService.create_snack(db.session, snack_data)
        return jsonify(snack.to_dict()), 201

    @staticmethod
    def update_snack(snack_id):
        updated_data = request.json
        snack = SnackService.update_snack(db.session, snack_id, updated_data)
        return jsonify(snack.to_dict()) if snack else (jsonify({"error": "Snack not found"}), 404)

    @staticmethod
    def delete_snack(snack_id):
        snack = SnackService.delete_snack(db.session, snack_id)
        return jsonify({"message": "Snack deleted"}) if snack else (jsonify({"error": "Snack not found"}), 404)

from flask import jsonify, request
from my_project.auth.service.snack_service import PromotionService
from db_init import db

class PromotionController:
    @staticmethod
    def get_all_promotions():
        promotions = PromotionService.get_all_promotions(db.session)
        return jsonify([promotion.to_dict() for promotion in promotions])

    @staticmethod
    def get_promotions_by_snack(snack_id):
        """Отримати акції для конкретного снека."""
        try:
            promotions = PromotionService.get_promotions_by_snack(db.session, snack_id)
            return jsonify([promotion.to_dict() for promotion in promotions]), 200
        except Exception as e:
            return jsonify({"error": str(e)}),

    @staticmethod
    def delete_promotions_by_snack(snack_id):
        promotions = PromotionService.delete_promotions_by_snack(db.session, snack_id)
        if promotions:
            return jsonify({"message": "Promotions deleted"})
        else:
            return jsonify({"error": "Promotions not found"}), 404

    @staticmethod
    def get_promotion_by_id(promotion_id):
        promotion = PromotionService.get_promotion_by_id(db.session, promotion_id)
        return jsonify(promotion.to_dict()) if promotion else (jsonify({"error": "Promotion not found"}), 404)

    @staticmethod
    def create_promotion():
        promotion_data = request.json
        promotion = PromotionService.create_promotion(db.session, promotion_data)
        return jsonify(promotion.to_dict()), 201

    @staticmethod
    def update_promotion(promotion_id):
        updated_data = request.json
        promotion = PromotionService.update_promotion(db.session, promotion_id, updated_data)
        return jsonify(promotion.to_dict()) if promotion else (jsonify({"error": "Promotion not found"}), 404)

    @staticmethod
    def delete_promotion(promotion_id):
        promotion = PromotionService.delete_promotion(db.session, promotion_id)
        return jsonify({"message": "Promotion deleted"}) if promotion else (jsonify({"error": "Promotion not found"}), 404)

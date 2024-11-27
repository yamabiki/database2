from my_project.auth.dao.snack_dao import SnackDAO

class SnackService:
    @staticmethod
    def get_all_snacks(session):
        return SnackDAO.get_all_snacks(session)

    @staticmethod
    def get_snack_by_id(session, snack_id):
        return SnackDAO.get_snack_by_id(session, snack_id)

    @staticmethod
    def create_snack(session, snack_data):
        return SnackDAO.create_snack(session, snack_data)

    @staticmethod
    def update_snack(session, snack_id, updated_data):
        return SnackDAO.update_snack(session, snack_id, updated_data)

    @staticmethod
    def delete_snack(session, snack_id):
        return SnackDAO.delete_snack(session, snack_id)

from my_project.auth.dao.snack_dao import PromotionsDAO

class PromotionService:
    @staticmethod
    def get_all_promotions(session):
        """Отримати всі акції"""
        return PromotionsDAO.get_all_promotions(session)

    @staticmethod
    def get_promotions_by_snack(session, snack_id):
        """Отримати акції для конкретного снека."""
        return PromotionsDAO.get_promotions_by_snack(session, snack_id)

    @staticmethod
    def delete_promotions_by_snack(session, snack_id):
        """Отримати акції для конкретного снека."""
        return PromotionsDAO.delete_promotions_by_snack(session, snack_id)

    @staticmethod
    def get_promotion_by_id(session, promotion_id):
        """Отримати акцію за її ID"""
        return PromotionsDAO.get_promotion_by_id(session, promotion_id)

    @staticmethod
    def create_promotion(session, promotion_data):
        """Створити нову акцію"""
        # Тут можна додати додаткову валідацію або обробку даних
        return PromotionsDAO.create_promotion(session, promotion_data)

    @staticmethod
    def update_promotion(session, promotion_id, updated_data):
        """Оновити акцію за її ID"""
        # Тут можна додавати додаткову логіку перевірок
        return PromotionsDAO.update_promotion(session, promotion_id, updated_data)

    @staticmethod
    def delete_promotion(session, promotion_id):
        """Видалити акцію за її ID"""
        return PromotionsDAO.delete_promotion(session, promotion_id)

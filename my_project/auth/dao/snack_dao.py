from my_project.auth.models.all import Snack, Promotion

class SnackDAO:
    @staticmethod
    def get_all_snacks(session):
        return session.query(Snack).all()

    @staticmethod
    def get_snack_by_id(session, snack_id):
        return session.query(Snack).get(snack_id)

    @staticmethod
    def create_snack(session, snack_data):
        snack = Snack(**snack_data)
        session.add(snack)
        session.commit()
        return snack

    @staticmethod
    def update_snack(session, snack_id, updated_data):
        snack = session.query(Snack).get(snack_id)
        if snack:
            for key, value in updated_data.items():
                setattr(snack, key, value)
            session.commit()
        return snack

    @staticmethod
    def delete_snack(session, snack_id):
        snack = session.query(Snack).get(snack_id)
        if snack:
            session.delete(snack)
            session.commit()
        return snack


class PromotionsDAO:
        @staticmethod
        def get_all_promotions(session):
            """Отримати всі акції."""
            return session.query(Promotion).all()

        @staticmethod
        def get_promotions_by_snack(session, snack_id):
            """Отримати акції для конкретного снека за його ID"""
            return session.query(Promotion).filter_by(snack_id=snack_id).all()

        @staticmethod
        def delete_promotions_by_snack(session, snack_id):
            """Видалити акції для конкретного снека за його ID"""
            promotions_to_delete = session.query(Promotion).filter_by(snack_id=snack_id).all()

            # Якщо акції знайдені, видалити їх
            if promotions_to_delete:
                for promotion in promotions_to_delete:
                    session.delete(promotion)
                session.commit()
            return promotions_to_delete

        @staticmethod
        def get_promotion_by_id(session, promotion_id):
            """Отримати акцію за її ID."""
            return session.query(Promotion).get(promotion_id)

        @staticmethod
        def create_promotion(session, promotion_data):
            """Створити нову акцію."""
            promotion = Promotion(**promotion_data)
            session.add(promotion)
            session.commit()
            return promotion

        @staticmethod
        def update_promotion(session, promotion_id, updated_data):
            """Оновити дані акції."""
            promotion = session.query(Promotion).get(promotion_id)
            if promotion:
                for key, value in updated_data.items():
                    setattr(promotion, key, value)
                session.commit()
            return promotion

        @staticmethod
        def delete_promotion(session, promotion_id):
            """Видалити акцію."""
            promotion = session.query(Promotion).get(promotion_id)
            if promotion:
                session.delete(promotion)
                session.commit()
            return promotion



from my_project.auth.dao.loading_dao import LoadingDAO
from sqlalchemy.orm import Session
from my_project.auth.dao.loading_dao import LoadinDetailDAO

class LoadingService:
    @staticmethod
    def get_all_loadings(session: Session):
        return LoadingDAO.get_all_loadings(session)

    @staticmethod
    def get_loading_by_id(session: Session, loading_id: int):
        return LoadingDAO.get_loading_by_id(session, loading_id)

    @staticmethod
    def create_loading(session: Session, loading_data: dict):
        return LoadingDAO.create_loading(session, loading_data)

    @staticmethod
    def update_loading(session: Session, loading_id: int, updated_data: dict):
        return LoadingDAO.update_loading(session, loading_id, updated_data)

    @staticmethod
    def delete_loading(session: Session, loading_id: int):
        return LoadingDAO.delete_loading(session, loading_id)

class LoadinDetailService:

    @staticmethod
    def get_all_loadin_details(session: Session):
        """Отримати всі записи з loadin_detail."""
        return LoadinDetailDAO.get_all_loadin_details(session)

    @staticmethod
    def get_loadin_detail_by_ids(session: Session, loading_id: int, snack_id: int):
        """Отримати запис по loading_id та snack_id."""
        return LoadinDetailDAO.get_loadin_detail_by_ids(session, loading_id, snack_id)

    @staticmethod
    def create_loadin_detail(session: Session, loading_id: int, snack_id: int):
        """Створити новий зв'язок між Loading і Snack."""
        # Перевірка, чи існує вже цей зв'язок
        existing_record = LoadinDetailDAO.get_loadin_detail_by_ids(session, loading_id, snack_id)
        if existing_record:
            return existing_record

        # Якщо такого зв'язку немає, створюємо новий
        return LoadinDetailDAO.create_loadin_detail(session, loading_id, snack_id)

    @staticmethod
    def delete_loadin_detail(session: Session, loading_id: int, snack_id: int):
        """Видалити зв'язок між Loading і Snack."""
        loadin_detail = LoadinDetailDAO.get_loadin_detail_by_ids(session, loading_id, snack_id)
        if loadin_detail:
            return LoadinDetailDAO.delete_loadin_detail(session, loading_id, snack_id)
        return None

    @staticmethod
    def get_loadings_by_snack(session: Session, snack_id: int):
        """Отримати всі записи loading для конкретного snack_id."""
        return LoadinDetailDAO.get_loadings_by_snack(session, snack_id)

    @staticmethod
    def update_loadin_detail(session: Session, loading_id: int, snack_id: int, new_data: dict):
        """Оновити дані у записі loadin_detail за loading_id та snack_id."""
        loadin_detail = LoadinDetailDAO.get_loadin_detail_by_ids(session, loading_id, snack_id)
        if loadin_detail:
            for key, value in new_data.items():
                setattr(loadin_detail, key, value)
            session.commit()
            return loadin_detail
        return None
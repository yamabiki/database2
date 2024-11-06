from my_project.auth.dao.loading_dao import LoadingDAO
from sqlalchemy.orm import Session

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

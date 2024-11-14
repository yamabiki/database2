from my_project.auth.models.loading import Loading
from my_project.auth.models.all import LoadinDetail
from sqlalchemy.orm import Session
from db_init import db

class LoadingDAO:
    @staticmethod
    def get_all_loadings(session: Session):
        return session.query(Loading).all()

    @staticmethod
    def get_loading_by_id(session: Session, loading_id: int):
        return session.query(Loading).filter(Loading.loading_id == loading_id).first()

    @staticmethod
    def create_loading(session: Session, loading_data: dict):
        new_loading = Loading(**loading_data)
        session.add(new_loading)
        session.commit()
        return new_loading

    @staticmethod
    def update_loading(session: Session, loading_id: int, updated_data: dict):
        loading = session.query(Loading).filter(Loading.loading_id == loading_id).first()
        if loading:
            for key, value in updated_data.items():
                setattr(loading, key, value)
            session.commit()
        return loading

    @staticmethod
    def delete_loading(session: Session, loading_id: int):
        loading = session.query(Loading).filter(Loading.loading_id == loading_id).first()
        if loading:
            session.delete(loading)
            session.commit()
        return loading



class LoadinDetailDAO:
    @staticmethod
    def get_all_loadin_details(session: Session):
        return session.query(LoadinDetail).all()

    @staticmethod
    def get_loadin_detail_by_id(session: Session, loading_id: int, snack_id: int):
        return session.query(LoadinDetail).filter(LoadinDetail.loading_id == loading_id, LoadinDetail.snack_id == snack_id).first()

    @staticmethod
    def get_loadings_by_snack(session: Session, snack_id: int):
        # Пошук всіх завантажень (loading), що пов'язані з певним snack_id через LoadinDetail
        return session.query(Loading).join(LoadinDetail).filter(LoadinDetail.snack_id == snack_id).all()

    @staticmethod
    def create_loadin_detail(session: Session, loadin_detail_data: dict):
        new_loadin_detail = LoadinDetail(**loadin_detail_data)
        session.add(new_loadin_detail)
        session.commit()
        return new_loadin_detail

    @staticmethod
    def update_loadin_detail(session: Session, loading_id: int, snack_id: int, updated_data: dict):
        loadin_detail = session.query(LoadinDetail).filter(LoadinDetail.loading_id == loading_id, LoadinDetail.snack_id == snack_id).first()
        if loadin_detail:
            for key, value in updated_data.items():
                setattr(loadin_detail, key, value)
            session.commit()
        return loadin_detail

    @staticmethod
    def delete_loadin_detail(session: Session, loading_id: int, snack_id: int):
        loadin_detail = session.query(LoadinDetail).filter(LoadinDetail.loading_id == loading_id, LoadinDetail.snack_id == snack_id).first()
        if loadin_detail:
            session.delete(loadin_detail)
            session.commit()
        return loadin_detail

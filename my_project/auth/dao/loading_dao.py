from my_project.auth.models.loading import Loading
from sqlalchemy.orm import Session

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

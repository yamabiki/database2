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

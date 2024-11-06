from my_project.auth.dao.technician_dao import TechnicianDAO

class TechnicianService:
    @staticmethod
    def get_all_technicians(session):
        return TechnicianDAO.get_all_technicians(session)

    @staticmethod
    def get_technician_by_id(session, technician_id):
        return TechnicianDAO.get_technician_by_id(session, technician_id)

    @staticmethod
    def create_technician(session, technician_data):
        return TechnicianDAO.create_technician(session, technician_data)

    @staticmethod
    def update_technician(session, technician_id, updated_data):
        return TechnicianDAO.update_technician(session, technician_id, updated_data)

    @staticmethod
    def delete_technician(session, technician_id):
        return TechnicianDAO.delete_technician(session, technician_id)

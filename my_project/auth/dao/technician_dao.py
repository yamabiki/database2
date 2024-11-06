from my_project.auth.models.technician import Technician

class TechnicianDAO:
    @staticmethod
    def get_all_technicians(session):
        return session.query(Technician).all()

    @staticmethod
    def get_technician_by_id(session, technician_id):
        return session.query(Technician).get(technician_id)

    @staticmethod
    def create_technician(session, technician_data):
        technician = Technician(**technician_data)
        session.add(technician)
        session.commit()
        return technician

    @staticmethod
    def update_technician(session, technician_id, updated_data):
        technician = session.query(Technician).get(technician_id)
        if technician:
            for key, value in updated_data.items():
                setattr(technician, key, value)
            session.commit()
        return technician

    @staticmethod
    def delete_technician(session, technician_id):
        technician = session.query(Technician).get(technician_id)
        if technician:
            session.delete(technician)
            session.commit()
        return technician

    @staticmethod
    def get_technicians_with_details(session):
        technicians = session.query(Technician).all()
        technicians_data = [technician.to_dict() for technician in technicians]
        return technicians_data

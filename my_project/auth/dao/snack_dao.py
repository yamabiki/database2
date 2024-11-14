from my_project.auth.models.all import Snack

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

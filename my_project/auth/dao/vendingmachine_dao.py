from my_project.auth.models.vendingmachine import VendingMachine

class VendingMachineDAO:
    @staticmethod
    def get_all_vending_machines(session):
        return session.query(VendingMachine).all()

    @staticmethod
    def get_vending_machine_by_id(session, vending_machine_id):
        return session.query(VendingMachine).get(vending_machine_id)

    @staticmethod
    def create_vending_machine(session, vending_machine_data):
        vending_machine = VendingMachine(**vending_machine_data)
        session.add(vending_machine)
        session.commit()
        return vending_machine

    @staticmethod
    def update_vending_machine(session, vending_machine_id, updated_data):
        vending_machine = session.query(VendingMachine).get(vending_machine_id)
        if vending_machine:
            for key, value in updated_data.items():
                setattr(vending_machine, key, value)
            session.commit()
        return vending_machine

    @staticmethod
    def delete_vending_machine(session, vending_machine_id):
        vending_machine = session.query(VendingMachine).get(vending_machine_id)
        if vending_machine:
            session.delete(vending_machine)
            session.commit()
        return vending_machine

    @staticmethod
    def get_vending_machines_with_details(session):
        vending_machines = session.query(VendingMachine).all()
        vending_machines_data = [vending_machine.to_dict() for vending_machine in vending_machines]
        return vending_machines_data

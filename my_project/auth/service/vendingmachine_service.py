from my_project.auth.dao.vendingmachine_dao import VendingMachineDAO
from sqlalchemy.orm import Session

class VendingMachineService:
    @staticmethod
    def get_all_vending_machines(session: Session):
        return VendingMachineDAO.get_all_vending_machines(session)

    @staticmethod
    def get_vending_machine_by_id(session: Session, vending_machine_id: int):
        return VendingMachineDAO.get_vending_machine_by_id(session, vending_machine_id)

    @staticmethod
    def create_vending_machine(session: Session, vending_machine_data: dict):
        return VendingMachineDAO.create_vending_machine(session, vending_machine_data)

    @staticmethod
    def update_vending_machine(session: Session, vending_machine_id: int, updated_data: dict):
        return VendingMachineDAO.update_vending_machine(session, vending_machine_id, updated_data)

    @staticmethod
    def delete_vending_machine(session: Session, vending_machine_id: int):
        return VendingMachineDAO.delete_vending_machine(session, vending_machine_id)

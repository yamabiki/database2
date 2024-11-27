from db_init import db
from datetime import datetime
from my_project.auth.models.all import LoadinDetail, Snack
from my_project.auth.models.technician import Technician



class Loading(db.Model):
    __tablename__ = 'loading'

    loading_id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('vending_machines.machine_id', ondelete="CASCADE"), nullable=False)
    tenchician_id = db.Column(db.Integer, db.ForeignKey('technichians.tenchician_id', ondelete="CASCADE"), nullable=False)
    loading_date = db.Column(db.String(45), nullable=True)

    # Відношення з таблицею Technician
    technician = db.relationship('Technician', back_populates='loadings')

    # Відношення з таблицею VendingMachine
    vending_machine = db.relationship('VendingMachine', back_populates='loadings')
    loadin_details = db.relationship('LoadinDetail', back_populates='loading', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Loading(loading_id={self.loading_id}, machine_id={self.machine_id}, loading_date='{self.loading_date}')>"

    def to_dict(self):
        return {
            "loading_id": self.loading_id,
            "machine_id": self.machine_id,
            "tenchician_id": self.tenchician_id,
            "loading_date": self.loading_date
        }


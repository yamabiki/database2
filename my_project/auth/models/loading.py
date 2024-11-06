from db_init import db
from datetime import datetime
from my_project.auth.models.all import Snack, VendingMachine
from my_project.auth.models.technician import Technician


class Loading(db.Model):
    __tablename__ = 'loading'

    loading_id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('vending_machines.machine_id', ondelete="CASCADE"), nullable=False)
    tenchician_id = db.Column(db.Integer, db.ForeignKey('technichians.tenchician_id', ondelete="CASCADE"), nullable=False)
    loading_date = db.Column(db.Date, nullable=True)

    technician = db.relationship('Technician', back_populates='loadings')

    vending_machine = db.relationship('VendingMachine', back_populates='loadings')

    def __repr__(self):
        return f"<Loading(loading_id={self.loading_id}, machine_id={self.machine_id}, loading_date='{self.loading_date}')>"

    def to_dict(self):
        return {
            "loading_id": self.loading_id,
            "machine_id": self.machine_id,
            "tenchician_id": self.tenchician_id,
            "loading_date": self.loading_date.isoformat() if isinstance(self.loading_date, datetime) else self.loading_date,
        }

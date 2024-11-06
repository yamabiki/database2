from db_init import db
from datetime import datetime
from my_project.auth.models.all import Snack
from my_project.auth.models.technician import Technician


class VendingMachine(db.Model):
    __tablename__ = 'vending_machines'

    machine_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adress = db.Column(db.String(45), nullable=True)
    gps_latitude = db.Column(db.Float, nullable=True)
    gps_longtitude = db.Column(db.Float, nullable=True)
    last_loaded_date = db.Column(db.Date, nullable=True)
    last_collected_date = db.Column(db.Date, nullable=True)
    collected_amount = db.Column(db.Float, nullable=True)

    # Зв'язки з Loading, CoinLoading, CoinExtraction, VendingMachineStock, Sales
    loadings = db.relationship('Loading', back_populates='vending_machine')
    coin_loadings = db.relationship('CoinLoading', back_populates='vending_machine')
    coin_extractions = db.relationship('CoinExtraction', back_populates='vending_machine')
    stocks = db.relationship('VendingMachineStock', back_populates='vending_machine')
    sales = db.relationship('Sale', back_populates='vending_machine')

    def to_dict(self):
        return {
            "machine_id": self.machine_id,
            "adress": self.adress,
            "gps_latitude": self.gps_latitude,
            "gps_longtitude": self.gps_longtitude,
            "last_loaded_date": self.last_loaded_date.isoformat() if self.last_loaded_date else None,
            "last_collected_date": self.last_collected_date.isoformat() if self.last_collected_date else None,
            "collected_amount": self.collected_amount
        }


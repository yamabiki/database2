from db_init import db

class Technician(db.Model):
    __tablename__ = 'technichians'

    tenchician_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=True)
    phone = db.Column(db.String(45), nullable=True)

    loadings = db.relationship('Loading', back_populates='technician', foreign_keys='Loading.tenchician_id', cascade="all, delete-orphan")
    coin_loadings = db.relationship('CoinLoading', back_populates='technician', foreign_keys='CoinLoading.technichian_id', cascade="all, delete-orphan")
    coin_extractions = db.relationship('CoinExtraction', back_populates='technician', foreign_keys='CoinExtraction.technichian_id', cascade="all, delete-orphan")
    vending_machines = db.relationship('TechnicianHasVendingMachine', back_populates='technician')

    def to_dict(self):
        return {
            "tenchician_id": self.tenchician_id,
            "name": self.name,
            "phone": self.phone,
            "loadings": [loading.to_dict() for loading in self.loadings],
            "coin_loadings": [coin_loading.to_dict() for coin_loading in self.coin_loadings],
            "coin_extractions": [coin_extraction.to_dict() for coin_extraction in self.coin_extractions]
        }

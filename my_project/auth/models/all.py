from db_init import db
from datetime import date

class LoadinDetail(db.Model):
    __tablename__ = 'loadin_detail'

    loading_id = db.Column(db.Integer, db.ForeignKey('loading.loading_id', ondelete="CASCADE"), primary_key=True)
    snack_id = db.Column(db.Integer, db.ForeignKey('snacks.snack_id', ondelete="CASCADE"), primary_key=True)
    snack = db.relationship('Snack', back_populates='loadin_details')
    loading = db.relationship('Loading', back_populates='loadin_details')

    def to_dict(self):
        return {
            "loading_id": self.loading_id,
            "snack_id": self.snack_id,
            "loading": self.loading.to_dict() if self.loading else None,
            "snack": self.snack.to_dict() if self.snack else None
        }

# Модель для таблиці Brand
class Brand(db.Model):
    __tablename__ = 'brand'

    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(45), nullable=True)

    # Зв'язок з Snacks
    snacks = db.relationship('Snack', back_populates='brand')

    def to_dict(self):
        return {
            "brand_id": self.brand_id,
            "brand_name": self.brand_name
        }

# Модель для таблиці Snacks
class Snack(db.Model):
    __tablename__ = 'snacks'

    snack_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.brand_id', ondelete="CASCADE"), nullable=False)

    # Зв'язок з таблицею Brand
    brand = db.relationship('Brand', back_populates='snacks')
    # Зв'язки з LoadinDetail, VendingMachineStock, Sales
    loadin_details = db.relationship('LoadinDetail', back_populates='snack')
    stocks = db.relationship('VendingMachineStock', back_populates='snack')
    sales = db.relationship('Sale', back_populates='snack')

    def to_dict(self):
        return {
            "snack_id": self.snack_id,
            "name": self.name,
            "brand_id": self.brand_id
        }

# Модель для таблиці LoadingDetail



class CoinLoading(db.Model):
    __tablename__ = 'coin_loading'

    coin_loading_id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('vending_machines.machine_id', ondelete="CASCADE"), nullable=False)
    technichian_id = db.Column(db.Integer, db.ForeignKey('technichians.tenchician_id', ondelete="CASCADE"), nullable=False)
    loading_date = db.Column(db.Date, nullable=True)
    amount = db.Column(db.Float, nullable=True)

    # Зв'язки з таблицями VendingMachine, Technician
    vending_machine = db.relationship('VendingMachine', back_populates='coin_loadings')
    technician = db.relationship('Technician', back_populates='coin_loadings')

    def to_dict(self):
        return {
            "coin_loading_id": self.coin_loading_id,
            "machine_id": self.machine_id,
            "technichian_id": self.technichian_id,
            "loading_date": self.loading_date.isoformat() if self.loading_date else None,
            "amount": self.amount
        }


# Модель для таблиці CoinExtraction
class CoinExtraction(db.Model):
    __tablename__ = 'coin_extraction'

    coin_extraction_id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('vending_machines.machine_id', ondelete="CASCADE"), nullable=False)
    technichian_id = db.Column(db.Integer, db.ForeignKey('technichians.tenchician_id', ondelete="CASCADE"), nullable=False)
    extracted_quantity = db.Column(db.Integer, nullable=True)
    collection_date = db.Column(db.Date, nullable=True)

    # Зв'язки з таблицями VendingMachine, Technician
    vending_machine = db.relationship('VendingMachine', back_populates='coin_extractions')
    technician = db.relationship('Technician', back_populates='coin_extractions')

    def to_dict(self):
        return {
            "coin_extraction_id": self.coin_extraction_id,
            "machine_id": self.machine_id,
            "technichian_id": self.technichian_id,
            "extracted_quantity": self.extracted_quantity,
            "collection_date": self.collection_date.isoformat() if self.collection_date else None
        }


# Модель для таблиці VendingMachineStock
class VendingMachineStock(db.Model):
    __tablename__ = 'vending_machine_stock'

    machine_id = db.Column(db.Integer, db.ForeignKey('vending_machines.machine_id', ondelete='CASCADE'), primary_key=True)
    snack_id = db.Column(db.Integer, db.ForeignKey('snacks.snack_id'), primary_key=True)

    vending_machine = db.relationship('VendingMachine', back_populates='stocks')
    snack = db.relationship('Snack')

    def to_dict(self):
        return {
            "machine_id": self.machine_id,
            "snack_id": self.snack_id,
        }


# Модель для таблиці Sales
class Sale(db.Model):
    __tablename__ = 'sales'

    sale_id = db.Column(db.Integer, primary_key=True)
    sale_date = db.Column(db.Date, nullable=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('vending_machines.machine_id', ondelete="CASCADE"), nullable=False)
    snack_id = db.Column(db.Integer, db.ForeignKey('snacks.snack_id', ondelete="CASCADE"), nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=True)

    # Зв'язки з таблицями VendingMachine, Snack
    vending_machine = db.relationship('VendingMachine', back_populates='sales')
    snack = db.relationship('Snack', back_populates='sales')

    def to_dict(self):
        return {
            "sale_id": self.sale_id,
            "sale_date": self.sale_date.isoformat() if self.sale_date else None,
            "machine_id": self.machine_id,
            "snack_id": self.snack_id,
            "quantity_sold": self.quantity_sold,
        }

class Promotion(db.Model):
    __tablename__ = 'promotions'

    promotion_id = db.Column(db.Integer, primary_key=True)
    snack_id = db.Column(db.Integer, nullable=False)
    promotion_details = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "promotion_id": self.promotion_id,
            "snack_id": self.snack_id,
            "promotion_details": self.promotion_details,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
        }


class TechnicianHasVendingMachine(db.Model):
    __tablename__ = 'technician_has_vending_machine'

    technician_id = db.Column(db.Integer, db.ForeignKey('technichians.tenchician_id', ondelete='CASCADE'), primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('vending_machines.machine_id', ondelete='CASCADE'), primary_key=True)

    technician = db.relationship('Technician', back_populates='vending_machines')
    vending_machine = db.relationship('VendingMachine', back_populates='technicians')

    def to_dict(self):
        return {
            "technician_id": self.technician_id,
            "machine_id": self.machine_id,
        }
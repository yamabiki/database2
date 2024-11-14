from my_project.auth.models.all import Brand

class BrandDAO:
    @staticmethod
    def get_all_brands(session):
        return session.query(Brand).all()

    @staticmethod
    def get_brand_by_id(session, brand_id):
        return session.query(Brand).get(brand_id)

    @staticmethod
    def create_brand(session, brand_data):
        brand = Brand(**brand_data)
        session.add(brand)
        session.commit()
        return brand

    @staticmethod
    def update_brand(session, brand_id, updated_data):
        brand = session.query(Brand).get(brand_id)
        if brand:
            for key, value in updated_data.items():
                setattr(brand, key, value)
            session.commit()
        return brand

    @staticmethod
    def delete_brand(session, brand_id):
        brand = session.query(Brand).get(brand_id)
        if brand:
            session.delete(brand)
            session.commit()
        return brand

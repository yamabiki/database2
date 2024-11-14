from my_project.auth.dao.brand_dao import BrandDAO

class BrandService:
    @staticmethod
    def get_all_brands(session):
        return BrandDAO.get_all_brands(session)

    @staticmethod
    def get_brand_by_id(session, brand_id):
        return BrandDAO.get_brand_by_id(session, brand_id)

    @staticmethod
    def create_brand(session, brand_data):
        return BrandDAO.create_brand(session, brand_data)

    @staticmethod
    def update_brand(session, brand_id, updated_data):
        return BrandDAO.update_brand(session, brand_id, updated_data)

    @staticmethod
    def delete_brand(session, brand_id):
        return BrandDAO.delete_brand(session, brand_id)

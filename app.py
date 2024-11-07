from flask import Flask
from db_init import db
from my_project.auth.route.loading_route import loading_bp
from my_project.auth.route.technician_route import technician_bp
from my_project.auth.route.vendingmachine_route import vending_machine_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ANDerander123!@localhost/jasper'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(loading_bp, url_prefix='/api')
app.register_blueprint(technician_bp, url_prefix='/api')
app.register_blueprint(vending_machine_bp, url_prefix='/api')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

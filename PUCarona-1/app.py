from flask import Flask
from Entities.Corrida import db
from Controllers.ControllerCorrida import corrida_controller

app = Flask(__name__)


server = 'pucarona-server.database.windows.net'
database = 'pucarona'
username = 'admin_pucarona'
password = '1234puc$'


DATABASE_URI = (
    f'mssql+pyodbc://{username}:{password}@{server}/{database}?'
    'driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=yes'
)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)


app.register_blueprint(corrida_controller)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Welcome to pucaronas"

if __name__ == '__main__':
    app.run(debug=True)
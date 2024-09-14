from Tools.scripts.make_ctype import method
from flask import Flask
from Entities.Corrida import db
from Controllers.ControllerCorrida import corrida_controller

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@127.0.0.1/pucaronas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

# Registrar o blueprint
app.register_blueprint(corrida_controller)

# Criar tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route('/' , method['GET'])
def index():
    return "Welcome to pucaronas"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from Entities.Corrida import db
from Controllers.ControllerCorrida import corrida_controller

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/pucaronas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

# Registrar o blueprint
app.register_blueprint(corrida_controller)

# Criar tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route("/")
def fuck_you():
    return "Fuck you"

if __name__ == '__main__':
    app.run(debug=True)
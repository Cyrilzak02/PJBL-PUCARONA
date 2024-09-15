from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Corrida(db.Model):
    __tablename__ = 'dbo.Corridas'

    idcorrida = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_ini = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime, nullable=False)
    end_origem = db.Column(db.String(45), nullable=False)
    end_fim = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(45), nullable=False)

    def __init__(self, data_ini, data_fim, end_origem, end_fim, status):
        self.data_ini = data_ini
        self.data_fim = data_fim
        self.end_origem = end_origem
        self.end_fim = end_fim
        self.status = status

    def __repr__(self):
        return (f"<Corrida idcorrida={self.idcorrida}, "
                f"data_ini={self.data_ini}, data_fim={self.data_fim}, "
                f"end_origem={self.end_origem}, end_fim={self.end_fim}, "
                f"status={self.status}>")
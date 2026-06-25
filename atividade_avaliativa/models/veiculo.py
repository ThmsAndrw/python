from . import db
from .base import ModeloBase


class Veiculo(ModeloBase):
    __tablename__ = "veiculos"

    # TODO ALUNO: diaria (Float)
    placa = db.Column(db.String(10), nullable=False)
    modelo = db.Column(db.String(80), nullable=False)
    diaria = db.Column(db.Float, nullable=False)

    # TODO ALUNO: relationship com Locacao
    locacoes = db.relationship("Locacao", back_populates="veiculo")

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.modelo).all()

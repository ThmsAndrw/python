from flask import Blueprint, render_template

from models import ClienteLocadora, Locacao, Veiculo


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    total_clientes = ClienteLocadora.query.count()
    total_veiculos = Veiculo.query.count()
    total_locacoes = Locacao.query.count()

    return render_template(
        "index.html",
        total_clientes=total_clientes,
        total_veiculos=total_veiculos,
        total_locacoes=total_locacoes,
    )

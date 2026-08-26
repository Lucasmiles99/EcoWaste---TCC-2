from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from database.connection import criar_tabelas

from services.empresa_service import EmpresaService
from services.ecoponto_service import EcopontoService
from services.material_service import MaterialService
from services.ecoponto_material_service import EcopontoMaterialService

app = Flask(__name__)

criar_tabelas()

empresa_service = EmpresaService()

ecoponto_service = EcopontoService()

material_service = MaterialService()

ecoponto_material_service = EcopontoMaterialService()

@app.route("/")
def inicio():
    return render_template(
        "index.html"
    )

@app.route("/empresas")
def listar_empresas():

    empresas = empresa_service.listar()

    return render_template(
        "empresas/lista.html",
        empresas=empresas
    )

@app.route(
    "/empresas/nova",
    methods=["GET", "POST"]
)
def cadastrar_empresa():

    if request.method == "POST":

        empresa_service.cadastrar(
            nome=request.form["nome"],
            cidade=request.form["cidade"],
            segmento=request.form["segmento"],
            contato=request.form["contato"]
        )

        return redirect(
            url_for("listar_empresas")
        )

    return render_template(
        "empresas/formulario.html"
    )

@app.route(
    "/empresas/<int:id>/editar",
    methods=["GET", "POST"]
)
def editar_empresa(id):

    empresa = empresa_service.buscar_por_id(id)

    if empresa is None:
        return "Empresa não encontrada.", 404

    if request.method == "POST":

        empresa_service.atualizar(
            id=id,
            nome=request.form["nome"],
            cidade=request.form["cidade"],
            segmento=request.form["segmento"],
            contato=request.form["contato"]
        )

        return redirect(
            url_for("listar_empresas")
        )

    return render_template(
        "empresas/editar.html",
        empresa=empresa
    )

@app.route(
    "/empresas/<int:id>/excluir",
    methods=["POST"]
)
def excluir_empresa(id):

    try:
        empresa_service.excluir(id)

    except ValueError:
        return "Empresa não encontrada.", 404

    return redirect(
        url_for("listar_empresas")
    )

@app.route("/ecopontos")
def listar_ecopontos():

    ecopontos = ecoponto_service.listar()

    return render_template(
        "ecopontos/lista.html",
        ecopontos=ecopontos
    )

@app.route(
    "/ecopontos/novo",
    methods=["GET"]
)
def novo_ecoponto():

    materiais = material_service.listar()

    return render_template(
        "ecopontos/formulario.html",
        materiais=materiais
    )

@app.route(
    "/ecopontos/salvar",
    methods=["POST"]
)
def salvar_ecoponto():

    nome = request.form.get("nome")

    endereco = request.form.get("endereco")

    cidade = request.form.get("cidade")

    localizacao_maps = request.form.get(
        "localizacao_maps",
        ""
    )

    imagem = request.form.get(
        "imagem",
        ""
    )

    descricao = request.form.get(
        "descricao",
        ""
    )

    try:

        ecoponto = ecoponto_service.cadastrar(
            nome=nome,
            endereco=endereco,
            cidade=cidade,
            localizacao_maps=localizacao_maps,
            imagem=imagem,
            descricao=descricao
        )

    except ValueError as erro:

        return str(erro), 400

    materiais_selecionados = request.form.getlist(
        "materiais"
    )

    for material_id in materiais_selecionados:

        ecoponto_material_service.associar(
            ecoponto.id,
            int(material_id)
        )

    return redirect(
        url_for("listar_ecopontos")
    )

@app.route(
    "/ecopontos/<int:id>"
)
def detalhes_ecoponto(id):

    try:

        ecoponto = ecoponto_service.buscar_por_id(
            id
        )

    except ValueError:

        return "Ecoponto não encontrado.", 404

    materiais = (
        ecoponto_material_service
        .listar_materiais_do_ecoponto(
            id
        )
    )

    return render_template(
        "ecopontos/detalhes.html",
        ecoponto=ecoponto,
        materiais=materiais
    )

@app.route(
    "/ecopontos/<int:id>/excluir",
    methods=["POST"]
)
def excluir_ecoponto(id):

    try:

        ecoponto_service.excluir(
            id
        )

    except ValueError:

        return "Ecoponto não encontrado.", 404

    return redirect(
        url_for("listar_ecopontos")
    )

@app.route("/materiais")
def listar_materiais():

    materiais = material_service.listar()

    return render_template(
        "materiais/lista.html",
        materiais=materiais
    )

@app.route(
    "/materiais/novo",
    methods=["GET", "POST"]
)
def cadastrar_material():

    if request.method == "POST":

        try:

            material_service.cadastrar(
                nome=request.form["nome"],
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                descricao=request.form.get(
                    "descricao",
                    ""
                )
            )

        except ValueError as erro:

            return str(erro), 400

        return redirect(
            url_for("listar_materiais")
        )

    return render_template(
        "materiais/formulario.html"
    )

@app.route(
    "/materiais/<int:id>"
)
def detalhes_material(id):

    try:

        material = material_service.buscar_por_id(
            id
        )

    except ValueError:

        return "Material não encontrado.", 404

    ecopontos = (
        ecoponto_material_service
        .listar_ecopontos_do_material(
            id
        )
    )

    return render_template(
        "materiais/detalhes.html",
        material=material,
        ecopontos=ecopontos
    )

@app.route(
    "/materiais/<int:id>/excluir",
    methods=["POST"]
)
def excluir_material(id):

    try:

        material_service.excluir(
            id
        )

    except ValueError:

        return "Material não encontrado.", 404

    return redirect(
        url_for("listar_materiais")
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )
import os
import uuid
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from werkzeug.utils import secure_filename
from database.connection import criar_tabelas

from services.empresa_service import EmpresaService
from services.ecoponto_service import EcopontoService
from services.material_service import MaterialService
from services.ecoponto_material_service import EcopontoMaterialService
from services.equipamento_service import EquipamentoService
from services.descarte_service import DescarteService
from services.checklist_service import ChecklistService

app = Flask(__name__)

criar_tabelas()

PASTA_IMAGENS_EQUIPAMENTOS = os.path.join(
    app.root_path,
    "static",
    "img",
    "equipamentos"
)

EXTENSOES_IMAGEM_PERMITIDAS = {
    "png",
    "jpg",
    "jpeg",
    "webp"
}

os.makedirs(
    PASTA_IMAGENS_EQUIPAMENTOS,
    exist_ok=True
)


def salvar_imagem_equipamento(
    arquivo
):

    if (
        arquivo is None
        or arquivo.filename == ""
    ):
        return ""

    nome_original = secure_filename(
        arquivo.filename
    )

    if "." not in nome_original:

        raise ValueError(
            "Arquivo de imagem inválido."
        )

    extensao = (
        nome_original
        .rsplit(".", 1)[1]
        .lower()
    )

    if extensao not in EXTENSOES_IMAGEM_PERMITIDAS:

        raise ValueError(
            "Formato de imagem não permitido. "
            "Utilize PNG, JPG, JPEG ou WEBP."
        )

    nome_arquivo = (
        f"{uuid.uuid4().hex}.{extensao}"
    )

    caminho_arquivo = os.path.join(
        PASTA_IMAGENS_EQUIPAMENTOS,
        nome_arquivo
    )

    arquivo.save(
        caminho_arquivo
    )

    return nome_arquivo

PASTA_IMAGENS_MATERIAIS = os.path.join(
    app.root_path,
    "static",
    "img",
    "materiais"
)

os.makedirs(
    PASTA_IMAGENS_MATERIAIS,
    exist_ok=True
)


def salvar_imagem_material(
    arquivo
):

    if (
        arquivo is None
        or arquivo.filename == ""
    ):
        return ""

    nome_original = secure_filename(
        arquivo.filename
    )

    if "." not in nome_original:

        raise ValueError(
            "Arquivo de imagem inválido."
        )

    extensao = (
        nome_original
        .rsplit(".", 1)[1]
        .lower()
    )

    if extensao not in EXTENSOES_IMAGEM_PERMITIDAS:

        raise ValueError(
            "Formato de imagem não permitido. "
            "Utilize PNG, JPG, JPEG ou WEBP."
        )

    nome_arquivo = (
        f"{uuid.uuid4().hex}.{extensao}"
    )

    caminho_arquivo = os.path.join(
        PASTA_IMAGENS_MATERIAIS,
        nome_arquivo
    )

    arquivo.save(
        caminho_arquivo
    )

    return nome_arquivo

empresa_service = EmpresaService()

ecoponto_service = EcopontoService()

material_service = MaterialService()

ecoponto_material_service = EcopontoMaterialService()

equipamento_service = EquipamentoService()

descarte_service = DescarteService()

checklist_service = ChecklistService()

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

@app.route("/equipamentos")
def listar_equipamentos():

    equipamentos = equipamento_service.listar()

    return render_template(
        "equipamentos/lista.html",
        equipamentos=equipamentos
    )

@app.route(
    "/equipamentos/novo",
    methods=["GET", "POST"]
)
def cadastrar_equipamento():

    if request.method == "POST":

        try:

            imagem_galeria = request.files.get(
                "imagem"
            )

            imagem_camera = request.files.get(
                "imagem_camera"
            )

            arquivo_imagem = None

            if (
                imagem_camera is not None
                and imagem_camera.filename != ""
            ):
                arquivo_imagem = imagem_camera

            elif (
                imagem_galeria is not None
                and imagem_galeria.filename != ""
            ):
                arquivo_imagem = imagem_galeria

            nome_imagem = (
                salvar_imagem_equipamento(
                    arquivo_imagem
                )
            )

            equipamento_service.cadastrar(
                nome=request.form["nome"],
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                marca=request.form.get(
                    "marca",
                    ""
                ),
                quantidade=request.form.get(
                    "quantidade",
                    1
                ),
                estado=request.form.get(
                    "estado",
                    ""
                ),
                imagem=nome_imagem,
                descricao=request.form.get(
                    "descricao",
                    ""
                )
            )

        except ValueError as erro:

            return str(erro), 400

        return redirect(
            url_for("listar_equipamentos")
        )

    return render_template(
        "equipamentos/formulario.html"
    )

@app.route(
    "/equipamentos/<int:id>/editar",
    methods=["GET", "POST"]
)
def editar_equipamento(id):

    try:

        equipamento = (
            equipamento_service
            .buscar_por_id(id)
        )

    except ValueError:

        return (
            "Equipamento não encontrado.",
            404
        )

    if request.method == "POST":

        try:

            imagem_galeria = (
                request.files.get(
                    "imagem"
                )
            )

            imagem_camera = (
                request.files.get(
                    "imagem_camera"
                )
            )

            arquivo_imagem = None

            if (
                imagem_camera is not None
                and imagem_camera.filename != ""
            ):

                arquivo_imagem = (
                    imagem_camera
                )

            elif (
                imagem_galeria is not None
                and imagem_galeria.filename != ""
            ):

                arquivo_imagem = (
                    imagem_galeria
                )

            if arquivo_imagem is not None:

                nome_imagem = (
                    salvar_imagem_equipamento(
                        arquivo_imagem
                    )
                )

            else:

                nome_imagem = (
                    equipamento.imagem
                )

            equipamento_service.atualizar(
                id=id,
                nome=request.form["nome"],
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                marca=request.form.get(
                    "marca",
                    ""
                ),
                quantidade=request.form.get(
                    "quantidade",
                    1
                ),
                estado=request.form.get(
                    "estado",
                    ""
                ),
                imagem=nome_imagem,
                descricao=request.form.get(
                    "descricao",
                    ""
                )
            )

        except ValueError as erro:

            return (
                str(erro),
                400
            )

        return redirect(
            url_for(
                "listar_equipamentos"
            )
        )

    return render_template(
        "equipamentos/editar.html",
        equipamento=equipamento
    )

@app.route(
    "/equipamentos/<int:id>/excluir",
    methods=["POST"]
)
def excluir_equipamento(id):

    try:

        equipamento_service.excluir(
            id
        )

    except ValueError:

        return "Equipamento não encontrado.", 404

    return redirect(
        url_for("listar_equipamentos")
    )

@app.route("/descartes")
def listar_descartes():

    descartes = descarte_service.listar_com_detalhes()

    return render_template(
        "descartes/lista.html",
        descartes=descartes
    )

@app.route(
    "/descartes/novo",
    methods=["GET", "POST"]
)
def cadastrar_descarte():

    empresas = empresa_service.listar()

    equipamentos = equipamento_service.listar()

    ecopontos = ecoponto_service.listar()

    if request.method == "POST":

        try:

            descarte_service.cadastrar(
                empresa_id=request.form.get(
                    "empresa_id"
                ),
                equipamento_id=request.form.get(
                    "equipamento_id"
                ),
                ecoponto_id=request.form.get(
                    "ecoponto_id"
                ),
                quantidade=request.form.get(
                    "quantidade",
                    1
                ),
                data_descarte=request.form.get(
                    "data_descarte",
                    ""
                ),
                status=request.form.get(
                    "status",
                    ""
                ),
                observacao=request.form.get(
                    "observacao",
                    ""
                )
            )

        except ValueError as erro:

            return str(erro), 400

        return redirect(
            url_for("listar_descartes")
        )

    return render_template(
        "descartes/formulario.html",
        empresas=empresas,
        equipamentos=equipamentos,
        ecopontos=ecopontos
    )

@app.route(
    "/descartes/<int:id>/editar",
    methods=["GET", "POST"]
)
def editar_descarte(id):

    try:

        descarte = descarte_service.buscar_por_id(
            id
        )

    except ValueError:

        return "Descarte não encontrado.", 404

    empresas = empresa_service.listar()

    equipamentos = equipamento_service.listar()

    ecopontos = ecoponto_service.listar()

    if request.method == "POST":

        try:

            descarte_service.atualizar(
                id=id,
                empresa_id=request.form.get(
                    "empresa_id"
                ),
                equipamento_id=request.form.get(
                    "equipamento_id"
                ),
                ecoponto_id=request.form.get(
                    "ecoponto_id"
                ),
                quantidade=request.form.get(
                    "quantidade",
                    1
                ),
                data_descarte=request.form.get(
                    "data_descarte",
                    ""
                ),
                status=request.form.get(
                    "status",
                    ""
                ),
                observacao=request.form.get(
                    "observacao",
                    ""
                )
            )

        except ValueError as erro:

            return str(erro), 400

        return redirect(
            url_for("listar_descartes")
        )

    return render_template(
        "descartes/editar.html",
        descarte=descarte,
        empresas=empresas,
        equipamentos=equipamentos,
        ecopontos=ecopontos
    )

@app.route(
    "/descartes/<int:id>/excluir",
    methods=["POST"]
)
def excluir_descarte(id):

    try:

        descarte_service.excluir(
            id
        )

    except ValueError:

        return "Descarte não encontrado.", 404

    return redirect(
        url_for("listar_descartes")
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

    latitude = request.form.get(
        "latitude",
        ""
    )

    longitude = request.form.get(
        "longitude",
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
            latitude=latitude,
            longitude=longitude,
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
    "/ecopontos/<int:id>/editar",
    methods=["GET", "POST"]
)
def editar_ecoponto(id):

    try:

        ecoponto = ecoponto_service.buscar_por_id(
            id
        )

    except ValueError:

        return "Ecoponto não encontrado.", 404

    materiais = material_service.listar()

    materiais_associados = (
        ecoponto_material_service
        .listar_materiais_do_ecoponto(
            id
        )
    )

    materiais_associados_ids = [
        material["id"]
        for material in materiais_associados
    ]

    if request.method == "POST":

        try:

            ecoponto_service.atualizar(
                id=id,
                nome=request.form.get(
                    "nome"
                ),
                endereco=request.form.get(
                    "endereco"
                ),
                cidade=request.form.get(
                    "cidade"
                ),
                localizacao_maps=request.form.get(
                    "localizacao_maps",
                    ""
                ),
                latitude=request.form.get(
                    "latitude",
                    ""
                ),
                longitude=request.form.get(
                    "longitude",
                    ""
                ),
                imagem=request.form.get(
                    "imagem",
                    ""
                ),
                descricao=request.form.get(
                    "descricao",
                    ""
                )
            )

            ecoponto_material_service.remover_todas_associacoes(
                id
            )

            materiais_selecionados = request.form.getlist(
                "materiais"
            )

            for material_id in materiais_selecionados:

                ecoponto_material_service.associar(
                    id,
                    int(material_id)
                )

        except ValueError as erro:

            return str(erro), 400

        return redirect(
            url_for(
                "detalhes_ecoponto",
                id=id
            )
        )

    return render_template(
        "ecopontos/editar.html",
        ecoponto=ecoponto,
        materiais=materiais,
        materiais_associados_ids=materiais_associados_ids
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

            imagem_galeria = request.files.get(
                "imagem"
            )

            imagem_camera = request.files.get(
                "imagem_camera"
            )

            arquivo_imagem = None

            if (
                imagem_camera is not None
                and imagem_camera.filename != ""
            ):

                arquivo_imagem = (
                    imagem_camera
                )

            elif (
                imagem_galeria is not None
                and imagem_galeria.filename != ""
            ):

                arquivo_imagem = (
                    imagem_galeria
                )

            nome_imagem = (
                salvar_imagem_material(
                    arquivo_imagem
                )
            )

            material_service.cadastrar(
                nome=request.form["nome"],
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                imagem=nome_imagem,
                descricao=request.form.get(
                    "descricao",
                    ""
                )
            )

        except ValueError as erro:

            return (
                str(erro),
                400
            )

        return redirect(
            url_for(
                "listar_materiais"
            )
        )

    return render_template(
        "materiais/formulario.html"
    )

@app.route(
    "/materiais/<int:id>/editar",
    methods=["GET", "POST"]
)
def editar_material(id):

    try:

        material = (
            material_service
            .buscar_por_id(id)
        )

    except ValueError:

        return (
            "Material não encontrado.",
            404
        )

    if request.method == "POST":

        try:

            imagem_galeria = request.files.get(
                "imagem"
            )

            imagem_camera = request.files.get(
                "imagem_camera"
            )

            arquivo_imagem = None

            if (
                imagem_camera is not None
                and imagem_camera.filename != ""
            ):

                arquivo_imagem = (
                    imagem_camera
                )

            elif (
                imagem_galeria is not None
                and imagem_galeria.filename != ""
            ):

                arquivo_imagem = (
                    imagem_galeria
                )

            if arquivo_imagem is not None:

                nome_imagem = (
                    salvar_imagem_material(
                        arquivo_imagem
                    )
                )

            else:

                nome_imagem = (
                    material.imagem
                )

            material_service.atualizar(
                id=id,
                nome=request.form.get(
                    "nome"
                ),
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                imagem=nome_imagem,
                descricao=request.form.get(
                    "descricao",
                    ""
                )
            )

        except ValueError as erro:

            return (
                str(erro),
                400
            )

        return redirect(
            url_for(
                "detalhes_material",
                id=id
            )
        )

    return render_template(
        "materiais/editar.html",
        material=material
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

@app.route("/checklist")
def listar_checklist():

    municipios = (
        checklist_service
        .listar_municipios()
    )

    return render_template(
        "checklist/lista.html",
        municipios=municipios
    )

@app.route(
    "/checklist/<int:municipio_id>"
)
def detalhes_checklist(
    municipio_id
):

    resultado = (
        checklist_service
        .obter_checklist_municipio(
            municipio_id
        )
    )

    if resultado is None:

        return (
            "Município não encontrado.",
            404
        )

    return render_template(
        "checklist/detalhes.html",
        municipio=resultado[
            "municipio"
        ],
        checklist=resultado[
            "checklist"
        ],
        total_perguntas=resultado[
            "total_perguntas"
        ],
        total_respondidas=resultado[
            "total_respondidas"
        ],
        percentual=resultado[
            "percentual"
        ]
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )
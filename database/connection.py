import sqlite3

def conectar():
    """
    Cria e retorna uma conexão com o banco de dados SQLite do EcoWaste.
    """

    conexao = sqlite3.connect(
        "database/ecowaste.db"
    )

    conexao.row_factory = sqlite3.Row

    conexao.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conexao

def coluna_existe(
    conexao,
    tabela,
    coluna
):
    """
    Verifica se uma coluna já existe em uma tabela.
    """

    cursor = conexao.cursor()

    cursor.execute(
        f"PRAGMA table_info({tabela})"
    )

    colunas = cursor.fetchall()

    for coluna_banco in colunas:

        if coluna_banco["name"] == coluna:
            return True

    return False

def criar_tabelas():
    """
    Cria e atualiza as tabelas necessárias
    para o funcionamento do EcoWaste.
    """

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empresa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            segmento TEXT,
            contato TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ecoponto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            cidade TEXT NOT NULL,
            localizacao_maps TEXT,
            latitude REAL,
            longitude REAL,
            imagem TEXT,
            descricao TEXT
        )
    """)

    if not coluna_existe(
        conexao,
        "ecoponto",
        "latitude"
    ):

        cursor.execute("""
            ALTER TABLE ecoponto
            ADD COLUMN latitude REAL
        """)

    if not coluna_existe(
        conexao,
        "ecoponto",
        "longitude"
    ):

        cursor.execute("""
            ALTER TABLE ecoponto
            ADD COLUMN longitude REAL
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS material (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            imagem TEXT,
            descricao TEXT
        )
    """)

    if not coluna_existe(
        conexao,
        "material",
        "imagem"
    ):

        cursor.execute("""
            ALTER TABLE material
            ADD COLUMN imagem TEXT
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ecoponto_material (
            ecoponto_id INTEGER NOT NULL,
            material_id INTEGER NOT NULL,

            PRIMARY KEY (
                ecoponto_id,
                material_id
            ),

            FOREIGN KEY (ecoponto_id)
                REFERENCES ecoponto(id)
                ON DELETE CASCADE,

            FOREIGN KEY (material_id)
                REFERENCES material(id)
                ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            marca TEXT,
            quantidade INTEGER NOT NULL DEFAULT 1,
            estado TEXT,
            imagem TEXT,
            descricao TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS descarte (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            empresa_id INTEGER NOT NULL,
            equipamento_id INTEGER NOT NULL,
            ecoponto_id INTEGER,

            quantidade INTEGER NOT NULL DEFAULT 1,
            data_descarte TEXT,
            status TEXT,
            observacao TEXT,

            FOREIGN KEY (empresa_id)
                REFERENCES empresa(id)
                ON DELETE RESTRICT,

            FOREIGN KEY (equipamento_id)
                REFERENCES equipamento(id)
                ON DELETE RESTRICT,

            FOREIGN KEY (ecoponto_id)
                REFERENCES ecoponto(id)
                ON DELETE SET NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS municipio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pergunta_checklist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER NOT NULL UNIQUE,
            texto TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resposta_checklist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            municipio_id INTEGER NOT NULL,
            pergunta_id INTEGER NOT NULL,

            resposta TEXT,

            UNIQUE (
                municipio_id,
                pergunta_id
            ),

            FOREIGN KEY (municipio_id)
                REFERENCES municipio(id)
                ON DELETE CASCADE,

            FOREIGN KEY (pergunta_id)
                REFERENCES pergunta_checklist(id)
                ON DELETE CASCADE
        )
    """)

    conexao.commit()

    conexao.close()

    print(
        "Tabelas do EcoWaste "
        "criadas/verificadas com sucesso!"
    )

if __name__ == "__main__":

    criar_tabelas()
import sqlite3

def conectar():
    """
    Cria e retorna uma conexão com o banco de dados SQLite do EcoWaste.
    """

    conexao = sqlite3.connect("database/ecowaste.db")

    conexao.row_factory = sqlite3.Row

    conexao.execute("PRAGMA foreign_keys = ON")

    return conexao

def criar_tabelas():
    """
    Cria as tabelas necessárias para o funcionamento do EcoWaste.
    As tabelas somente serão criadas caso ainda não existam.
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
            imagem TEXT,
            descricao TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS material (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            descricao TEXT
        )
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

    conexao.commit()

    conexao.close()

    print("Tabelas do EcoWaste criadas/verificadas com sucesso!")

if __name__ == "__main__":
    criar_tabelas()
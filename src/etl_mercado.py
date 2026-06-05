from sqlalchemy import create_engine

# Cria um banco de dados local chamado 'mercado_financeiro.db'
engine = create_engine('sqlite:///mercado_financeiro.db')

# Salva o DataFrame no banco. Se a tabela já existir, ele substitui (replace).
# Em um ambiente real, você faria um "append" ou "upsert", mas para a foto atual, "replace" funciona.
dados_acoes.to_sql('indicadores_acoes', con=engine, if_exists='replace', index=False)

print("Dados salvos com sucesso no banco de dados SQLite!")
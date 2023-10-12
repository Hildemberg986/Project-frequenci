def load_df() -> dict:
    # Importa a biblioteca Pandas para lidar com DataFrames
    import pandas as pd

    # Especifique o nome do arquivo da planilha
    nome_arquivo = "dados.xlsx"
    
    try:
        # Tenta ler o arquivo existente
        dados = pd.read_excel(nome_arquivo)
    except:
        # Se o arquivo não existe, cria um novo DataFrame e o salva como um arquivo Excel

        # Define um dicionário com as colunas do novo DataFrame
        data = {'Nome': [],
                'Idade': [],
                'Sex': []
                }

        # Cria um novo DataFrame a partir do dicionário
        dados = pd.DataFrame(data)

    dados = dados.fillna('-')
    # Retorna o DataFrame lido a partir do arquivo Excel (pode ser o existente ou o recém-criado)
    return dados

import pandas as pd


def edit_user(dados: dict, nome_usuario: str):
    df = pd.DataFrame(dados)

    # Localiza o índice do usuário com base no nome
    indice_usuario = df[df['Nome'] == nome_usuario].index

    # Verifica se o usuário foi encontrado
    if not indice_usuario.empty:
        print(
            f'As informações do usuário {nome_usuario} foram atualizadas com sucesso.')
    else:
        print(f'Usuário {nome_usuario} não encontrado.')

import pandas as pd

def save_new_user(dados:dict, new_user:dict):
    
    df = pd.DataFrame(dados)

    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True,  axis=0)
    
    nome_arquivo = "dados.xlsx"
    df.to_excel(nome_arquivo, index=False)

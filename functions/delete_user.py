import pandas as pd

def delete_user(dados:dict, del_id:str):
    
    df = pd.DataFrame(dados)
    
    
    linha_a_excluir = df[df['Nome'] == del_id]
    
    df = df.drop(linha_a_excluir.index)
    df.to_excel('dados.xlsx', index=False)


import pandas as pd

def save_frec(dados:dict, frec, dia):

    
    df = pd.DataFrame(dados)
    
    df[dia] = frec
    
    nome_arquivo = "dados.xlsx"
    df.to_excel(nome_arquivo, index=False)

    print(f"A planilha foi salva em '{nome_arquivo}'")

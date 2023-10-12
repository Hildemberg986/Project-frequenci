# Import function
from functions.save_frec import save_frec
from functions.save_new_user import save_new_user
from functions.delete_user import delete_user
from functions.load_df import load_df

dados = load_df()
print(dados)
new_user = {'Nome': 'Clara', 'Idade': 28, 'cidade': "caico",'Sex':'F', "altura": 1.8}
save_new_user(dados, new_user)
dados = load_df()
print(dados)

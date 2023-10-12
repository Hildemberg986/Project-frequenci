import datetime

def gerar_calendario():
    hoje = datetime.date.today()
    primeiro_dia_mes = hoje.replace(day=1)
    ultimo_dia_mes = primeiro_dia_mes.replace(day=28) + datetime.timedelta(days=4)
    ultimo_dia_mes = ultimo_dia_mes - datetime.timedelta(days=ultimo_dia_mes.day)
    return hoje, primeiro_dia_mes, ultimo_dia_mes
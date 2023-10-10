from Bot import Bot
from user_configs import dados_user

bot = Bot(
    CPF_CNPJ=dados_user['user_CPF_CNPJ'],
    SENHA=dados_user['user_senha'],
    TOMADOR_CNPJ=dados_user['tomador_cnpj'],
    LOCAL_SERVICO=dados_user['local_servico'],
    DESCRICAO_SERVICO = dados_user['descricao_servico'],
    CODIGO_TRIBUTACAO_NACIONAL=dados_user['codigo_tributacao_nacional']
    )
bot.iniciar_bot()


from Bot import Bot
from user_configs import user_CPF_CNPJ, user_senha

bot = Bot(CPF_CNPJ=user_CPF_CNPJ, SENHA=user_senha)
bot.acessar_nfse()
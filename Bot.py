from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep




class Bot:
    def __init__(self, CPF_CNPJ, SENHA):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.CPF_CNPJ = CPF_CNPJ
        self.SENHA = SENHA
        print(CPF_CNPJ, SENHA)
    
    def acessar_nfse(self):
        self.navegador.get('https://www.nfse.gov.br/EmissorNacional/Login?ReturnUrl=%2fEmissorNacional')
        sleep(2)
        input_cnpj = self.navegador.find_element(By.ID, 'Inscricao')
        input_senha = self.navegador.find_element(By.ID, 'Senha')
        
        input_cnpj.send_keys(self.CPF_CNPJ)
        sleep(1)
        input_senha.send_keys(self.SENHA)
        sleep(1)
        
        btn_entrar = self.navegador.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[1]/div/form/div[3]/button')
        btn_entrar.click()
        sleep(1)
        







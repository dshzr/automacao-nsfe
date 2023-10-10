from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from JS_actions import scrollToFinal

from selenium.webdriver.support.ui import WebDriverWait




class Bot:
    def __init__(self, CPF_CNPJ, SENHA, TOMADOR_CNPJ, LOCAL_SERVICO, CODIGO_TRIBUTACAO_NACIONAL, DESCRICAO_SERVICO):
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=self.servico)
        self.CPF_CNPJ = CPF_CNPJ
        self.SENHA = SENHA
        self.TOMADOR_CNPJ = TOMADOR_CNPJ
        self.LOCAL_SERVICO = LOCAL_SERVICO
        self.CODIGO_TRIBUTACAO_NACIONAL = CODIGO_TRIBUTACAO_NACIONAL
        self.DESCRICAO_SERVICO = DESCRICAO_SERVICO
        
    def iniciar_bot(self):
        #acessar nfse
        try: 
            self.acessar_nfse()
        except Exception as e:
            print(f'Erro ao acessar NFSE: {e}')
        else:
            print('Iniciando bot...') 
            print('Acessando NFSE...')
        
        #acessar aba pessoas
        try:
            self.aba_pessoas()
        except Exception as e:
            print(f'Erro ao acessar aba pessoas: {e}')
        else:
            print('Acessando aba pessoas...')
        
        #acessar aba servico
        try:
            self.aba_servico()
        except Exception as e:
            print(f'Erro ao acessar aba servico: {e}')
    
        
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
        sleep(2)
             
    def aba_pessoas(self):
        #card
        card_nova_nsfe = self.navegador.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[2]/a/div')
        card_nova_nsfe.click() 
        sleep(1)
        
        #botao nova nsfe completa
        btn_nsfe_completa = self.navegador.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[2]/ul/li[2]/a')
        btn_nsfe_completa.click()
        sleep(2)
        
        # selecionar a data de competencia da nota
        DataCompetencia = self.navegador.find_element(By.ID, 'DataCompetencia')  
        DataCompetencia.send_keys(datetime.now().strftime("%d/%m/%Y"))
        sleep(1)
        
        #clicar fora para selecionar a data
        text_clique_fora = self.navegador.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div/div[1]/div/div/label/span')
        text_clique_fora.click()
        sleep(2)
        
        # dar scroll ate o final da pagina
        scrollToFinal(self)
        
        # selecionar tomador do Brasil
        radio_Brasil_tomador = self.navegador.find_element(By.XPATH, '//*[@id="pnlTomador"]/div[1]/div/div/div[2]/label')
        radio_Brasil_tomador.click()
        sleep(1)
        
        #informações do tomador do serviço
        
        cpf_cnpj_tomador = self.navegador.find_element(By.ID, 'Tomador_Inscricao')
        cpf_cnpj_tomador.send_keys(self.TOMADOR_CNPJ)
        sleep(1)
        btn_pesquisar_cnpj_tomador = self.navegador.find_element(By.XPATH,'//*[@id="btn_Tomador_Inscricao_pesquisar"]/i')
        btn_pesquisar_cnpj_tomador.click()
        sleep(1)
        
         # dar scroll ate o final da pagina
        scrollToFinal(self)
        
        #ir para proxima aba
        btn_proximo = self.navegador.find_element(By.XPATH, '//*[@id="btnAvancar"]/span')
        btn_proximo.click()
        sleep(2)
        
    def aba_servico(self):
        #selecionar municipio do serviço
        drop_municipio = self.navegador.find_element(By.XPATH, '//*[@id="pnlLocalPrestacao"]/div/div/div[2]/div/span[1]/span[1]/span/span[2]')
        drop_municipio.click()
        sleep(1)
        
        search_municipio = self.navegador.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
        search_municipio.send_keys(self.LOCAL_SERVICO)
        sleep(1)
        
        # verifica qual item da lista de li's é o municipio desejado e clica nele
        itens_pesquisa = self.navegador.find_elements(By.CLASS_NAME,'select2-results__option')
        sleep(1)
        for item in itens_pesquisa:
            # clicar arrow downa te que o item seja visivel
            sleep(1)
            if item.text.lower().find(self.LOCAL_SERVICO.lower()) != -1:
                search_municipio.send_keys(Keys.ENTER)
                break
            search_municipio.send_keys(Keys.ARROW_DOWN)
        sleep(1)
        
        
        
        
        
        
        
        
        
        #selecionar o codigo de tributacao
        drop_tributacao = self.navegador.find_element(By.XPATH, '//*[@id="pnlServicoPrestado"]/div/div[1]/div/div/span[1]/span[1]/span/span[2]')
        drop_tributacao.click()
        sleep(1)
        
        search_tributacao = self.navegador.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
        search_tributacao.send_keys(self.CODIGO_TRIBUTACAO_NACIONAL)
        sleep(1)
        print('pesquisando...')
        # verifica qual item da lista de li's é o municipio desejado e clica nele
        ul = self.navegador.find_element(By.ID, 'select2-ServicoPrestado_CodigoTributacaoNacional-results')
        itens_pesquisa = ul.find_elements(By.TAG_NAME, 'li')
        
        sleep(1)
        for item in itens_pesquisa:
            sleep(1)
            if(item.text.lower().find(self.CODIGO_TRIBUTACAO_NACIONAL.lower()) != -1):
                search_tributacao.send_keys(Keys.ENTER)
                break
            search_municipio.send_keys(Keys.ARROW_DOWN)
        sleep(2)
      
        
        
        

        # O serviço prestado é um caso de: exportação, imunidade ou não incidência do ISSQN?* (NÃO)
        radio_exportacao = self.navegador.find_element(By.XPATH, '//*[@id="pnlServicoPrestado"]/div/div[2]/div/div[1]/label/span/i')
        radio_exportacao.click()
        sleep(1)
        
        #descricao do servico com a data de hoje no final formatada
        descricao_servico = self.navegador.find_element(By.ID, 'ServicoPrestado_Descricao')
        descricao_servico.send_keys(f'{self.DESCRICAO_SERVICO} - {datetime.now().strftime("%d/%m/%Y")}')
        sleep(1)
        
        scrollToFinal(self)
        
        btn_avancar_valores = self.navegador.find_element(By.XPATH, '/html/body/div[1]/form/div[7]/button/span')
        btn_avancar_valores.click()
        sleep(2)
        


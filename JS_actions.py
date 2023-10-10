from time import sleep

def scrollToFinal(self, tamanho = 1000):
    self.navegador.execute_script(f"window.scrollBy(0, {tamanho});")
    sleep(1)
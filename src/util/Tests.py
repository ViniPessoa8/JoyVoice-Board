"""
Métodos para testar outros métodos do sistema.

Métodos
-------
teste_toca_som() : void
    Reproduz o primeiro audio da lista de sons.
teste_para_som() : void
    Reproduz o primeiro áudio da lista de sons e, depois de 1 segundo, interrompe-o.
teste_remove_som() : void
    Remove o 
"""
def teste_toca_som(self): 
    self.controlador.soundboard.toca_som(0)

def teste_para_som(self):
    # Reproduz o som
    self.controlador.soundboard.toca_som(0)
    print('Esperando 1 segundo... ')
    sleep(1)
    
    # Para o som
    self.controlador.soundboard.para_som()

def teste_remove_som(self):
    self.controlador.soundboard.remove_som('com - Ratinho vinheta')


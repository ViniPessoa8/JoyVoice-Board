"""
Métodos para testar outros métodos do sistema.

Métodos
-------
teste_toca_som() : void
    Reproduz o primeiro audio da lista de sons.
teste_para_som() : void
    Reproduz o primeiro áudio da lista de sons e, depois de 1 segundo, interrompe-o.
teste_remove_som() : void
    Remove o primeiro som da lista de sons, removendo-o também do arquivo sons.json
"""
def teste_toca_som(self): 
    """
    Reproduz o primeiro audio da lista de sons.
    """
    self.controlador.soundboard.toca_som(0)

def teste_para_som(self):
    """
    Reproduz o primeiro áudio da lista de sons e, depois de 1 segundo, interrompe-o.
    """
    # Reproduz o som
    self.controlador.soundboard.toca_som(0)
    print('Esperando 1 segundo... ')
    sleep(1)
    
    # Para o som
    self.controlador.soundboard.para_som()

def teste_remove_som(self):
    """
    Remove o primeiro som da lista de sons, removendo-o também do arquivo sons.json
    """
    self.controlador.soundboard.remove_som(0)


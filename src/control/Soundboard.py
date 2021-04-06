class Soundboard:
    """
    Classe gerenciadora dos sons. Responsável por 
    ler, armazenar, reproduzir, interromper e remover os sons.
    
    Atributos
    ---------
    sons : list 
        Lista do caminho dos sons no computador.
    efeitos : list
        Lista de efeitos. 

    Métodos
    -------
    adiciona_som() : void
        Adiciona um áudio do computador, selecionado pelo usuário, e adiciona 
        na lista de áudios do programa.
    remove_som() : void
        Remove um áudiso da lista de sons do programa.
    toca_som(id) : void
        Reproduz um áudio, de acordo com o id fornecido.
    para_som() : void
        Para a reprodução do áudio em execução, se houver um.
    """

    def __init__(self):
        """
        Construtor da classe.
        """    
        self.sons    = []
        self.efeitos = []

    # Métodos #
    def adiciona_som(self):
        """
        Adiciona um áudio do computador, selecionado pelo usuário, e adiciona 
        na lista de áudios do programa.
        """
        print('adicionar_som()')

    def remove_som(self):
        """
        Remove um áudio da lista de sons do programa.
        """
        print('remover_som()')

    def toca_som(self, id):
        """
        Reproduz um áudio, de acordo com o id fornecido.

        Parâmetros
        ----------
        id : int
            Representa o ID do som a ser reproduzido. 
        """

        print('tocar_som(%d)' % id)

    def para_som(self):
        """
        Para a reprodução do áudio em execução, se houver um.
        """
        print('parar_som()')

    def main(self):
        self.adiciona_som()
        self.remove_som()
        self.toca_som(10)
        self.para_som()

# Main #
# Usada pra testar os métodos da classe
if __name__ == '__main__':
    # Instância do controlador
    soundboard = Soundboard()
    
    # Teste dos métodos do controlador
    soundboard.main()
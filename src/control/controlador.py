class Controlador:
    """
    Classe controladora do sistema. Responsável por interagir
    com as classes Model e as classes View.

    Atributos
    ---------
    volume_saida : int
        Volume que o áudio será reproduzido no microfone do usuário. 
        (O padrão é 100)
    volume_retorno : int
        Volume que o usuário escutará o audio em seu dispositivo de saída (Fone/Caixa de som). 
        (O padrão é 100)

    Métodos
    -------
    adiciona_som() : void
        Adiciona um áudio do computador, selecionado pelo usuário, e adiciona 
        na lista de áudios do programa.
    remove_som() : void
        Remove um áudio da lista de sons do programa.
    toca_som(id) : void
        Reproduz um áudio, de acordo com o id fornecido.
    para_som() : void
        Para a reprodução do áudio em execução, se houver um.
    """

    def __init__(self, v_saida=100, v_retorno=100):
        """
        Construtor da classe.

        Parâmetros
        ----------
        v_saida : int
            Volume de saída.
        v_retorno : int
            Voulme de Retorno.
        """
        self.volume_saida = v_saida
        self.volume_retorno = v_retorno

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

# Main #
# Usada pra testar os métodos da classe
if __name__ == '__main__':
    # Instância do controlador
    controlador = Controlador()
    
    # Teste dos métodos do controlador
    controlador.adiciona_som()
    controlador.remove_som()
    controlador.toca_som(10)
    controlador.para_som()
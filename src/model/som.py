class Som:
    """
    Representa a faixa de áudio selecionada pelo usuário.

    Parâmetros
    ----------
    id : int 
        Identificador único do som.
    caminho : String
        Caminho do arquivo de som, localizado no computador do usuário.
    titulo : String
        Título do som, para que o usuário possa identificá-lo.
    voulme : int
        Volume de reprodução do som. (Padrão 100)
    """
    def __init__(self, id_som, titulo, caminho):
        """
        Construtor da classe.
        """
        self.id = id_som 
        self.caminho = caminho
        self.titulo = titulo
        self.volume = 100

    def tocar(self):
        """
        Reproduz o som
        """
        print('tocar()')

    def parar(self):
        """
        Para a reprodução de todos os sons em execução.
        """
        print('parar()')

if __name__ == '__main__':
    som = Som(1, 'ratinhooo.mp3', '~/Downloads/ratinhooo.mp3')

    som.tocar()
    som.parar()
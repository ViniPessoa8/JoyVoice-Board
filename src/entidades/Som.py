class Som:
    """
    Representa a faixa de áudio selecionada pelo usuário.

    Atributos
    ----------
    id : int 
        Identificador único do som.
    caminho : String
        Caminho do arquivo de som, localizado no computador do usuário.
    titulo : String
        Título do som, para que o usuário possa identificá-lo.
    voulme : int
        Volume de reprodução do som. (O padrão é 100)

    Métodos
    -------
    retornar()
        Coleta as informações do arquivo e retorna como dicionario para armazenamento.
    tocar()
        Inicia a reprodução do som.
    parar()
        Para a reprodução de todos os sons em execução.
    """
    
    def __init__(self, id_som, titulo, caminho, volume):
        """
        Construtor da classe.
        """
        self.id = id_som 
        self.caminho = caminho
        self.titulo = titulo
        self.volume = 100

    def to_dict(self):
        """
        Coleta as informações do arquivo e retorna como dicionario para armazenamento.
        """
        json_dict = {
            "título": self.titulo,
            "caminho": self.caminho,
            "formato": self.id,
            "volume": self.volume,
        }
                
        return json_dict
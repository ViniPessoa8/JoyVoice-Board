class Efeito:
    """
    Representa os efeitos que o usuário pode utilizar em seu microfone para alterar sua voz.

    Atributos
    ---------
    id_efeito : int
        Identificador único de cada efeito.
    titulo : String
        Título do efeito, para que o usuário possa identificá-lo.
    """
    
    def __init__(self, id_efeito, titulo):
        self.id_efeito = id_efeito
        self.titulo = titulo
class Efeito:
    """
    Representa os efeitos que o usuário pode utilizar em seu microfone para alterar sua voz.

    Atributos
    ---------
    id_efeito : int
        Identificador único de cada efeito.
    titulo : String
        Título do efeito, para que o usuário possa identificá-lo.

    Métodos
    -------
    ativar()
        Ativa o efeito no microfone do usuário.
    desativar()
        Desativa o efeito no microfone do usuário.
    """

    def __init__(self, id_efeito, titulo):
        self.id_efeito = id_efeito
        self.titulo = titulo
    
    def ativar(self):
        """
        Ativa o efeito no microfone do usuário.
        """
        # IMPLEMENTAÇÂO #
        print('ativar()')

    def desativar(self):
        """
        Desativa o efeito, caso esteja ativo.
        """
        # IMPLEMENTAÇÂO #
        print('desativar()')

if __name__ == '__main__':
    efeito = Efeito(1, 'Echo')

    efeito.ativar()
    efeito.desativar() 
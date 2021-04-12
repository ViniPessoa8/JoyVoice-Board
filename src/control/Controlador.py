from .Soundboard import Soundboard
from .Soundboard import SONS_JSON

class Controlador:
    """
    Classe controladora do sistema. Responsável por interagir
    com as classes de modelo (Model) e as classes de vizualização (View).

    Atributos
    ---------
    volume_saida : int
        Volume que o áudio será reproduzido no microfone do usuário.b(O padrão é 100)
    volume_retorno : int
        Volume que o usuário escutará o audio em seu dispositivo de saída (Fone/Caixa de som). (O padrão é 100)
    soundboard : Soundboard
        Instância da classe Soundboard, responsável por gerenciar os sons do usuário.
    
    Métodos
    -------

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
        self.soundboard = Soundboard()
        # TODO #1: INSTANCIA DA PAGINA PRINCIPAL

        # DEBUG
        print('volume_saida = ', self.volume_saida)
        print('volume_retorno = ', self.volume_retorno)

    # Métodos #
    # Loop para seleção de arquivos
    def loop_selecao_arquivos(self):
        rodando = True
        while (rodando):
            # Seleciona arquivo
            caminho_arquivo = self.soundboard.seleciona_arquivo()

            # Verifica se o arquivo é válido
            if (caminho_arquivo == '' or caminho_arquivo is None or caminho_arquivo == ()):
                print('Arquivo inválido.')
            else:
                print(caminho_arquivo)

                # formata o titulo do arquivo
                titulo = caminho_arquivo.split('.')[-2]
                print(titulo)

                # Salva arquivo em sons.json
                self.soundboard.salva_som_json(titulo, caminho_arquivo)

            # Verifica fim do loop
            while (True):
                # Lẽ a resposta
                resposta = input('\nDeseja adicionar outro arquivo?(S/N)')
    
                # Verifica a resposta
                if (resposta == 'N' or resposta == 'n'):
                    rodando = False
                    break
                elif (resposta == 'S' or resposta == 's'):
                    rodando = True
                    break
                else:
                    print('Resposta inválida. Tente novamente.')

    def alterar_volume(self, alt_volume_saida, alt_volume_retorno):
        self.m_volume_de_saida = alt_volume_saida
        self.m_volume_de_retorno = alt_volume_retorno   
        print('alteração de volume {} {}.'.format(self.m_volume_de_retorno, self.m_volume_de_saida))

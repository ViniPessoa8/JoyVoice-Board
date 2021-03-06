from .Soundboard import Soundboard
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import util.Util as Util
import os

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
        # TODO #1: Prepara pastas e arquivos
        
        # Criação das pastas do projeto
        self.cria_pastas_projeto()

        # Instancía variáveis
        self.volume_saida = v_saida
        self.volume_retorno = v_retorno
        self.soundboard = Soundboard()
       
        # TODO #2: INSTANCIA DA PAGINA PRINCIPAL

        # DEBUG
        print('volume_saida = ', self.volume_saida)
        print('volume_retorno = ', self.volume_retorno)

    # Métodos #
    # Loop para seleção de arquivos
    def loop_selecao_arquivos(self):
        rodando = True
        while (rodando):
            # Seleciona arquivo
            caminho_arquivo = self.seleciona_arquivo()

            # Verifica se o arquivo é válido
            if (caminho_arquivo == '' or caminho_arquivo is None or caminho_arquivo == ()):
                print('Arquivo inválido.')
            else:
                print(caminho_arquivo)

                # formata o titulo do arquivo
                titulo = caminho_arquivo.split('.')[-2]
                print(titulo)

                # Salva arquivo em sons.json
                Util.salva_som_json(titulo, caminho_arquivo)

            # Verifica fim do loop
            while (True):
                # Lẽ a resposta
                resposta = input('\nDeseja adicionar outro arquivo?(S/N)\n')
    
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

    # Métodos #

    # Métodos Úteis #

    def seleciona_arquivo(self):
        """
        Abre uma caixa de diálogo do sistema para que o usuário possa selecionar
        um arquivo do seu próprio computador.
        Os arquivos aceitos são: .mp3 e .wav
        """
        Tk().withdraw() # Faz o programa abrir em modo janela.
        caminho_arquivo = askopenfilename(initialdir='~/Music', filetypes=[('Audio', '*.mp3 *.wav')]) # Abre a caixa de diálogo no diretório '~/Music' 
        if (caminho_arquivo is not None):
            print(caminho_arquivo)
            return caminho_arquivo
        else:
            return ''

    

    def cria_pastas_projeto(self):

        # data/
        if (not os.path.exists(Util.DATA_DIR)):
            print('Diretório ' + Util.DATA_DIR + ' não existe. Criando...')
            os.mkdir(Util.DATA_DIR)

        # tmp_audio/
        if (not os.path.exists(Util.TMP_AUDIO_DIR)):
            print('Diretório ' + Util.TMP_AUDIO_DIR + ' não existe. Criando...')
            os.mkdir(Util.TMP_AUDIO_DIR)

        # data/sons.json
        if (not os.path.exists(Util.SONS_JSON)):
            print('Diretório ' + Util.SONS_JSON + ' não existe. Criando...')
            # Configura a estrutura inicial do json
            dados_iniciais = {
                'sons': [],
            }
            
            # Cria o arquivo 'sons.json' com o registro escrito nele.
            Util.cria_arquivo_json('sons', dados_iniciais)

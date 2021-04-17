from .Soundboard import Soundboard
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

    def alterar_volume(self, alt_volume_saida, alt_volume_retorno):
        self.m_volume_de_saida = alt_volume_saida
        self.m_volume_de_retorno = alt_volume_retorno   
        print('alteração de volume {} {}.'.format(self.m_volume_de_retorno, self.m_volume_de_saida))

    # Métodos #

    # Métodos Úteis #

    def seleciona_arquivo(self): # TODO: Mover para Controlador.py
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

    def formata_pra_wav(self, som): # TODO: Mover para Controlador.py
        """
        Converte um arquivo para o formato WAV, utilizando o método `export`
        da biblioteca pydub. 
        `Documentação do método export <https://github.com/jiaaro/pydub/blob/master/API.markdown#audiosegmentexport>`_

        Parametros
        -----------
        som : Som
            Instância da classe Som. Referente ao audio que será convertido.
        """
        # Preparação dos dados
        formato = som.caminho.split('.')[-1]

        try:
            with open(som.caminho, 'rb') as f:
                # Carrega o audio
                audio = AudioSegment.from_file(f, format=formato)
                # Formata o caminho do arquivo
                caminho_arquivo = './data/tmp_audio/' + som.titulo + '.wav'

                # Checa se o arquivo .wav já existe, senão o cria.
                if (not os.path.exists(caminho_arquivo)):
                    # Usa o método export da classe pydub para converter o arquivo
                    audio.export(caminho_arquivo, format='wav')
                    
                # retorna o caminho do novo arquivo .wav criado
                return caminho_arquivo

        except FileNotFoundError:
            print('Arquivo não encontrado. Veririfque o caminho do som \''+som.titulo+'\'.')

    def cria_pastas_projeto(self): # TODO: Mover para Controlador.py

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
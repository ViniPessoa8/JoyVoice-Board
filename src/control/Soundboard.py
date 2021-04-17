import simpleaudio as sa
from pydub import AudioSegment
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from model.Som import Som
import util.Util as Util
import os



class Soundboard:
    """
    Classe gerenciadora dos sons. Responsável por 
    ler, armazenar, reproduzir, interromper e remover os sons.

    Utiliza a biblioteca simpleaudio para a manipulação dos áudios.
    
    Atributos
    ---------
    sons : list 
        Lista do caminho dos sons no computador.

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

    Métodos Úteis
    -------------
    carrega_sons() : void
        Função para carregar os sons a partir do arquivo sons.json,
        salvando os dados na variável 'sons' como instâncias da classe Som.
    seleciona_arquivo() : void
        Abre uma caixa de diálogo do sistema para que o usuário possa selecionar
        um arquivo do seu próprio computador.
        Os arquivos aceitos são: .mp3 e .wav
    cria_arquivo_json(nome, data) : void
        Cria um arquivo <nome>.json no diretório 'data/', contendo <data>.
    salva_som_json(titulo, caminho) : void
        Salva o registro de um som, localizado no computador do usuário, contendo 
        o caminho do arquivo, um nome identificador e o formato do arquivo.
    checa_registro_json(registro, caminho_json) : Bool
        Chega se um <registro> já está no arquivo <caminho_json>.

    """

    def __init__(self):
        """
        Construtor da classe.
        """    
        # Inicialização de variáveis
        self.sons    = []

        # Criação das pastas do projeto
        self.cria_pastas_projeto()
        
        # Carregamento dos sons listados no arquivo 'sons.json'
        self.carrega_sons()

    # Métodos #
    def adiciona_som(self, titulo, caminho):
        """
        Adiciona um áudio do computador, selecionado pelo usuário, e adiciona 
        na lista de áudios do programa.
        Parâmetros
        ----------
        titulo : str
            Título identificador do arquivo.
        caminho : str
            Caminho do arquivo no computador do usuário.
        """
        self.salva_som_json(titulo, caminho)

    def remove_som(self, titulo):
        """
        Remove um áudio da lista de sons do programa.
        """
        print('remover_som()')

        # Remove o som da lista interna.
        for som in self.sons:
            print(som)
            print('\''+som.titulo + '\'', '==', '\''+titulo + '\'')
            if (som.titulo == titulo):
                print('Remove:', som)
                self.sons.remove(som)
                print(self.sons)

        # TODO: Reescreve o arquivo sons.json com a nova lista
        Util.escreve_em_json(Util.SONS_JSON, self.sons)

    def toca_som(self, id):
        """
        Reproduz um áudio, de acordo com o id fornecido.

        Parametros
        ----------
        id : int
            Representa o ID do som a ser reproduzido. 
        """
        print('tocar_som(%d)' % id)

        # Prepara os dados
        som = self.sons[id]
        caminho = som.caminho 
        formato = caminho.split('.')[-1]
        volume = str(som.volume)

        # Imprime informações sobre o som no console
        print('Som({}, {}, {}, {}'.format(som.titulo, caminho, formato, volume))

        # Trata formato: se for mp3, converte para wav.
        if (formato != 'wav'):
            # Salva o caminho do arquivo wav
            novo_caminho = self.formata_pra_wav(som=som)
            if (novo_caminho is not None):
                caminho = novo_caminho
                
        # Abre o arquivo e executa
        try:
            with open(caminho, 'rb') as f:
                # Carrega audio
                arq_wave = sa.WaveObject.from_wave_file(f)

                # Reproduz o audio 
                print('[Tocando {}]'.format(caminho))
                play_obj = arq_wave.play()
                # play_obj.wait_done() # Aguarda o fim do áudio


        except FileNotFoundError:
            print('Arquivo não encontrado. Veririfque o caminho do som \''+som.titulo+'\'.')

    def para_som(self):
        """
        Para a reprodução do áudio em execução, se houver um.
        """
        print('para_som()')

        sa.stop_all()

    def carrega_sons(self):
        """
        Função para carregar os sons a partir do arquivo sons.json,
        salvando os dados na variável 'sons' como instâncias da classe Som.
        """
        # Lê os dados do arquivo sons.json
        dados_json = Util.le_arquivo_json(Util.SONS_JSON)

        # Checa se os dados foram lidos corretamente
        if dados_json is not None:
            # Transforma os dicionarios em instâncias da classe Som
            for som in dados_json['sons']:
                # Cria a instância da classe Som
                som = Som(id_som=0, titulo=som['titulo'], caminho=som['caminho'], volume=som['volume'])
                # Adiciona a instância à lista de sons.
                self.sons.append(som)
        else :
            print('Soundboard: carrega_sons(): Erro na leitura dos dados do arquivo sons.json')

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

    # Main #
    # Usada pra testar os métodos da classe
    def main(self):
        self.carregar_sons()
        # caminho = self.seleciona_arquivo()
        # print('CAMINHO:', caminho)
        # if (caminho is not None and caminho != () ):
        #     self.adiciona_som('cavalo', caminho)
        # else:
        #     print('Caminho inválido.')
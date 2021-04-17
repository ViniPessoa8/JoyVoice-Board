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

    def remove_som(self):
        """
        Remove um áudio da lista de sons do programa.
        """
        print('remover_som()')

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
            # TODO: checar se há dados
            if len(dados_json) != 0:
                
                # Transforma os dicionarios em instâncias da classe Som
                for som in dados_json['sons']:
                    # Cria a instância da classe Som
                    som = Som(id_som=0, titulo=som['titulo'], caminho=som['caminho'], volume=som['volume'])
                    # Adiciona a instância à lista de sons.
                    self.sons.append(som)
            else:
                print('Arquivo vazio.')
        else :
            print('Soundboard: carrega_sons(): Erro na leitura dos dados do arquivo sons.json')

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
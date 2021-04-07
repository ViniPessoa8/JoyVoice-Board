from pydub import AudioSegment
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import json
import os

SONS_JSON = './data/sons.json'

class Soundboard:
    """
    Classe gerenciadora dos sons. Responsável por 
    ler, armazenar, reproduzir, interromper e remover os sons.
    
    Atributos
    ---------
    sons : list 
        Lista do caminho dos sons no computador.
    efeitos : list
        Lista de efeitos. 

    Métodos
    -------
    adiciona_som() : void
        Adiciona um áudio do computador, selecionado pelo usuário, e adiciona 
        na lista de áudios do programa.
    remove_som() : void
        Remove um áudiso da lista de sons do programa.
    toca_som(id) : void
        Reproduz um áudio, de acordo com o id fornecido.
    para_som() : void
        Para a reprodução do áudio em execução, se houver um.
    """

    def __init__(self):
        """
        Construtor da classe.
        """    
        self.sons    = []
        self.efeitos = []

    # Métodos #
    def adiciona_som(self, titulo, caminho):
        """
        Adiciona um áudio do computador, selecionado pelo usuário, e adiciona 
        na lista de áudios do programa.
        """
        formato = caminho.split('.')[-1] # Do nome do arquivo, salva-se o formato.
        # if (formato == 'mp3'):
            # som = AudioSegment.from_mp3(caminho)
        # elif (formato == 'wav'):
            # som = AudioSegment.from_wav(caminho)

        self.salva_som_json(titulo, caminho)

        print('adicionar_som({})'.format(caminho))

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

    def seleciona_arquivo(self):
        Tk().withdraw() # Faz o programa abrir em modo janela.
        caminho_arquivo = askopenfilename(initialdir='~/Music', filetypes=[('Audio', '*.mp3 *.wav')])
        if (caminho_arquivo is not None):
            print(caminho_arquivo)
            return caminho_arquivo
        else:
            return ''

    def salva_som_json(self, titulo, caminho):
        # Estrutura os dados
        formato = caminho.split('.')[-1]
        data = {
            'titulo' : titulo,
            'caminho': caminho,
            'formato': formato,
        }

        # Abre o arquivo de audios em formato JSON
        if (os.path.exists(SONS_JSON)):
            with open(SONS_JSON, 'a+') as arquivo:
                print('ARQUIVO ABERTO:', SONS_JSON)
                arquivo_json = json.loads(arquivo.read())

                # self.checa_registro_json(data, SONS_JSON)
                json.dump(data, arquivo)
                arquivo.write('\n')
        else:
            dados_iniciais = {
                'sons': [],
            }

            dados_iniciais['sons'].append(data)
            with open(SONS_JSON, 'x') as arquivo:
                json.dump(dados_iniciais, arquivo)
                arquivo.write('\n')

    def checa_registro_json(self, registro, caminho_json):
        with open(caminho_json) as arquivo:
            print('caminho json:', caminho_json)
            print('arquivo:\n', arquivo.read())

            arq_json = json.load(arquivo)

    # Main #
    # Usada pra testar os métodos da classe
    def main(self):
        caminho = self.seleciona_arquivo()
        self.adiciona_som('cavalo', caminho)


if __name__ == '__main__':
    # Instância do controlador
    soundboard = Soundboard()
    
    # Chama a função 'main' do soundboard
    soundboard.main()
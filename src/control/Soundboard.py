import simpleaudio
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from model.Som import Som
import json
import os

# Constantes
DATA_DIR = './data/'
SONS_JSON = './data/sons.json'

class Soundboard:
    """
    Classe gerenciadora dos sons. Responsável por 
    ler, armazenar, reproduzir, interromper e remover os sons.
    
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
        Remove um áudiso da lista de sons do programa.
    toca_som(id) : void
        Reproduz um áudio, de acordo com o id fornecido.
    para_som() : void
        Para a reprodução do áudio em execução, se houver um.
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
        self.sons    = []

        # Cria arquivo de sons: sons.json. (Se ainda não existir)
        if (not os.path.exists(SONS_JSON)):
            # Configura a estrutura inicial do json
            dados_iniciais = {
                'sons': [],
            }
            
            # Cria o arquivo 'sons.json' com o registro escrito nele.
            self.cria_arquivo_json('sons', dados_iniciais)
        
        # Carrega sons do arquivo 'sons.json'
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
        print('tocar_som(%d)' % id)
        """
        Reproduz um áudio, de acordo com o id fornecido.

        Parâmetros
        ----------
        id : int
            Representa o ID do som a ser reproduzido. 
        """
        # Prepara os dados
        som = self.sons[id]
        caminho = som.caminho 
        formato = caminho.split('.')[-1]
        volume = str(som.volume)

        # Imprime informações sobre o som no console
        print('formato = ', formato)
        print('[Arquivo:', som.titulo + ']')
        print('[volume=', volume + ']')

        # Abre o arquivo e executa
        try:
            with open(caminho, 'rb') as f:
                # Carrega audio
                audio = AudioSegment.from_file(f, format=formato, parameters=['-vol', volume])
                # Reproduz o audio com o método 'play' da bibiloteca pydub. 
                print('[tocando]')
                play(audio)
        except FileNotFoundError:
            print('Arquivo não encontrado. Veririfque o caminho do som \''+som.titulo+'\'.')

    def para_som(self):
        """
        Para a reprodução do áudio em execução, se houver um.
        """
        print('parar_som()')

    def carrega_sons(self):
        """
        Função para carregar os sons a partir do arquivo sons.json,
        salvando os dados na variável 'sons' como instâncias da classe Som.
        """
        # Carrega o arquivo sons.json no modo leitura (r)
        with open(SONS_JSON, 'r') as f:
            # Extrai o dicionáro do arquivo sons.json
            dados_json = json.load(f)

        # Transforma os dicionarios em instâncias da classe Som
        for som in dados_json['sons']:
            # Cria a instância da classe Som
            som = Som(id_som=0, titulo=som['titulo'], caminho=som['caminho'], volume=som['volume'])
            # Adiciona a instância à lista de sons.
            self.sons.append(som)

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

    def cria_arquivo_json(self, nome, data):
        """ 
        Cria um arquivo <nome>.json no diretório 'data/', contendo <data>.
        Parâmetros
        ----------
        nome: str
            Nome do arquivo a ser criado.
        data: dict
            Dicionário de dados a serem escritos no arquivo criado. Os dados são 
            escritos com a função json.dump(), por isso deve-se fornecer um dicionário
            neste parâmetro.
        """
        caminho = DATA_DIR + nome + '.json' # caminho do arquivo
        with open(caminho, 'x') as arquivo:
            json.dump(data, arquivo, indent=2)

    def salva_som_json(self, titulo, caminho, volume=100):
        """
        Registra um arquivo de som na lista em 'sons.json'.
        Parâmetros
        ----------
        titulo : str
            Título identificador do arquivo.
        caminho : str
            Caminho do arquivo no computador do usuário.
        volume : int
            Volume de reprodução do áudio. 
            Vai de 0 à 200, sendo 100 o volume normal e 200 o volume amplificado.
            (Valor padrão: 100)
        """
        # Estruturação dos dados
        formato = caminho.split('.')[-1]
        data = {
            'titulo' : titulo,
            'caminho': caminho,
            'formato': formato,
            'volume' : volume,
        }

        # Verifica se o arquivo 'sons.json' existe
        if (os.path.exists(SONS_JSON)):
            # Verifica se os dados já existem no arquivo 'sons.json'
            if (not self.checa_registro_json(data, SONS_JSON)):
                # Se não existirem, abre o arquivo para leitura (r)
                with open(SONS_JSON, 'r') as f:
                    # Carrega os dados na variavel 'dados'
                    dados = json.load(f)
                    # Adiciona o novo registro à lista de registros
                    dados['sons'].append(data)
                    # Print de debug
                    print(dados)
                
                # Se os dados não forem nulos 
                if (dados is not None):
                    # Abre o arquivo para escrita, apagando o que tinha antes (w)
                    with open(SONS_JSON, 'w') as f:
                        # Escreve os novos dados no arquivo
                        json.dump(dados, f, indent=2)

        # Se o arquivo 'sons.json' NÃO existe
        else:
            print('ERRO: Arquivo \'sons.json\' não encontrado.')

    def checa_registro_json(self, registro, caminho_json):
        """
        Checa se um <registro> já está no arquivo <caminho_json>.
        Parâmetros
        ----------
        registro : dict
            Dicionário contendo o registro a ser checado.
            Espera-se o formato:
            {
                'titulo' : <str> ,
                'caminho': <str> ,
                'formato': <str> ,
                'volume' : <int> ,
            }
        caminho_json : str
            Caminho do arquivo onde será procurado o registro.
        """
        # Carrega o arquivo em modo leitura (r)
        with open(caminho_json, 'r') as arquivo:
            print('arquivo aberto:', caminho_json)
            dados = json.loads(arquivo.read()) 
            
            # Para cada registro
            for reg in dados['sons']:
                # Verifica se há chaves iguais entre o registro novo e os já existentes.
                if (reg['caminho'] == registro['caminho']):
                    print('Registro já existe.')
                    return True
        
        print('Registro não existe')
        return False

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
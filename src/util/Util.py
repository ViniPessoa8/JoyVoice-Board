from pydub import AudioSegment
import json
import os

# Constantes
DATA_DIR      = './data/'
SONS_JSON     = './data/sons.json'
TMP_AUDIO_DIR = './data/tmp_audio/'

def cria_arquivo_json(nome, data):
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

def salva_som_json(titulo, caminho, volume=100):
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
        if (not checa_registro_json(data, SONS_JSON)):
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
                escreve_em_json(SONS_JSON, dados)

    # Se o arquivo 'sons.json' NÃO existe
    else:
        print('ERRO: Arquivo \'sons.json\' não encontrado.')

def checa_registro_json(registro, caminho_json):

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
    
def le_arquivo_json(caminho):
    """
    Dado o <caminho> do arquivo, tenta ler seu conteúdo como JSON. 
    Se conseguir, retorna o conteúdo em forma de dicionário. 
    """
    # Carrega o arquivo sons.json no modo leitura (r)
    try:
        with open(caminho, 'r') as f:
            # Extrai o dicionáro do arquivo sons.json
            dados_json = json.load(f)
            # Retorna os dados
            return dados_json
    # Caso o arquivo não seja encontrado
    except FileNotFoundError as e:
        print('[ERRO] Util: le_arquivo_json(): Arquivo não encontrado:', e)

    return None

def formata_pra_wav(som):
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
def escreve_em_json(arq, dados):
    """
    Reescreve um arquivo .json com os dados fornecidos.

    Parametros
    ----------
    arq : str
        Caminho do arquivo a ser reescrito.
    dados : dict
        Dicionário contendo os dados a serem escritos no arquivo.
    """
    print('escreve_em_json()')
    # Checa se os dados são válidos
    if (dados is not None and dados != {} and dados != []):
        # Abre o arquivo para escrita
        try:
            with open(arq, 'w') as f:
                # Ecreve os dados no arquivo
                json.dump(dados, f, indent=2)        
        except FileNotFoundError as e:
            print('[ERRO] Util: escreve_em(): Arquivo não encontrado.\n' + e)

engine = create_engine('sqlite:///imoveis.db')

class Imovel:
  def __init__(self, id, logradouro, numero, cep):
    #...

def converte_dict_para_imovel(linha):
  d = dict (linha)
  return Imovel (**d)
  # Você viu esta sintaxe com ** em LP2, né?
  # Se você não lembra, ele vai pegar o dicionario d e transformá-lo
  # em uma lista de parâmetros. Se as chaves do dicionario forem as mesmas
  # que estão no parametros do construtor, isso dará certo. Mas se forem
  # diferentes ou se houverem chaves a mais ou a menos, não vai dar certo.

def pesquisar (nome_rua):
  with engine.connect() as con:
    lista = []
    sql = text("SELECT id, logradouro, numero, cep FROM imoveis WHERE logradouro = :logradouro")
    rs = con.execute(sql)
    for linha in rows:
                d = {
                    'id': linha['id'],
                    'logradouro': linha['logradouro'],
                    'numero': linha['numero'],
                    'cep': linha['cep']
                }
      lista.append(converte_dict_para_imovel(linha))
    return lista
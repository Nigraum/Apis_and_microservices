# Cria um dicionário sem informação alguma
agenda = {}

# Para inserir tem que ser apresentado chave e valor
agenda["maria"] = 9912312
agenda["joao"] = 1231245
agenda["chave"] = "valor"

print(agenda)

# Consulta apenas com chave
print(agenda["maria"])

# Verificar se a chave existe no dicionario
print("maria" in agenda)
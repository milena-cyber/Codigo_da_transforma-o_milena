

arquivo = open("informacoes.txt", "w")

arquivo.write("Nome: Milena\n")
arquivo.write("Idade: 17\n")

arquivo.close()


arquivo = open("informacoes.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()
import shutil

# Arquivo de origem
origem = "informacoes.txt"

# Pasta de destino
destino = "backup_informacoes.txt"

# Faz a cópia
shutil.copy(origem, destino)

print("Backup realizado com sucesso!")
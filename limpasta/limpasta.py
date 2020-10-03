import sys, os, datetime, shutil
from datetime import timedelta

baseDir = sys.argv[1]
dirs = os.listdir(baseDir)

for dir in dirs:
    caminhoObj = baseDir + "\\" + dir
    
    if os.path.isdir(caminhoObj):
        dataAtual = datetime.date.today()
        dataExpiracao = dataAtual - timedelta(days=7)
        dataCriacao = datetime.date.fromtimestamp(os.path.getctime(caminhoObj))

        if dataCriacao < dataExpiracao:
            print(f"Pasta: {caminhoObj}, criada em {dataCriacao}, sendo {dataExpiracao} a data de corte")
            shutil.rmtree(os.path.abspath(caminhoObj), ignore_errors=True)

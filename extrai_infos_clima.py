import os
import shutil
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
key = '9RBJEGX3C8PFMZBQDZP3QDD6K'

#passando as informacoes para a url
URL = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
          f"{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv")

#extraindo os dados em csv com pandas e mostrando as 5 primeiras linhas no terminal
dados = pd.read_csv(URL)
print(dados.head())




#Definir o diretório para salvar os arquivos e criar uma pasta
file_path = f"/home/dressasys/DataPipeline/semana={data_inicio}/"


# Verificar se o diretório já existe
if os.path.exists(file_path):
    # Se existe, exclua-o e todo o seu conteúdo
    shutil.rmtree(file_path)
    
# Agora, crie o diretório novamente
os.mkdir(file_path)


#salvar os arquivos em CSV
dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime','tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
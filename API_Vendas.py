import pandas as pd
from flask import Flask

app = Flask(__name__)

tabela = pd.read_csv('criando API no Python.csv')
print(tabela)

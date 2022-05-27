import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def homepage():
    tabela = pd.read_csv('criando API no Python.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


app.run(host='0.0.0.0')

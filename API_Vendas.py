import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def homepage():
    tabela = pd.read_csv('criando API no Python.csv')
    total_vendas = tabela['Vendas'].sum()
    total_vendas_tv = tabela['TV'].sum()
    total_vendas_radio = tabela['Radio'].sum()
    total_vendas_jornal = tabela['Jornal'].sum()
    resposta = {'total_vendas': total_vendas}, {
        'total_vendas_tv': total_vendas_tv}, {'total_vendas_radio': total_vendas_radio}, {'total_vendas_jornal': total_vendas_jornal}
    return jsonify(resposta)


app.run(host='0.0.0.0')

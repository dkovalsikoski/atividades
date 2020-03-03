from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def home():
    title = "Atividades Complementares"
    lista = ['Oficina Git e Github', 'Semana Acadêmica de ADS', 'Semana Acadêmica da Matemática']
    return render_template('index.html', titulo=title, eventos=lista)

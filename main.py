# filepath: /MysterySolver/MysterySolver/main.py

# This file is the main entry point of the application. It will likely contain the application logic and initialization code.

from flask import Flask, render_template, request, jsonify
from google import genai  # Importa o SDK da API Gemini
from google.genai import types

# Inicializa o cliente da API Gemini
client = genai.Client(api_key="")

app = Flask(__name__)

# -----------------------------------------------
# Rota principal para renderizar a página inicial
# -----------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# -----------------------------------------------
# Rota para processar comandos enviados pelo usuário
# -----------------------------------------------
@app.route('/api/command', methods=['POST'])
def handle_command():
    command = request.json.get('command', '').strip().lower()
    response = process_command(command)
    return jsonify({'response': response})

# -----------------------------------------------
# Função para processar os comandos do usuário
# -----------------------------------------------
def process_command(command):
    # Configurações do modelo Gemini
    config = types.GenerateContentConfig(
        max_output_tokens=200,
        temperature=0.7,
        system_instruction="Você é um assistente útil para um jogo de detetive. Responda em português."
    )

    # Gera a resposta usando a API Gemini
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[f"Comando: {command}"],
            config=config
        )
        return response.text
    except Exception as e:
        # Retorna uma mensagem de erro caso a API falhe
        return f"Erro ao processar o comando: {str(e)}"

# -----------------------------------------------
# Inicialização do servidor Flask
# -----------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
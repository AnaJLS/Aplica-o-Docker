import os
import json
import glob
from flask import Flask, jsonify, abort

app = Flask(__name__)

# Lê pasta de resultados via variável de ambiente
PASTA_RESULTADOS = os.environ.get("PASTA_RESULTADOS", "/dados/resultados")
APP_PORT = int(os.environ.get("APP_PORT", 5000))

def carregar_resultado(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return jsonify({
        "servico": "API de Resultados - Caminhos em Ilhas",
        "endpoints": ["/resultados", "/resultados/<nome_ilha>", "/saude"]
    })

@app.route("/saude")
def saude():
    return jsonify({"status": "ok"})

@app.route("/resultados")
def listar_resultados():
    arquivos = glob.glob(os.path.join(PASTA_RESULTADOS, "*.json"))
    if not arquivos:
        return jsonify({"aviso": "Nenhum resultado encontrado ainda.", "dica": "Execute o serviço 'app' primeiro."}), 404

    dados = []
    for arq in arquivos:
        try:
            conteudo = carregar_resultado(arq)
            if isinstance(conteudo, list):
                dados.extend(conteudo)
            else:
                dados.append(conteudo)
        except Exception as e:
            dados.append({"arquivo": arq, "erro": str(e)})

    # Remove duplicatas por ilha
    vistos = set()
    unicos = []
    for item in dados:
        chave = item.get("ilha", "")
        if chave not in vistos:
            vistos.add(chave)
            unicos.append(item)

    return jsonify(unicos)

@app.route("/resultados/<nome_ilha>")
def resultado_ilha(nome_ilha):
    # Aceita "Ilha_1", "ilha_1", "Ilha 1"
    nome_busca = nome_ilha.replace("_", " ").title()
    arquivos = glob.glob(os.path.join(PASTA_RESULTADOS, "*.json"))

    for arq in arquivos:
        try:
            conteudo = carregar_resultado(arq)
            if isinstance(conteudo, list):
                for item in conteudo:
                    if item.get("ilha", "").lower() == nome_busca.lower():
                        return jsonify(item)
            elif conteudo.get("ilha", "").lower() == nome_busca.lower():
                return jsonify(conteudo)
        except Exception:
            continue

    abort(404, description=f"Ilha '{nome_busca}' não encontrada.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT, debug=False)

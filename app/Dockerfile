# Imagem base leve com Python
FROM python:3.11-slim

# Define diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o código-fonte para dentro da imagem
COPY caminhos.py .

# Variáveis de ambiente com valores padrão
# (podem ser sobrescritas pelo docker-compose.yml)
ENV ILHA_ALVO=todas
ENV PASTA_SAIDA=/dados/resultados
ENV RANDOM_SEED=42

# Comando padrão ao iniciar o contêiner
CMD ["python", "caminhos.py"]

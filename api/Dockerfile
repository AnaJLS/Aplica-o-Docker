FROM python:3.11-slim

WORKDIR /api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py .

# Variáveis com padrão
ENV PASTA_RESULTADOS=/dados/resultados
ENV APP_PORT=5000

EXPOSE 5000

CMD ["python", "api.py"]

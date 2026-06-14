FROM nginx:alpine

# Copia configuração customizada
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copia o frontend estático
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

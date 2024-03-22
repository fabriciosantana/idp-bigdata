FROM python:3.8-slim

ENV FLASK_APP=app.py

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia o restante dos arquivos da aplicação
COPY . .

# Define a porta em que a aplicação será executada
EXPOSE 5000

# Define o comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--debug"]
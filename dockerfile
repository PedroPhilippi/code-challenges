FROM python:3.10-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

#define o diretório projeto
WORKDIR /meltano_project

#passa projeto para o container
COPY . /meltano_project

RUN pip install --upgrade pip && pip install meltano

WORKDIR /meltano_project/meltano/meltano_northwind

RUN meltano install

#diretório para saida das informações
RUN mkdir -p /data/postgres/orders

EXPOSE 5000


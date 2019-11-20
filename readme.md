[![Build Status](https://travis-ci.org/gbbocchini/challengeMet.svg?branch=master)](https://travis-ci.org/gbbocchini/challengeMet)


# Challenge
API RESTFUL com Swagger, feita em Flask e library Flask-RestPlus. Endpoints buscam dados meteorologicos observados e 
previsoes advindas de arquivos ```.CSV``` fornecidos.

## Implementações: 
Clássica (server) e Serverless (AWS Lambda, AWS S3, AWS API Gateway,  AWS CloudWatch, AWS CloudFormation).


## Estrutura do projeto
Projeto em Flask lendo informaçoes da memoria. Como as informaçoes sao lidas diretamente de arquivos CSVs optei por uma pasta "data" com todos os arquivos CSV (fonte dos dados/"bd"), uma pasta ```repository``` apenas com objetos que fazem acesso e leitura de dados (todo e qualquer acesso aos arquivos CSV e feito somente atraves das funçoes contidas em ```repository```). 

Na pasta ```business``` encontram-se todas as regras e exceções do app. As views contidas em ```app.py``` só funcionam através dos métodos contidos em business (controlers). A pasta ```helpers``` contem funções de ajuda aos métodos contidos em ```business```. 

A opçao de nao haver models formalmente tambem foi feita por questao de tempo para entrega deste desafio e tambem devido a excelente capacidade do Python em lidar com tabelas/arquivos ```.csv``` puros. As views, controlers e repo sao testados atraves dos arquivos: ```business_test.py``` e ```repo_test.py``` no mesmo diretorio de app.py


## Execuçao local

- Clone este repositorio (```git clone ...```);
- Crie um Virtual Env em Python (```python3 -m venv venv```) e ative-o (```source venv/bin/activate```);
- Instale os requisitos necessarios para o projeto (```pip install -r requirements.txt```);
- Dentro do folder clonado: ```python app.py```
- Pronto!

Uma versao live podera ser encontrada em: https://somarapi.herokuapp.com/

Um versão "serverless" feita com o framework https://serverless.com/ pode ser encontrada em: https://blpru37i9e.execute-api.us-east-1.amazonaws.com/dev 

(Uma alternativa serverless mais leve e baseada em Python seria a library ZAPPA: https://github.com/Miserlou/Zappa)


## Testes

Os testes podem ser rodados com ```pytest -v``` dentro do folder clonado. Este repo esta integrado com TravisCI.

# beer-model

## Introdução

Este repositório realiza duas entregas:

1. Treinamento de um modelo de predição de IBU utilizando Jupyter Notebook que se encontra na pasta `notebooks`
2. Imagem Docker que implementa uma API desenvolvida em FastAPI para a produtização do modelo treinado.

## Treinamento do Modelo

As explicações necessárias estão no próprio notebook do treinamento.

## FastAPI

Para testes locais, idealmente seria criado um arquivo `.env` com as variáveis de ambiente para desenvolvimento, mas para fins de demonstração deve-se renomear o arquivo `.env.example` para `.env`:

```
git clone https://github.com/amenegola/beer-model.git
cd beer-model/
mv .env.example .env
```

Instale os pacotes necessários em um ambiente virtual apropriado:

```
pip install -r requirements.txt
```

### Teste da API sem docker

Execute o servidor web com o comando

```
uvicorn --host 0.0.0.0 --port 8000 app.main:app
```

### Teste da API com docker

Com Docker instalado

```
./build_image.sh
./run_docker.sh
```

### Teste da API 

Acesse `localhost:8000/docs` no Chrome para testar a API. Um grande benefício do FastAPI, além de ser mais rápido, e além de realizar checagem nos dados de entrada, é que a documentação é criada automaticamente, tanto para referência como para testes. Ao acessar a rota de documentação mencionada, a seguinte página é disponibilizada:

<img src="https://i.imgur.com/uDlYeF4.png">

Para autorizar a execução da rota de predição, clique no botão `Authorize` e adicione a chave de API `134740f4-1c3c-4dba-ad02-875809d2bf0b`

Após, clique na rota de predição, altere o JSON de exemplo conforme necessário,e clique no botão executar.

### Considerações do deploy da API

Possuindo uma infraestrutura Kubernetes, em conjunto com Harness, a automação deste repositório para criação de endpoint seria bastante simplificada. Com o endpoint em mãos, um trigger no bucket com os dados limpos vindos do Firehose poderia fazer uma Lambda chamar o endpoint do modelo, retornando o valor do IBU.

Não queria subir um Kubernetes para este desafio, portanto parti para uma alternativa mencionada que é utilizar o Serverless Framework.

Portanto, comecei a aprender sobre Serveless Framework, imaginando que conseguiria realizar o deploy do modelo utilizando função Lambda. Foi só quando ia colocar em produção, que descobri que a função Lambda possui limite de tamanho de 250MB com as dependências, e que apenas a biblioteca do XGBoost era 350MB. O arquivo `serverless.yml` ainda se encontra neste repositório para referência. Note que eu realizar tentativas de diminuir o tamanho das dependências utilizando `serverless-python-requirements`. Outra questão é que Cloud Functions da GCP possui um gerenciamento mais facilitado de dependências Python, podendo instalar bibliotecas como XGBoost, portanto talvez com GCP dê para realizar deploy de modelos utilizando Serverless Framework. Vou realizar testes.

Eu venho de nuvens GCP e Azure, portanto parti para soluções de deploy gerenciado de containers. Encontrei Elastic Beanstalk e ECS, tentei realizar deploy utilizando essas soluções, mas não consegui terminar a tempo, pois estes recursos parecem ser bastante versáteis, mas a utilização não é tão facilitada como nas nuvens concorrentes (por exemplo Cloud Run/App Engine da GCP e App Engine da Azure).

### Testes

Este repositório passou em todos os testes (flake8, testes de chamada da API, bandit e pep8), para executar basta ter tox instalado e executar

```
tox
```

na raiz do repositório.

### Referências

O repositório com a implementação da arquitetura com Terraform se encontra [neste link](https://github.com/amenegola/ml-platform-challenge).
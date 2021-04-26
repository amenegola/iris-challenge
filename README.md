# iris-challenge

## Introdução

Este repositório cria uma imagem Docker que expõe um serviço FastAPI que carrega um modelo treinado do Google Cloud Storage e o disponibiliza para predição.

## Treinamento do Modelo

As explicações necessárias estão no próprio notebook do treinamento.

## FastAPI

Para testes locais, idealmente seria criado um arquivo `.env` com as variáveis de ambiente para desenvolvimento, mas para fins de demonstração deve-se renomear o arquivo `.env.example` para `.env`:

```
git clone https://github.com/amenegola/iris-challenge.git
cd iris-challenge/
mv .env.example .env
```

Instale os pacotes necessários em um ambiente virtual apropriado:

```
pip install -r requirements.txt
```

### API local sem docker

Execute o servidor web com o comando

```
uvicorn --host 0.0.0.0 --port 8000 app.main:app
```

### Criação da Imagem Docker (Obrigatório)

Com Docker instalado

O script `build_image.sh` cria uma imagem docker local, e faz push desta imagem para o Google Cloud Registry (GCR). Esta etapa é importante para colocar este modelo em produção, conforme repositório [iris-achirtecture](https://github.com/amenegola/iris-architecture)

### API local com docker

O script `run_docker.sh` roda o container criado com a imagem na etapa obrigatória em porta local, com as credenciais de usuário.

### Teste da API local

Acesse `localhost:8000/docs` no Chrome para testar a API. Um grande benefício do FastAPI, além de ser mais rápido, e além de realizar checagem nos dados de entrada, é que a documentação é criada automaticamente, tanto para referência como para testes rápidos. Ao acessar a rota de documentação mencionada, a seguinte página é disponibilizada:

<img src="https://i.imgur.com/WY9vbtw.png">

É necessário autorizar a execução da rota de predição, clique no botão `Authorize` e adicione a chave de API `134740f4-1c3c-4dba-ad02-875809d2bf0b`

Após, clique na rota de predição, altere o JSON de exemplo conforme necessário, e clique no botão executar.

### Deploy da API

A arquitetura para deploy do modelo foi criada utilizando Terraform para a criação de duas soluções, uma mais simples e outra mais robusta, com recursos Cloud Run, e Kubernetes, respectivamente. O Deploy foi realizado na Google Cloud Platform.

As explicações de como realizar deploy do modelo, assim como os links para teste, estão no README do repositório [iris-architecture](https://github.com/amenegola/iris-architecture). O repositório _iris-architecture_ faz parte da solução deste desafio.

### Testes de Qualidade

Este repositório passou nos seguintes testes: flake8, testes de chamada da API, bandit e pep8. Para executar basta ter tox instalado e executar

```
tox
```

na raiz do repositório.

### Referências

- O repositório com a implementação da arquitetura com Terraform se encontra [neste link](https://github.com/amenegola/iris-architecture)
- API_KEY=134740f4-1c3c-4dba-ad02-875809d2bf0b
- [FastAPI + Cloud Run](https://iris-model-nqsfhkuvaq-uc.a.run.app/docs)
- [FastAPI + GKE](http://104.198.132.8:8000/docs)

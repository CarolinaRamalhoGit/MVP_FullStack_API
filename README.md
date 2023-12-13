# MVP Full Stack - Back-End (API)
## 1. Introdução

Este projeto é parte do MVP - _Minimum Viable Product_ - da _Sprint_ **Desenvolvimento _Full Stack_ Básico** do Curso de Engenharia de Software da PUC-Rio. O MVP é composto de um Back-End, com banco de dados, e de um Front-End. Neste repositório encontra-se a parte do Back-end da aplicação. A parte do front-end pode ser acessada em [MVP_FullStack_Front-End](https://github.com/CarolinaRamalhoGit/MVP_FullStack_Frontend).

>O projeto desenvolvido objetiva a facilitação de controle de datas de vencimento de produtos de um *Minimercado Autônomo*. Este tipo de empreendimento, que ganhou força durante a pandemia de Covid-19, é uma loja de conveniências, sem funcionários, disponibilizadas em sua maior parte dentro de condomínios residenciais.

Devido ao seu baixo custo de implantação, este nicho de mercado atraiu pequenos empreendedores e vem apresentando um grande crescimento tanto em número de unidades instaladas quanto em número de franqueadoras que oferecem um grande suporte para o funcionamento dos mesmos, incluindo a solução tecnológica que possibilita a gestão de inventário e os meios de pagamentos, via totens de autoatendimento.

Uma das dores, contudo, encontradas pelos pequenos, e muitas vezes inexperientes, empreendedores é o controle da validade dos produtos ofertados, funcionalidade não disponível em algumas das principais soluções deste nicho de negócio.

>Desta forma, este projeto visa, de forma bastante simplificada, implementar um banco de dados no qual seja possível consultar uma lista dos produtos com suas respectivas quantidades e datas de validade, para que, de posse desta informação, os produtos possam ser substituídos na loja e novas compras de seu estoque possam ser providenciadas. Além da consulta, é possível a inserção de novos itens e a exclusão de itens existentes.
  
  
## 2. Back-end
O back-end da aplicação é responsável pela criação e manutenção do banco de dados da aplicação, bem como pelas rotas de requisição ao servidor. As rotas implementadas foram do tipo GET, POST e DELETE, e sua documentação pode ser acessada em Swagger, conforme instruções do item 4 do presente documento.

O back-end está organizado da seguinte forma:

- app.py *(onde estão definidas as rotas de requisição)*
- model:
    - __ init __.py *(responsável pela criação do banco de dados)*
    - base.py *(responsável pela criação de uma super classe com modelo em SQLAlchemy)*
    - produto.py *(responsável por criar a classe produto)*
- schemas:
    - __ init __.py *(responsável por importar os schemas criados nos arquivos error.py e produto.py)*
    - error.py *(define como uma mensagem de erro será representada)*
    - produto.py *(define os schemas que serão utilizados nas rotas de requisição)*
- requirements.txt *(contém as bibliotecas a serem instaladas, conforme instruções do item 4 do presente documento)*


## 3. Pré-Requisitos
- Recomenda-se o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

- Faz-se necessária a instalação de todas as dependências/bibliotecas listadas no arquivo requirements.txt:
```
    (env)$ pip install -r requirements.txt
```


## 4. Como executar
- Para processar a API e consultar sua documentação em Swagger, executar:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```
- Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.


## 5. Considerações
Por se tratar de um MVP, diversas funcionalidades da API não foram priorizadas neste momento, ficando sua implementação para as versões futuras da aplicação. Dentre as já mapeadas, destacam-se as listadas a seguir:

- Rota GET para a ordenação do banco de dados (por nome ou validade);
- Rota GET para busca de produtos por nome, para que um mesmo produto com diferentes datas de vencimento (validade) sejam vistos simultaneamente de forma clara;
- Rota PUT para a edição de produtos exitentes no banco (quantidade e/ou validade).
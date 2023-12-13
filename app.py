from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from model import Session, Produto
from schemas import *
from flask_cors import CORS

# Configuração da aplicação
info = Info(title="MVP_CGR_API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definição das Tags
home_tag = Tag(name="Documentação", description="Documentação em Swagger")
produto_tag = Tag(
    name="Produto", description="Visualização, inserção e remoção de produtos")

# Rota de Redirecionamento à raiz da documentação


@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para a tela inicial da documentação em Swagger.
    """
    return redirect('/openapi/swagger')


# Rota de Adição de Produto
@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo Produto à base de dados.
    Retorna uma representação do produto.
    """
    produto = Produto(
        nome=form.nome,
        quantidade=form.quantidade,
        validade=form.validade)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(produto)
        # efetivando o comando de adição de novo item na tabela
        session.commit()
        return apresenta_produto(produto), 200
    except Exception as e:
        # caso ocorra um erro fora do previsto
        print(e)
        error_msg = "Não foi possível salvar novo item."
        return {"mesage": error_msg}, 400


# Rota de Remoção de Produto
@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDeleteSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaIdSchema):
    """Deleta um Produto a partir do ID do produto informado.
    Retorna uma mensagem de confirmação da remoção.
    """
    try:
        produto_id = query.dict().get("id")
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        produto = session.query(Produto).filter(
            Produto.id == produto_id).first()
        if not produto:
            # se o produto não for encontrado:
            return {"mesage": "Produto não Encontrado!"}, 404

        # Salvando os dados do produto, antes de excluí-lo:
        produto_data = {
            "id": produto.id,
            "nome": produto.nome,
            "validade": produto.validade.strftime("%d/%m/%Y")
        }

        # Fazendo a remoção:
        count = session.query(Produto).filter(
            Produto.id == produto_id).delete()

        # Commit para efetivar a atualização no banco
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            return {"mesage": "Produto removido!", "Produto": produto_data}
        else:
            # se o produto não foi encontrado
            error_msg = "Produto não encontrado na base"
            return {"mesage": error_msg}, 404

    except Exception as e:
        print(e)
        return {"mesage": "Erro interno ao excluir o produto."}, 500


# Rota de Busca de Produtos cadastrados
@app.get('/lista_produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_lista_produtos():
    """Faz a busca por todos os Produtos cadastrados.
    Retorna uma representação da listagem de produtos.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    lista_produtos = session.query(Produto).all()

    if not lista_produtos:
        # se não há produtos cadastrados
        return {"Não há produtos cadastrados": []}, 200
    else:
        # retorna a representação de produto
        print(lista_produtos)
        return apresenta_lista_produtos(lista_produtos), 200


# Rota de busca de Produto por ID
@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaIdSchema):
    """Faz a busca por um Produto a partir do id do produto.
    Retorna uma representação do produto.
    """
    produto_id = query.id
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    produto = session.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base."
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação de produto
        return apresenta_produto(produto), 200
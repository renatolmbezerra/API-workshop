from typing import List, Dict
from fastapi import HTTPException

class Produtos:
    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone", 
            "descricao": "Smartphone com tela de 6 polegadas e 128GB de armazenamento.",
            "preco": 1999.99,
            "disponivel": True,
            "categoria": "eletronicos",
        },
        {
            "id": 2,
            "nome": "Notebook", 
            "descricao": "Um computador portátil com 16GB de RAM e 512GB de SSD.",
            "preco": 4999.99,
            "disponivel": False,
            "categoria": "eletronicos",
        },
        {
            "id": 3,
            "nome": "Cadeira Gamer", 
            "descricao": "Cadeira ergonômica para jogos com apoio para os braços.",
            "preco": 899.99,
            "disponivel": True,
            "categoria": "moveis",
        },
        {
            "id": 4,
            "nome": "Monitor", 
            "descricao": "Monitor de 27 polegadas com resolução 4K.",
            "preco": 2499.99,
            "disponivel": True,
            "categoria": "eletronicos",
        },
    ]


    def listar_produtos(self):
        """
        Função que retorna uma lista de produtos.
        :return: Lista de produtos.
        """
        return self.produtos
    
    def obter_produto(self, produto_id):
        """
        Função que retorna um produto específico com base no ID.
        :param produto_id: ID do produto a ser retornado.
        :return: Produto correspondente ao ID fornecido.
        """
        for produto in self.produtos:
            if produto["id"] == produto_id:
                return produto
        raise HTTPException(status_code=404, detail="Produto não encontrado")  
    
    def criar_produto(self, produto):
        """
        Função que cria um novo produto.
        :param produto: Produto a ser criado.
        :return: Produto criado.
        """
        novo_produto = produto.dict()
        novo_produto["id"] = len(self.produtos) + 1
        self.produtos.append(novo_produto)
        return novo_produto
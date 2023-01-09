def payload_post_livros():
    return {
        "nome": "Teste livro",
        "autor": "Pano Tech",
        "dataPublicacao": "2022-12-18",
        "qtdePaginas": 200
    }


def payload_patch_livros():
    return {
        "nome": "nome atualizado somente"
    }


def payload_put_livros():
    return {
        "nome": "nome atualizado",
        "autor": "autor atualizado",
        "dataPublicacao": "2022-12-22",
        "qtdePaginas": 250
    }
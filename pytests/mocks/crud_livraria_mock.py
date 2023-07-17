import uuid
import random
from faker import Faker

def payload_post_livros():
    return {
        "nome": f"{Faker().name()} {uuid.uuid4()}",
        "autor": Faker().name(),
        "dataPublicacao": "2022-12-18",
        "qtdePaginas": int(( ''.join(random.choice("123456789") for i in range(3)) ))
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
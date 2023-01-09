import json
from pytests.support.hooks import *
from pytests.mocks.crud_livraria_mock import *
from pytests.clients.livraria_api_client import LivrariaClient
from pytests.support.api_utils import ApiUtils


@pytest.mark.crud_livros
def test_post_livros():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.post_livros(payload)
    LivrariaClient.validate_response(response, 201)


@pytest.mark.crud_livros
def test_get_all_livros():
    response = LivrariaClient.get_livros()
    LivrariaClient.validate_response(response, 200)


@pytest.mark.crud_livros
def test_get_livros_id():
    response = LivrariaClient.get_livros_id()
    LivrariaClient.validate_response(response, 200)


@pytest.mark.crud_livros
def teste_patch_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.post_livros(payload)
    LivrariaClient.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    payload = payload_patch_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.patch_livros_id(id, payload)
    LivrariaClient.validate_response(response, 200)


@pytest.mark.crud_livros
def teste_put_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.post_livros(payload)
    LivrariaClient.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    payload = payload_put_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.put_livros_id(id, payload)
    LivrariaClient.validate_response(response, 200)


@pytest.mark.crud_livros
def teste_delete_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.post_livros(payload)
    LivrariaClient.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    response = LivrariaClient.delete_livros_id(id)
    LivrariaClient.validate_response(response, 200)

import json
from pytests.support.hooks import *
from pytests.mocks.crud_livraria_mock import *
from pytests.clients.livraria_api_client import LivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.examples.examples_test_crud_livraria import *
from pytests.clients.common import Common
from pytests.schemas.contract_api import *
from pytests.support.db.postgre_utils import PostgreUtils


@pytest.mark.crud_livros
def test_post_livros():
    payload = payload_post_livros()
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.post_livros(payload)
    resp_parse = LivrariaClient.validate_response(response, 201)
    ApiUtils.validate_json_schema(response, post_api_livraria)
    params = {
        "host": f"{os.environ['db_host']}",
        "port": os.environ['db_port'],
        "database": f"{os.environ['db_name']}",
        "user": f"{os.environ['db_user']}",
        "password": f"{os.environ['db_pass']}"
    }
    query = f"SELECT id, nome, autor, data_publicacao, qtde_paginas, created_on, update_at FROM public.livros where id = {resp_parse['id']};"
    connection = PostgreUtils.connection_postgre(params)
    response_query = PostgreUtils.query_postgre(connection, query)
    LivrariaClient.validate_query(resp_parse, response_query)

@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", examples_post_livros)
def test_invalid_values_post_livros(field, value, code):
    payload = payload_post_livros()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse_log(payload)
    response = LivrariaClient.post_livros(payload)
    LivrariaClient.validate_response(response, code)


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

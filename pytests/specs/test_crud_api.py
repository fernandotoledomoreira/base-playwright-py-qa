from pytests.support.hooks import *
from pytests.mocks.test_mock import *
from pytests.clients.smocking_api_client import SmockingApi
from pytests.support.api_utils import ApiUtils
from pytests.examples.examples_test_post_create_qa import *
from pytests.clients.common import Common
from pytests.schemas.post_create_qa_schema import *


# Descrição dos testes com pytest

@pytest.mark.journey
def test_post_create_qa():
    payload = payload_post()
    ApiUtils.payload_parse_log(payload)
    headers = SmockingApi.common_headers()
    ApiUtils.header_parse_log(headers)
    response = SmockingApi.post_create_qa(payload, headers)
    SmockingApi.validate_response(response, 201)
    ApiUtils.validate_json_schema(response, post_create_qa_schema)


# Descrição dos testes com pytest
@pytest.mark.prl
@pytest.mark.parametrize("payload, code", examples_post_create_qa_invalid_payload)
def test_post_create_qa_invalid_payload(payload, code):
    payload = Common.incorrect_payloads(payload)
    ApiUtils.payload_parse_log(payload)
    headers = SmockingApi.common_headers()
    ApiUtils.header_parse_log(headers)
    response = SmockingApi.post_create_qa(payload, headers)
    SmockingApi.validate_response(response, code)


# Descrição dos testes com pytest
@pytest.mark.prl
@pytest.mark.parametrize("header, value, code", examples_post_create_qa_invalid_headers)
def test_post_create_qa_invalid_headers(header, value, code):
    payload = payload_post()
    ApiUtils.payload_parse_log(payload)
    common_header = SmockingApi.common_headers()
    headers = Common.change_headers(None, common_header, header, value)
    ApiUtils.header_parse_log(headers)
    response = SmockingApi.post_create_qa(payload, headers)
    SmockingApi.validate_response(response, code)


# Descrição dos testes com pytest com exemplos
@pytest.mark.prl
@pytest.mark.parametrize("header, code", examples_post_create_qa_no_headers)
def test_post_create_qa_no_headers(header, code):
    payload = payload_post()
    ApiUtils.payload_parse_log(payload)
    common_header = SmockingApi.common_headers()
    headers = Common.delete_header(None, common_header, header)
    ApiUtils.header_parse_log(headers)
    response = SmockingApi.post_create_qa(payload, headers)
    SmockingApi.validate_response(response, code)


# Descrição dos testes com pytest com exemplos
@pytest.mark.prl
@pytest.mark.parametrize("field, value, code", examples_post_create_qa)
def test_post_create_qa_invalid_fields(field, value, code):
    payload = payload_post()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse_log(payload)
    headers = SmockingApi.common_headers()
    response = SmockingApi.post_create_qa(payload, headers)
    SmockingApi.validate_response(response, code)


# Descrição dos testes com pytest com exemplos
@pytest.mark.prl
@pytest.mark.parametrize("field, code", examples_post_create_qa_no_fields)
def test_post_create_qa_no_fields(field, code):
    payload = payload_post()
    payload = Common.remove_fields_payload(payload, field)
    ApiUtils.payload_parse_log(payload)
    headers = SmockingApi.common_headers()
    response = SmockingApi.post_create_qa(payload, headers)
    SmockingApi.validate_response(response, code)

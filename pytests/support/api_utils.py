from pytests.support.hooks import *
from jsonschema import validate
import json


class ApiUtils:

    # Método para validação de sttuso code
    @staticmethod
    def validate_status_code(request, code):
        try:
            LOG.log_info(f"Status code Esperado: {code}")
            LOG.log_info(f"Status code Recebido: {request['code']}")
            assert request['code'] == code
        except Exception as e:
            LOG.log_error("Codes divergentes")
            raise e

    # Método para realizar parse de request
    @staticmethod
    def request_parse_log(request):
        if "{" in request['body']:
            load = json.loads(request['body'])
            resp = json.dumps(load, indent=1, ensure_ascii=False)
            LOG.log_info(f"Response:\n{resp}")
            return load
        else:
            LOG.log_info(f"Response:\n{request['body']}")
            return request['body']

    # Método para realizar parse de payload
    @staticmethod
    def payload_parse_log(payload):
        resp = json.dumps(payload, indent=1, ensure_ascii=False)
        LOG.log_info(f"Payload:\n{resp}")

    # Método para realizar parse de headers
    @staticmethod
    def header_parse_log(header):
        resp = json.dumps(header, indent=1, ensure_ascii=False)
        LOG.log_info(f"Headers:\n{resp}")

    # Método para validar json schema
    @staticmethod
    def validate_json_schema(respnse, schema):
        try:
            response_json = json.loads(respnse['body'])
            validate(instance=response_json, schema=schema)
            LOG.log_info("Contrato validado com sucesso")
        except Exception as e:
            LOG.log_error("Erro ao validar o contrato")
            raise e
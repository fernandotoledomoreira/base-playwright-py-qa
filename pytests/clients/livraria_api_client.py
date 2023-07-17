from playwright.sync_api import sync_playwright
from pytests.support.hooks import *
from pytests.support.api_utils import ApiUtils


class LivrariaClient:
    @staticmethod
    def post_livros(payload):
        with sync_playwright() as p:
            uri_api = f"{os.environ['uri_api']}:{os.environ['api_port']}/livros"

            context = p.request.new_context()
            response = context.post(uri_api, data=payload)
            LOG.log_info("POST")
            LOG.log_info(f"URL: {uri_api}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def get_livros():
        with sync_playwright() as p:
            uri_api = f"{os.environ['uri_api']}:{os.environ['api_port']}/livros"

            context = p.request.new_context()
            response = context.get(uri_api)
            LOG.log_info("GET")
            LOG.log_info(f"URL: {uri_api}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def get_livros_id():
        with sync_playwright() as p:
            uri_api = f"{os.environ['uri_api']}:{os.environ['api_port']}/livros/1"

            context = p.request.new_context()
            response = context.get(uri_api)
            LOG.log_info("GET")
            LOG.log_info("URL: {uri_api}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def patch_livros_id(id, payload):
        with sync_playwright() as p:
            uri_api = f"{os.environ['uri_api']}:{os.environ['api_port']}/livros/{id}"
            
            context = p.request.new_context()
            response = context.patch(uri_api, data=payload)
            LOG.log_info("PATCH")
            LOG.log_info(f"URL: {uri_api}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def put_livros_id(id, payload):
        with sync_playwright() as p:
            uri_api = f"{os.environ['uri_api']}:{os.environ['api_port']}/livros/{id}"

            context = p.request.new_context()
            response = context.put(uri_api, data=payload)
            LOG.log_info("PUT")
            LOG.log_info(f"URL: {uri_api}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def delete_livros_id(id):
        with sync_playwright() as p:
            uri_api = f"{os.environ['uri_api']}:{os.environ['api_port']}/livros/{id}"

            context = p.request.new_context()
            response = context.delete(uri_api)
            LOG.log_info("DELETE")
            LOG.log_info(f"URL: {uri_api}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def validate_response(response, code):
        resp = ApiUtils.request_parse_log(response)
        ApiUtils.validate_status_code(response, code)
        return resp
    
    @staticmethod
    def validate_query(response, query_response):
        assert query_response[0]['id'] == response['id']
        assert query_response[0]['nome'] == response['nome']
        assert query_response[0]['autor'] == response['autor']
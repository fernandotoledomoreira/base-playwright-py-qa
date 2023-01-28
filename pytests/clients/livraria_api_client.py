from playwright.sync_api import sync_playwright
from pytests.support.hooks import *
from pytests.support.api_utils import ApiUtils


class LivrariaClient:
    @staticmethod
    def post_livros(payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.post("http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros", data=payload)
            LOG.log_info("POST")
            LOG.log_info("URL: http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def get_livros():
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.get("http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros")
            LOG.log_info("GET")
            LOG.log_info("URL: http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def get_livros_id():
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.get("http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/1")
            LOG.log_info("GET")
            LOG.log_info("URL: http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/1")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def patch_livros_id(id, payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.patch(f"http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/{id}", data=payload)
            LOG.log_info("PATCH")
            LOG.log_info(f"URL: http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/{id}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def put_livros_id(id, payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.put(f"http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/{id}", data=payload)
            LOG.log_info("PUT")
            LOG.log_info(f"URL: http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/{id}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def delete_livros_id(id):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.delete(f"http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/{id}")
            LOG.log_info("DELETE")
            LOG.log_info(f"URL: http://ec2-44-201-222-218.compute-1.amazonaws.com:3000/livros/{id}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def validate_response(response, code):
        ApiUtils.request_parse_log(response)
        ApiUtils.validate_status_code(response, code)

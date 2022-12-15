from playwright.sync_api import sync_playwright
from pytests.support.hooks import *
from pytests.support.api_utils import ApiUtils


class SmockingApi:

    # Método para declaração de header em comum
    @staticmethod
    def common_headers():
        headers = {
            "Content-Type": "application/json",
            "Authorization": os.environ['auth_create_qa_smockin']
        }
        return headers

    # Método para realização de requisição POST com Playwright
    @staticmethod
    def post_create_qa(payload, headers):
        with sync_playwright() as p:
            context = p.request.new_context(base_url=os.environ['uri_create_qa_smockin'])
            response = context.post(f"{os.environ['uri_create_qa_smockin']}create-qa", data=payload, headers=headers)
            LOG.log_info(f"URL: {os.environ['uri_create_qa_smockin']}create-qa")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    # Método chamando funções para validar response
    @staticmethod
    def validate_response(response, code):
        ApiUtils.request_parse_log(response)
        ApiUtils.validate_status_code(response, code)

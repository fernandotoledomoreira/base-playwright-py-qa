import pytest
import os
from dotenv import load_dotenv
from pytests.support.log_service import LogService
from pytests.support.aws.aws_utils import AwsUtils
LOG = LogService

# Função do pytest para executar uma única vez antes de todos os testes
@pytest.fixture(scope="session", autouse=True)
def before_all():

    if os.getenv("aws_access_key_id_temp_qa") is None:
        load_dotenv()
    else:
        os.environ['region'] = "us-east-2"
        os.environ['env_run'] = os.environ['config_vars']

    if "dev" in os.environ.get("env_run"):
        os.environ['config'] = "dev"
        os.environ['account_number'] = os.environ.get("account_dev")
    elif "hml" in os.environ.get("env_run"):
        os.environ['config'] = "hml"
        os.environ['account_number'] = os.environ.get("account_hml")
    elif "qa" in os.environ.get("env_run"):
        os.environ['config'] = "qa"
        os.environ['account_number'] = os.environ.get("account_qa")

    credential = AwsUtils.credentials_aws()
    creds_api = AwsUtils.get_sm_secret_value(credential, "api-livaria-credentials")
    os.environ.update(creds_api)

# Função do pytest para executar antes e depois de cada teste
# antes de "yield" = before, depois de "yield" = after
@pytest.fixture(autouse=True)
def before_after():
    LOG.log_info("-----Before-----")
    yield
    LOG.log_info("-----After-----")
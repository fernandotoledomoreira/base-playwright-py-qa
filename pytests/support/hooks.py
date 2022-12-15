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
        os.environ['AWS_ACCESS_KEY_ID_TEMP_QA'] = os.environ['aws_access_key_id_temp_qa']
        os.environ['AWS_SECRET_ACCESS_KEY_TEMP_QA'] = os.environ['aws_secret_access_key_temp_qa']
        os.environ['ACCOUNT_DEV'] = os.environ['account_dev']
        os.environ['ACCOUNT_HML'] = os.environ['account_hml']
        os.environ['ACCOUNT_QA'] = os.environ['account_qa']
        os.environ['REGION'] = "us-east-2"
        os.environ['ENV_RUN'] = os.environ['config_vars']

    if "dev" in os.environ.get("ENV_RUN"):
        os.environ['CONFIG'] = "dev"
        os.environ['ACCOUNT_NUMBER'] = os.environ.get("ACCOUNT_DEV")
    elif "hml" in os.environ.get("ENV_RUN"):
        os.environ['CONFIG'] = "hml"
        os.environ['ACCOUNT_NUMBER'] = os.environ.get("ACCOUNT_HML")
    elif "qa" in os.environ.get("ENV_RUN"):
        os.environ['CONFIG'] = "qa"
        os.environ['ACCOUNT_NUMBER'] = os.environ.get("ACCOUNT_QA")

    credential = AwsUtils.credentials_aws()
    uris = AwsUtils.get_sm_secret_value(credential, f"cucumber_uris_{os.environ['CONFIG']}")
    access = AwsUtils.get_sm_secret_value(credential, f"cucumber_{os.environ['ENV_RUN']}")
    accounts = AwsUtils.get_sm_secret_value(credential, "cucumber_accounts_aws")
    os.environ.update(uris)
    os.environ.update(access)
    os.environ.update(accounts)


# Função do pytest para executar antes e depois de cada teste
# antes de "yield" = before, depois de "yield" = after
@pytest.fixture(autouse=True)
def before_after():
    LOG.log_info("-----gerando token ou buscando do redis-----")
    yield
    LOG.log_info("-----realizando qualquer acao necessaria-----")

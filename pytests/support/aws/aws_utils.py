import boto3
import os
import json
from pytests.support.log_service import LogService

LOG = LogService


class AwsUtils:

    # Método para realizar conexão com AWS
    @staticmethod
    def credentials_aws():
        try:
            sts_client = boto3.client('sts', aws_access_key_id=os.environ['aws_access_key_id_temp_qa'],
                                      aws_secret_access_key=os.environ['aws_secret_access_key_temp_qa'],
                                      region_name=os.environ['region'])
            role_credentials = sts_client.assume_role(
                RoleArn=f"arn:aws:iam::{os.environ['account_number']}:role/automationQA",
                RoleSessionName='Automation')

            session = boto3.Session(aws_access_key_id=role_credentials['Credentials']['AccessKeyId'],
                                    aws_secret_access_key=role_credentials['Credentials']['SecretAccessKey'],
                                    aws_session_token=role_credentials['Credentials']['SessionToken'],
                                    region_name=os.environ['region'])
        except Exception as e:
            LOG.log_error("Erro ao conectar via sts assume role")
            raise e
        return session

    # Método para consultar o serviço "secrets manager" da AWS
    @staticmethod
    def get_sm_secret_value(credential, secret_name):
        LOG.log_info(f"Iniciando busca do secrets: {secret_name}")
        try:
            secrets_client = credential.client('secretsmanager')
            resp = secrets_client.get_secret_value(SecretId=secret_name)
            secret = resp['SecretString']
        except:
            LOG.log_error("Erro retornado ao tentar buscar o secrets")
            secret = {}

        LOG.log_info("Busca finalizada no secrets")
        return json.loads(secret)

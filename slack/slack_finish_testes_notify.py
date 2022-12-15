import os
import datetime
from playwright.sync_api import sync_playwright
time = datetime.datetime.now()
import json

# Condicional para direcionar o caminho da pasta no S3 a fim de localizar as evidencias do allure report
if "dev" in os.environ.get("config_vars"):
    os.environ['config'] = "dev"
elif "hml" in os.environ.get("config_vars"):
    os.environ['config'] = "hml"
elif "qa" in os.environ.get("config_vars"):
    os.environ['config'] = "qa"

# Allure generate + montagem da url do report do S3 + url webhook do canal
os.system('allure generate reports/allure-results')
report_uri = f"https://report-tests.devtools.caradhras.io/{os.environ['JOB_NAME']}/{os.environ['config']}/{os.environ['BUILD_ID']}/index.html"
uri_webhook = "webhook canal"

# Leitura do arquivo json + condicional de cores do report + results com a quantidade de testes
with open('allure-report/history/history-trend.json') as file:
    data = json.load(file)

if data[0]['data']['failed'] > 0:
    color = '#ff0033'
else:
    color = '#00FF00'

results = json.dumps(data[0]['data'], indent=1, ensure_ascii=False)

# Payload no formato esperado pelo Slack
payload = {
    "username": "Report Automation Tests",
    "icon_url": "",
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": f'{color}',
            "author_link": "",
            "author_icon": "",
            "text": f"<!channel> \n *Tests Executed!* \n *Pipeline Name:* {os.environ['JOB_NAME']} \n *Enviroment: {os.environ['config_vars']}* \n *Report Link:* {report_uri} \n",
            "fields": [
                {
                    "title": "Results:",
                    "value": f"``` {results} ```",
                    "short": True
                }
            ],
            "image_url": "",
            "thumb_url": "",
            "footer": "QA Team",
            "footer_icon": ""
        }
    ]
}

# Headers para requisição do Slack
headers = {
    "Content-type": "application/json"
}

# Função do playwright para requisição do Slack
with sync_playwright() as p:
    context = p.request.new_context(base_url=uri_webhook)
    context.post(f"{uri_webhook}", data=payload, headers=headers)
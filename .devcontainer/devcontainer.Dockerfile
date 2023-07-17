FROM python:3.11

WORKDIR /base-playwright-py-qa
COPY . /base-playwright-py-qa

RUN apt-get update && \
    apt-get install -y vim python3-pip bash awscli git default-jre tzdata zip unzip && \
    curl -k https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py && \
    pip install --upgrade pip && \
    wget -q https://github.com/allure-framework/allure2/releases/download/2.22.0/allure-2.22.0.tgz && \
    tar -zxvf allure-2.22.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.22.0/bin/allure /usr/bin/allure && \
    rm -R allure-2.22.0.tgz && \
    chmod 777 -R /base-playwright-py-qa

ENV TZ=America/Sao_Paulo

ENTRYPOINT ["/bin/bash"]
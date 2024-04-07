FROM apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

RUN  pip install --upgrade pip && pip install --no-cache-dir -r /opt/airflow/requirements.txt && python -m textblob.download_corpora
